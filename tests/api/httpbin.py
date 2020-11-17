from api.api import BaseApi


class APiHttpBinGet(BaseApi):

    url = 'http://www.httpbin.org/get'
    header = {'accept': 'application/json'}
    method = 'GET'
    cookies = {'cookies': ''}
    params = {'a': 123}


class APiHttpBinPost(BaseApi):
    url = 'http://www.httpbin.org/post'
    header = {'accept': 'application/json'}
    method = 'POST'
    cookies = {'cookies': ''}
    params = {'a': 123}
    json = {'m': ''}


class APiHttpBinCookies(BaseApi):
    url = 'http://www.httpbin.org/cookies'
    header = {'accept': 'application/json'}
    method = 'GET'
