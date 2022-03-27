from flask import Flask
import xmltodict as xd
import json
import logging

app = Flask(__name__)

epoch_data = {}
sighting_data = {}
#Read the two xml files
@app.route('/read_data', methods=['POST'])
def read_data_to_dict():
    """
    This route reads two XML data files and confirms they have been read.
    """
    logging.info("Reading data.")
    global epoch_data
    global sighting_data

    with open('ISS.OEM_J2K_EPH.xml' , 'r') as f:
        epoch_data =  xd.parse(f.read())

    with open('XMLsightingData_citiesINT01.xml' , 'r') as f:
        sighting_data = xd.parse(f.read())

    return f'Data has been read from file\n'

#Information on how to interact with the application
@app.route('/help', methods=['GET'])
def help():
    """
    Outputs information on each route including the results from each
    """
    logging.info("Information on each route is being outputted on the screen for your reference.")
    describe = "ISS Sighting Location\n"
    describe += "/                                                      (GET) print this information\n"
    describe += "/read_data                                             (POST) reset data, load from file\n"
    describe += "Routes for Querying Positional and Velocity Data:\n\n"
    describe += "/epochs                                                (GET) lists all epochs in positional and velocity data\n"
    describe += "/epochs/<epoch>                                        (GET) lists all data associated with a specific epoch\n"
    describe += "Routes for Querying Sighting Data\n\n"
    describe += "/countries                                             (GET) lists all countries in sighting data\n"
    describe += "/countries/<country>                                   (GET) lists all data for a specific country\n"
    describe += "/countries/<country>/regions                           (GET) lists all regions in a specific country\n"
    describe += "/countries/<country>/regions/<regions>                 (GET) lists all data for a specific region\n"
    describe += "/countries/<country>/regions/<regions>/cities          (GET) lists all cities in a specific region\n"
    describe += "/countries/<country>/regions/<regions>/cities/<city>   (GET) lists all data for a specific city \n"
    return describe


#All Epochs in the positional data
@app.route('/EPOCH', methods=['GET'])
def all_epochs():
    """
    Loops all EPOCH dictionaries
    Returns:
    All EPOCHs in positional data
    """
    logging.info("Getting all epochs...")
    EPOCH = ""
    for i in range(len(epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'])):
        EPOCH = EPOCH + epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] + '\n'
    return EPOCH

#All information about a specific Epoch in the positional data
@app.route('/<epoch>', methods=['GET'])
def get_epoch_data(epoch: str):
    """
    Loops through all of the state vectors in the ISS EPOCH DATA dictionary. Returns all the positional and velocity values of the specified epoch. 
    Args:
    epoch (str): EPOCH value
    Returns:
    epoch_dict (dictionary): All information about the specified epoch (positional and velocity)
    """
    logging.info(f"Gettting {epoch}")
    epoch_index = 0
    i = 0
    while(epoch == epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH']):
        i+= -1
    epoch_index = i

    positional_velocity_data = ['X', 'Y', 'Z', 'X_DOT', 'Y_DOT', 'Z_DOT']
    epoch_dict = {}
    for p_v in positional_velocity_data:
        epoch_dict[p_v] = epoch_data['ndm']['oem']['body']['segment']['data']['stateVector'][epoch_index][p_v]
    return epoch_dict

#All Countries from the sighting data
@app.route('/countries',methods=['GET'])
def all_countries():
    """
    Obtains the country key of sightings data
    Returns:
    all_countries (dict): Dictionary of every unique country in sightings data
    """
    logging.info("Obtaining all country data ")
    all_countries = {}
    for i in range(len(sighting_data['visible_passes']['visible_pass'])):
        if sighting_data['visible_passes']['visible_pass'][i]['country'] in all_countries:
            all_countries[sighting_data['visible_passes']['visible_pass'][i]['country']] += 1
        else:
            all_countries[sighting_data['visible_passes']['visible_pass'][i]['country']] = 1
    return all_countries

#All information about a specific Country in the sighting data
@app.route('/COUNTRY/<country>', methods=['GET'])
def get_country_data(country):
    """
    Iterates through visibale passes and gets the information associated with a user specified country.
    Args:
    country (str): Country to query for
    Returns:
    dict_list (list): Specified countries information.
    """
    logging.info(f"Getting info for  {country}")
    dict_list = []
    country_data = ['region', 'city', 'spacecraft', 'sighting_date','duration_minutes','max_elevation','enters','exits','utc_offset','utc_time', 'utc_date']
    for i in range(len(sighting_data['visible_passes']['visible_pass'])):
        if country == sighting_data['visible_passes']['visible_pass'][i]['country']:
            country_dict = {}
            for j in country_data:
                country_dict[j] = sighting_data['visible_passes']['visible_pass'][i][j]
            dict_list.append(country_dict)
    return json.dumps(dict_list, indent=2)

#All Regions associated with a given Country in the sighting data
@app.route('/COUNTRY/<country>/regions',methods=['GET'])
def all_regions(country):
    """
    Iterates through all regions in a specified country. 
    Args:
    country (str): Country to find the regions for. 
    Returns:
    all_regions (dictionary): Dictionary containing all regions in a specified country. 
    """
    logging.info(f"Obtaining all regions in {country}")
    all_regions = {}
    for i in range(len(sighting_data['visible_passes']['visible_pass'])):
        if country == sighting_data['visible_passes']['visible_pass'][i]['country']:
            region = sighting_data['visible_passes']['visible_pass'][i]['region']
            if region in all_regions:
                all_regions[region] += 1
            else:
                all_regions[region] = 1
    return all_regions

#All information about a specific Region in the sighting data
@app.route('/COUNTRY/<country>/regions/<regions>',methods=['GET'])
def get_region_data(country, regions):
    """
    Gets all information associated with specified region. 
    Args:
    country (str): Country to search in
    regions (str): Region to search in 
    Returns: dict_list (list): contains all the information about a specific region
    """
    logging.info(f"Getting information about {regions}")
    dict_list = []
    list_region_data = ['city', 'spacecraft', 'sighting_date','duration_minutes','max_elevation','enters',\
'exits','utc_offset','utc_time', 'utc_date']
    for i in range(len(sighting_data['visible_passes']['visible_pass'])):
        if country == sighting_data['visible_passes']['visible_pass'][i]['country']:
            if regions == sighting_data['visible_passes']['visible_pass'][i]['region']:
                region_dict = {}
                for j in list_region_data:
                    region_dict[j] = sighting_data['visible_passes']['visible_pass'][i][j]
                dict_list.append(region_dict)
    return json.dumps(dict_list, indent=2)

#All Cities associated with a given Country and Region in the sighting data
@app.route('/COUNTRY/<country>/regions/<regions>/cities',methods=['GET'])
def all_cities(country, regions):
    """
    Finds all cities within a specified country and region. 
    Args:
    country (str): Country to search in 
    regions (str): Region to search in 
    Returns:
    all_cities (dictionary): A dictionary of cities within a specified country/region
    """
    logging.info(f"Getting all cities within {country} and {regions}")
    all_cities = {}
    for i in range(len(sighting_data['visible_passes']['visible_pass'])):
        if country == sighting_data['visible_passes']['visible_pass'][i]['country']:
            if regions == sighting_data['visible_passes']['visible_pass'][i]['region']:
                city = sighting_data['visible_passes']['visible_pass'][i]['city']
                if city in all_cities:
                    all_cities[city] +=1
                else:
                    all_cities[city]=1
    return all_cities
#All information about a specific City in the sighting data
@app.route('/COUNTRY/<country>/regions/<regions>/cities/<cities>',methods=['GET'])
def get_city_data(country, regions, cities):
    """
    Gets information for specified cities within specified regions and countries
    Args:
    country (str): Country to search in 
    regions (str): Region to search in 
    cities (str): City to search in 
    Returns:
    dict_list (list): City information
    """
    logging.info("Querying route to obtain info about /"+cities)
    dict_list = []
    city_data = ['spacecraft', 'sighting_date','duration_minutes','max_elevation','enters',\
'exits','utc_offset','utc_time', 'utc_date']
    for i in range(len(sighting_data['visible_passes']['visible_pass'])):
        if country == sighting_data['visible_passes']['visible_pass'][i]['country']:
            if regions == sighting_data['visible_passes']['visible_pass'][i]['region']:
                if cities == sighting_data['visible_passes']['visible_pass'][i]['city']:
                    city_dict = {}
                    for j in city_data:
                        city_dict[j] = sighting_data['visible_passes']['visible_pass'][i][j]
                    dict_list.append(city_dict)
    return json.dumps(dict_list, indent=2)
if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')


