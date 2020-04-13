# -*- coding: utf-8 -*-

from urllib import parse, request


class HttpClient(object):
    def __init__(self):
        self._response_data = None
        self._last_url = None

        request.install_opener(self.__get_opener())

    def send_request(self, url, params=None, timeout=30):
        post_data = parse.urlencode(params) if params else None

        response = request.urlopen(
            url, post_data.encode() if post_data else None, timeout
        )

        self._response_data = response.read()
        self._last_url = response.geturl()

    def get_response_text(self, encoding='utf-8'):
        return self._response_data.decode(encoding)

    def last_url(self):
        return self._last_url

    @staticmethod
    def __get_opener():
        return request.build_opener(
            request.HTTPHandler(),
            request.HTTPSHandler(),
            request.HTTPCookieProcessor()
        )


if __name__ == '__main__':
    client = HttpClient()
    client.send_request("https://ya.ru")
    
    print(client.last_url())
    print(client.get_response_text())
