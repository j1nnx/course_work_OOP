from abc import ABC, abstractmethod

import requests


class JobPlatformAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str):
        pass


class HeadHunterAPI(JobPlatformAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def connect(self):
        pass

    def get_vacancies(self, search_query: str):
        params = {"text": search_query, "per_page": 20}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()["items"]
        else:
            raise Exception(f"Ошибка подключения: {response.status_code}")
