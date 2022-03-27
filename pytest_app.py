import pytest
from app import *

read_data_to_dict()


def test_help():
    assert isinstance(help(), str) == True


def test_get_all_epochs():
    assert isinstance(all_epochs(), str) == True


def test_get_epoch_data():
    assert isinstance(get_epoch_data("input"), dict) == True


def test_get_all_countries():
    assert isinstance(all_countries(), dict) == True


def test_get_country_data():
    assert isinstance(get_country_data("input"), str) == True


def test_get_all_regions():
    assert isinstance(all_regions("input"), dict) == True


def test_get_region_data():
    assert isinstance(get_region_data("input", "input"), str) == True


def test_get_all_cities():
    assert isinstance(all_cities("input", "input"), dict) == True


def test_get_city_data():
    assert isinstance(get_city_data("input", "input", "input"), str) == True
