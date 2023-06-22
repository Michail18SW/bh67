from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, PositiveInt

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    jobs = relationship("Job", back_populates="user")


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    profession = Column(String)
    experience = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="jobs")


class UserSchema(BaseModel):
    name: str
    age: PositiveInt


engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)


def create_user(name: str, age: int):
    with sessionmaker(bind=engine)() as session:
        user_schema = UserSchema(name=name, age=age)
        user = User(**user_schema.dict())
        session.add(user)
        session.commit()
        return user


def add_job(user_id: int, profession: str, experience: int):
    with sessionmaker(bind=engine)() as session:
        job = Job(profession=profession, experience=experience)
        session.add(job)
        session.commit()
        return job


def get_all_users():
    with sessionmaker(bind=engine)() as session:
        return session.query(User).all()


def get_all_jobs():
    with sessionmaker(bind=engine)() as session:
        return session.query(Job).all()


def print_table_list():
    print("    1. Пользователи")
    print("    2. Вакансии")


def print_actions_list():
    print("    1. Назад к списку таблиц")
    print("    2. Внести данные")
    print("    3. Получить все данные")


def insert_data(table):
    if table == "users":
        name = input("    Введите имя: ")
        age = int(input("    Введите возраст: "))
        try:
            user = create_user(name, age)
            print(f"    Пользователь создан с id {user.id}")
        except ValueError as e:
            print(f"Validation error: {e}")
    elif table == "jobs":
        profession = input("    Введите профессию: ")
        experience = input("    Введите опыт работы по специальности: ")
        user_id = int(input("    Введите пользовательский id: "))
        job = add_job(user_id, profession, experience)
        print(f"    Вакансия создана с id {job.id}")


def get_all_data(table):
    if table == "users":
        users = get_all_users()
        print("    Пользователи: ")
        for user in users:
            print(f"        id: {user.id}, имя: {user.name}, возраст: {user.age}")
    elif table == "jobs":
        jobs = get_all_jobs()
        print("    Вакансии: ")
        for job in jobs:
            print(f"        id: {job.id}, профессия: {job.profession}, опыт работы по специальности: {job.experience}, пользовательский id: {job.user_id}")


while True:
    print("Список таблиц: ")
    print_table_list()
    table_choice = int(input("    Выберите таблицу: "))
    if table_choice not in [1,2]:
        print("Неверный номер таблицы :( попробуйте ещё раз.")
        continue

    if table_choice == 1:
        print('Выбрана таблица "Пользователи"')
        table = "users"
    elif table_choice == 2:
        print('Выбрана таблица "Вакансии"')
        table = "jobs"

    while True:
        print("Действия с таблицами: ")
        print_actions_list()
        action_choice = int(input("    Выберите действие: "))

        if action_choice == 1:
            break
        elif action_choice == 2:
            insert_data(table)
        elif action_choice == 3:
            get_all_data(table)
        else:
            print("Неверный номер действия :( попробуйте ещё раз.")

