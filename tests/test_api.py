import requests_mock

from src.api import HeadHunterAPI


def test_get_vacancies_success():
    hh_api = HeadHunterAPI()
    search_query = "Python"

    with requests_mock.Mocker() as m:
        m.get(
            hh_api.base_url,
            json={"items": [{"id": "1", "name": "Python Developer"}, {"id": "2", "name": "Data Scientist"}]},
            status_code=200,
        )

        vacancies = hh_api.get_vacancies(search_query)

        # Проверяем длину списка вакансий и их содержание
        assert len(vacancies) == 2
        assert vacancies[0]["name"] == "Python Developer"
        assert vacancies[1]["name"] == "Data Scientist"


def test_get_vacancies_failure():
    hh_api = HeadHunterAPI()
    search_query = "Python"

    with requests_mock.Mocker() as m:
        m.get(hh_api.base_url, status_code=500)

        try:
            hh_api.get_vacancies(search_query)
        except Exception as e:
            assert str(e) == "Ошибка подключения: 500"
