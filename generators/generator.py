import os
import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


class GeneratePerson:
    def __init__(self, language='ru_RU'):
        self.fake = Faker(language)
        self.result = {
            'firstname': self.fake.first_name(),
            'lastname': self.fake.first_name(),
            'age': random.randint(10, 80),
            'email': self.fake.email(),
            'salary': random.randrange(10000, 100000),
            'department': self.fake.job()
        }


class GenerateFile:
    def __init__(self, file_name='file.txt'):
        self.file_name = file_name
        self.current_dir = os.path.abspath(os.path.dirname(__file__))
        self.file_path = os.path.join(self.current_dir, self.file_name)
        self.file = None

    def create_file(self):
        self.file = open(self.file_path, 'w+')
        self.file.close()

    def delete_file(self):
        self.file.close()
        os.remove(self.file_path)
