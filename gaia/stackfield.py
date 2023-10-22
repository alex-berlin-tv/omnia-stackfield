from .config import settings

import requests
from urllib import parse


URL_PREFIX = "https://www.stackfield.com/apiwh/"


class Stackfield:
    def task(self, title: str, content: str):
        headers = {"Content-Type": "application/json"}
        data = {
            "Title": title,
            "Content": content,
        }
        print(self.__task_url())
        response = requests.post(self.__task_url(), headers=headers, json=data)
        print(f"Response status {response.status_code}")
        print(f"Data {response.content}")

    def __task_url(self) -> str:
        return parse.urljoin(URL_PREFIX, settings.stackfield_task_uuid)