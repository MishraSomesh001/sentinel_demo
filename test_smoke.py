import flask

def test_app_creates_and_responds():
    app = flask.Flask(__name__)

    @app.route('/ping')
    def ping():
        return 'pong'

    client = app.test_client()
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.data == b'pong'
