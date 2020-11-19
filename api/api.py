import requests


class BaseApi(object):
    method = ''
    url = ''
    cookies = {}
    header = {}
    params = ''
    data = ''
    json = ''

    def __init__(self):
        self.response = None

    def set_cookie(self, key, value):
        self.cookies.update({key: value})
        return self

    def set_params(self, params: dict):
        self.params = params
        return self

    def set_data(self, data: dict):
        self.data = data
        return self

    def set_json(self, json: dict):
        self.json = json
        return self

    def run(self, session=None):
        session = session or requests.sessions.Session()
        self.response = session.request(
            self.method,
            self.url,
            cookies=self.cookies,
            headers=self.header,
            json=self.json,
            data=self.data,
            params=self.params)
        return self

    def extract(self, key):
        value = self.response
        for _key in key.split('.'):
            if isinstance(value, requests.Response):
                if _key in ['json()', 'json']:
                    value = self.response.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict,dict)):
                value = value[_key]
        return value

    def validate(self, key, expected_value):
        value = self.extract(key)
        assert value == expected_value
        return self

    def get_response(self):
        return self.response

