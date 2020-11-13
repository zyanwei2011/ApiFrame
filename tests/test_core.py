from api import __version__
from api.api import BaseApi


def test_version():
    assert isinstance(__version__, str)


class TestHttpbin(BaseApi):

    url = 'http://www.httpbin.org/get'
    header = {'accept': 'application/json'}
    method = 'GET'
    cookies = {'cookies':''}
    params = {'a': 123}


def test_httpbin_get():
    TestHttpbin().run()\
        .validate('status_code', 200)\
        .validate('headers.server', 'gunicorn/19.9.0')\










