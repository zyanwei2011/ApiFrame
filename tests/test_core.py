from tests.api.httpbin import *


def test_version():
    from api import __version__
    assert isinstance(__version__, str)


def test_httpbin_get():
    APiHttpGet().set_params(a='46')\
        .run()\
        .validate('status_code', 200)\
        .validate('headers.server', 'gunicorn/19.9.0')\
        .validate('json().args.a', '46')


def test_httpbin_post():
    APiHttpPost().set_json({'m': 9999})\
        .run()\
        .validate('status_code', 200)\
        .validate('headers.server', 'gunicorn/19.9.0')\
        .validate('json().args.a', '123')







