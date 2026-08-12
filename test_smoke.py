import requests
import flask

def test_both_importable():
    assert requests.__version__
    assert flask.__version__
