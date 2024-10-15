import json

from src.vacancy import Vacancy


class JSONSaver:
    def __init__(self, filename="vacancies.json"):
        self.filename = filename

    def add_vacancy(self, vacancy: Vacancy):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(
            {"title": vacancy.title, "link": vacancy.link, "salary": vacancy.salary, "description": vacancy.description}
        )

        with open(self.filename, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return

        data = [v for v in data if v["title"] != vacancy.title]

        with open(self.filename, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
