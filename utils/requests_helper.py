import logging

import allure
import curlify
from requests import Session


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
        message = curlify.to_curl(response.request)
        with allure.step(f'{response.request.method} {response.request.url}'):
            allure.attach(
                body=message.encode('utf8'),
                name=f'Request {response.request.method} {response.status_code}',
                attachment_type=allure.attachment_type.TEXT,
                extension='txt'
            )
            if method is not 'DELETE':
                allure.attach(
                    body=str(response.json()).encode('utf-8'),
                    name='Response JSON',
                    attachment_type=allure.attachment_type.TEXT,
                    extension='txt'
                )
        return response