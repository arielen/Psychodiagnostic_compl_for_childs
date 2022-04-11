import json
# from anxiety import data as anx_data


class ScaleOfPersonalAnxiety:

    def __init__(self, gender: str = "Мужчина", age: int = 0) -> None:
        self.data = self.__create_data(
            "Шкала личностной тревожности для учащихся 10-16 лет")
        self.rating = self.data['rating']
        self.school = self.selfreported = 0
        self.interpersonal = self.magical = 0
        self.age = age
        self.gender = gender
        self.result = 0

    def __create_data(self, name_test,) -> dict:
        with open("tests/tests_data.json", 'r', encoding="utf-8") as f:
            return json.load(f)[name_test]

    def get_result(self) -> dict:
        pass

    def check_anxiety(self, anxiety: str) -> dict:
        return anx_data[anxiety]

    def check_age(self, age: int) -> dict:
        pass

    def check_gender(self, gender: str) -> dict:
        pass

    def __str__(self) -> str:
        return str(self.rating)


class FormA(ScaleOfPersonalAnxiety):

    def __init__(self, age: int, gender: str) -> None:
        super().__init__(age=age, gender=gender)


def main():
    A = FormA(10)
    print(A)

    # with open("tests/asd.txt", 'r', encoding='utf-8') as f:
    #     data = [_.strip().format('\n', '') for _ in f]

    # [print(f'"{_}",') for _ in data]

    A.check_anxiety('Общая')

    x = 65
    age = 10
    gender = "girls"


if __name__ == "__main__":
    main()
