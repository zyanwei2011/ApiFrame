import requests


class BaseApi(object):
    method = ''
    url = ''
    cookies = {}
    header = {}
    # data = {}
    json = {}
    params = {}

    def set_params(self, **params):
        self.params = params
        return self

    # def set_data(self, data):
    #     self.data = data
    #     return self

    def set_json(self, json):
        self.json = json
        return self

    def run(self):
        self.response = requests.request(
            self.method,
            self.url,
            cookies=self.cookies,
            headers=self.header,
            json=self.json,
            # data=self.data,
            params=self.params)
        return self

    def validate(self, key, expected_value):
        value = self.response
        for _key in key.split('.'):
            if isinstance(value, requests.Response):
                if _key in ['json()', 'json']:
                    value = self.response.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict,dict)):
                value = value[_key]
        assert value == expected_value
        return self