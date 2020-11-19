from tests.api.httpbin import *


def test_version():
    from api import __version__
    assert isinstance(__version__, str)


def test_httpbin_get():
    APiHttpBinGet().set_params({'a': '46'})\
        .run()\
        .validate('status_code', 200)\
        .validate('headers.server', 'gunicorn/19.9.0')\
        .validate('json().args.a', '46')

def test_httpbin_post():
    APiHttpBinPost().set_json({'m': 9999})\
        .set_data({'n': 88888})\
        .run()\
        .validate('status_code', 200)\
        .validate('headers.server', 'gunicorn/19.9.0')\
        .validate('json().args.a', '123')


def test_httpbin_extract():
    status_code = APiHttpBinCookies().run().extract('status_code')
    assert status_code == 200


def test_httpbin_set_cookies():
    APiHttpBinCookies()\
        .set_cookie('freeform1', 'test1') \
        .set_cookie('freeform2', 'test2') \
        .run()


def test_httpbin_login_status(init_session):
    # step1: login
    APiHttpBinSetCookies()\
        .set_params({'freeform': 'test'}) \
        .run(init_session)

    # step2: request whit session
    resp = APiHttpBinPost()\
        .set_data({'n': 88888})\
        .run(init_session).get_response()

    request_header = resp.request.headers
    assert 'freeform=test' in request_header['Cookie']












