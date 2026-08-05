import requests


def test_requests_importable():
    assert requests.__version__


def test_requests_has_get():
    assert callable(requests.get)
