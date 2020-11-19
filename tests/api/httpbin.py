from api.api import BaseApi


class APiHttpBinGet(BaseApi):

    url = 'http://www.httpbin.org/get'
    header = {'accept': 'application/json'}
    method = 'GET'
    params = {'a': 123}


class APiHttpBinPost(BaseApi):
    url = 'http://www.httpbin.org/post'
    header = {'accept': 'application/json'}
    method = 'POST'
    params = {'a': 123}
    json = {'m': ''}
    data = {'n': ''}


class APiHttpBinCookies(BaseApi):
    url = 'http://www.httpbin.org/cookies'
    header = {'accept': 'application/json'}
    method = 'GET'


class APiHttpBinSetCookies(BaseApi):
    url = 'http://www.httpbin.org/cookies/set'
    header = {'accept': 'text/plain'}
    method = 'GET'
    params = {'freeform': ''}
