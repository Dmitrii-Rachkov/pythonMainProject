import datetime
import os


class Logger():
    # В переменной file_name будет храниться название нашего файла с логами
    file_name = f"D:\\Projects\\pythonMainProject\\logs\\log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    # Используем метода класса, который обозначается декоратором @classmethod
    # Методы класса привязаны к самому классу, а не к его экземпляру.
    # Они могут менять состояние класса, что отразиться на всех объектах этого класса,
    # но не могут менять конкретный объект.

    # Метод 'write_log_to_file' записывает данные в наш файл.
    # cls - эта некая ссылка на наш класс, такая же как мы использовали self, только когда мы используем
    # classmethod нам необходимо использовать cls
    # data: str - обязательный атрибут метода, это данные которые будут поступать в формате строки

    # Конструкция 'with' и 'as' с помощью которой мы открываем наш файл,
    # указываем название нашего файла - 'cls.file_name'
    # Указываем ключ, что мы будем туда записывать данные - 'a'
    # Указываем кодировку наших данных - encoding='utf=8'
    # После этого указываем что наша конструкция будет переменной под названием logger_file
    # Далее обращаемся к нашей переменной чтобы записать данные - logger_file.write(data)
    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    # Метод 'add_start_step' говорит нам о том какие действия будут производится перед запуском
    # каждого нашего метода, например метод авторизации или помещения товара в корзину и т.д.

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    # Метод add_end_step говорит нам о том какие действия будут производиться
    # после окончания работы метода
    @classmethod
    def add_end_step(cls, url: str, method: str):

        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)
