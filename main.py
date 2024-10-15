from src.api import HeadHunterAPI
from src.file_manager import JSONSaver
from src.vacancy import Vacancy


def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = [
        Vacancy(v["name"], v["alternate_url"], v["salary"], v["snippet"]["responsibility"]) for v in vacancies
    ]

    top_vacancies = sorted(vacancies_list, reverse=True)[:top_n]
    for vacancy in top_vacancies:
        print(vacancy)

    saver = JSONSaver()
    for vacancy in top_vacancies:
        saver.add_vacancy(vacancy)


if __name__ == "__main__":
    user_interaction()
