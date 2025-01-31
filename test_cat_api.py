import requests
from unittest.mock import patch
from cat_api import get_random_cat_image

def test_get_random_cat_image_success():
    mock_response = [{
        "id": "coi",
        "url": "https://cdn2.thecatapi.com/images/coi.jpg",
        "width": 459,
        "height": 375
    }]

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_random_cat_image()
        assert result == "https://cdn2.thecatapi.com/images/coi.jpg"

def test_get_random_cat_image_failure():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {}

        result = get_random_cat_image()
        assert result is None

def test_get_random_cat_image_empty_response():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []

        result = get_random_cat_image()
        assert result is None

def test_get_random_cat_image_exception():
    with patch("requests.get", side_effect=requests.RequestException):
        result = get_random_cat_image()
        assert result is None
