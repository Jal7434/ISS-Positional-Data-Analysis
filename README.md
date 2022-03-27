<h1>Specificity for Information from the ISS</h1> 

<h2> Introduction </h2>
This project allows users to go through large amounts of data from the International Space Station (ISS) and access specific information about the ISS. 
The project uses two files one which contains the positional data and the other which contains sighting data from the ISS about certain cities Internationally.

<h2>  Important Information before Starting with code </h2>
To begin one will need two xml files which contain the data that is required to be read for the code to work.
This project will be using the two following data sets. For additional data sets you can visit NASA's site under https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq for more information and other data samples.

<h3> ISS Positional and Velocity Data </h3>
  
  - This file can be found in the following url [ISS_COORDS](https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml) or going to the NASA ISS Coordinate under this url to see the rest of the data and selecting the first xml file that is available https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq
  
  - The file can additionally be downloaded from the terminal using the ```wget```command and copying the link for the file that is needed to be downloaded ``` wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml ```
 <h3> ISS Sighting data for International 01 </h3>
 
  * The file can be found in the following url ([INT01_Sighting_Data](https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesINT01.xml)) or can also be found in the NASA ISS Coordinate page under this url https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq
  - It can also be retrieved by using the ```wget``` under the same pretext as ```wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesINT01.xml ``` 

<h2> Additional Starting Setup </h2>

<h3> Building Docker Container </h3>

The file for the Docker setup is already included in the file under the name ```Dockerfile``` 
  - <h4> Dockerfile </h4>

    - To begin you want to Touch a file named ```Dockerfile``` into the derectory by using the command ```touch Dockerfile```
    
    - Additionally there is a Makefile that will help to facilitate the process
    - Simply use ```make all``` to have the container made and run 

<h2> Using Flask </h2>

  - to Begin the following commands are required to set up the flask enviornment
  - ``` 
        export FLASK_APP =app.py
        export FLASK_APP=development
        flask run -p 50XX
    ```
  - replace the XX from the ```50XX``` with a different port number as if one is already being used the Flask operation will not work for this demonstration ```5017``` was used.
  - Initiallize the Flask application on a seperate commandline and on the second command like the following command can be used to ensure that the flask is operational and is reading the flask file correctly ``` curl localhost:5017/read_data -X post'''
  - using ``` curl localhost:5017/help ``` will provide a helpful list of the commands that are available to be used for this application.
  - The following is an example of input and output data of the application.
``` 
[jal7434@isp02 ~]$ curl localhost:5017/COUNTRY/Canada/regions/Quebec/cities/Alma
[
  {
    "spacecraft": "ISS",
    "sighting_date": "Sat Feb 19/05:42 AM",
    "duration_minutes": "5",
    "max_elevation": "22",
    "enters": "10 above SSW",
    "exits": "10 above E",
    "utc_offset": "-5.0",
    "utc_time": "10:42",
    "utc_date": "Feb 19, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Sun Feb 20/04:55 AM",
    "duration_minutes": "4",
    "max_elevation": "14",
    "enters": "10 above S",
    "exits": "10 above ESE",
    "utc_offset": "-5.0",
    "utc_time": "09:55",
    "utc_date": "Feb 20, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Mon Feb 21/05:41 AM",
    "duration_minutes": "6",
    "max_elevation": "46",
    "enters": "10 above SW",
    "exits": "10 above ENE",
    "utc_offset": "-5.0",
    "utc_time": "10:41",
    "utc_date": "Feb 21, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Tue Feb 22/04:55 AM",
    "duration_minutes": "4",
    "max_elevation": "31",
    "enters": "23 above S",
    "exits": "10 above E",
    "utc_offset": "-5.0",
    "utc_time": "09:55",
    "utc_date": "Feb 22, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Wed Feb 23/04:09 AM",
    "duration_minutes": "2",
    "max_elevation": "19",
    "enters": "19 above ESE",
    "exits": "10 above E",
    "utc_offset": "-5.0",
    "utc_time": "09:09",
    "utc_date": "Feb 23, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Wed Feb 23/05:42 AM",
    "duration_minutes": "6",
    "max_elevation": "90",
    "enters": "14 above WSW",
    "exits": "10 above ENE",
    "utc_offset": "-5.0",
    "utc_time": "10:42",
    "utc_date": "Feb 23, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Thu Feb 24/04:55 AM",
    "duration_minutes": "4",
    "max_elevation": "65",
    "enters": "45 above SW",
    "exits": "10 above ENE",
    "utc_offset": "-5.0",
    "utc_time": "09:55",
    "utc_date": "Feb 24, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Fri Feb 25/04:09 AM",
    "duration_minutes": "2",
    "max_elevation": "29",
    "enters": "29 above E",
    "exits": "10 above ENE",
    "utc_offset": "-5.0",
    "utc_time": "09:09",
    "utc_date": "Feb 25, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Fri Feb 25/05:42 AM",
    "duration_minutes": "6",
    "max_elevation": "58",
    "enters": "16 above W",
    "exits": "10 above ENE",
    "utc_offset": "-5.0",
    "utc_time": "10:42",
    "utc_date": "Feb 25, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Sat Feb 26/03:23 AM",
    "duration_minutes": "< 1",
    "max_elevation": "10",
    "enters": "10 above E",
    "exits": "10 above E",
    "utc_offset": "-5.0",
    "utc_time": "08:23",
    "utc_date": "Feb 26, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Sat Feb 26/04:56 AM",
    "duration_minutes": "4",
    "max_elevation": "71",
    "enters": "54 above W",
    "exits": "10 above ENE",
    "utc_offset": "-5.0",
    "utc_time": "09:56",
    "utc_date": "Feb 26, 2022"
  }
```

These results show the information taken from the ISS positional and sighting data and offers a more understandable and readable format than simply reading it straight from the XML file.
<h2> Citations </h2>
Goodwin, S. (n.d.). ISS_COORDS_2022-02-13. NASA. https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml Retrieved March 27, 2022, from https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq
Goodwin, S. (n.d.). XMLsightingData_citiesINT01. NASA. https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesINT01.xml Retrieved March 27, 2022, from https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq

  
