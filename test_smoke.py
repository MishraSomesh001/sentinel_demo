import django

def test_importable_and_major_version():
    assert django.VERSION[0] >= 3
