from api.api import BaseApi


class APiHttpGet(BaseApi):

    url = 'http://www.httpbin.org/get'
    header = {'accept': 'application/json'}
    method = 'GET'
    cookies = {'cookies': ''}
    params = {'a': 123}


class APiHttpPost(BaseApi):
    url = 'http://www.httpbin.org/post'
    header = {'accept': 'application/json'}
    method = 'POST'
    cookies = {'cookies': ''}
    params = {'a': 123}
    json = {'m': ''}