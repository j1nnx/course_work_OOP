import json
import os

from src.file_manager import JSONSaver
from src.vacancy import Vacancy


def create_temp_file(filename):
    with open(filename, "w") as f:
        json.dump([], f, ensure_ascii=False, indent=4)


def remove_temp_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


def test_delete_vacancy():
    temp_filename = "temp_vacancies.json"
    create_temp_file(temp_filename)

    vacancy1 = Vacancy(
        title="Python Developer",
        link="http://example.com",
        salary="1000 USD",
        description="Develop Python applications",
    )

    vacancy2 = Vacancy(title="Data Scientist", link="http://example.com", salary="1200 USD", description="Analyze data")

    json_saver = JSONSaver(filename=temp_filename)
    json_saver.add_vacancy(vacancy1)
    json_saver.add_vacancy(vacancy2)

    with open(temp_filename, "r") as file:
        data = json.load(file)
        assert len(data) == 2

    json_saver.delete_vacancy(vacancy1)

    with open(temp_filename, "r") as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]["title"] == "Data Scientist"

    remove_temp_file(temp_filename)
