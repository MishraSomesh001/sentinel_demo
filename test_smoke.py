import requests

def test_importable():
    assert requests.__version__

def test_has_get():
    assert callable(requests.get)
