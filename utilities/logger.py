import datetime
import os


class Logger:
    file_name = f"C:\\Users\\user\\PycharmProjects\\Testing_Automation_and_Python_Programming_Selenium\\logs\\log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    # Записываем данные в файл
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    # Запускается до запуска методов
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Тест: {test_name}\n"
        data_to_add += f"Время начала выполнения теста: {str(datetime.datetime.now())}\n"
        data_to_add += f"Выполнялся метод : {method}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    # Записываем после отработки метода
    def add_end_step(cls, url: str, method: str):

        data_to_add = f"Время окончания теста: {str(datetime.datetime.now())}\n"
        data_to_add += f"Выполнился : {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)

