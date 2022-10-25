from utils.requests_helper import BaseSession
import os


def reqres() -> BaseSession:
        reqres_api = os.getenv("api_url")
        return BaseSession(base_url=reqres_api)