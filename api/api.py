import requests


class BaseApi(object):
    method = ''
    url = ''
    cookies = {}
    header = {}
    data = {}
    json = {}
    params = {}

    def run(self):
        self.response = requests.request(
            self.method,
            self.url,
            cookies=self.cookies,
            headers=self.header,
            data=self.data,
            json=self.json,
            params=self.params)
        return self

    def validate(self, key, expected_value):
        value = self.response
        for _key in key.split('.'):
            if isinstance(value, requests.Response):
                value = getattr(value, _key)
            elif isinstance(value, requests.structures.CaseInsensitiveDict):
                value = value[_key]
        assert value == expected_value
        return self