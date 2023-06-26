from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase
from pydantic import BaseModel, PositiveInt


class Base(DeclarativeBase): pass


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    jobs = relationship("Job", back_populates="user")


class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)
    profession = Column(String)
    experience = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))

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
        return user.id


def add_job(user_id: int, profession: str, experience: int):
    with sessionmaker(bind=engine)() as session:
        job = Job(profession=profession, experience=experience, user_id=user_id)
        job.user_id = user_id
        session.add(job)
        session.commit()
        return job.id


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
            print(f"    Пользователь создан с id {user}")
        except ValueError as e:
            print(f"Validation error: {e}")
    elif table == "jobs":
        profession = input("    Введите профессию: ")
        experience = input("    Введите опыт работы по специальности: ")
        user_id = int(input("    Введите пользовательский id: "))
        job = add_job(user_id, profession, experience)
        print(f"    Вакансия создана с id {job}")


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

    while True:
        try:
            table_choice = int(input("    Выберите таблицу: "))
            break
        except ValueError:
            print('Пожалуйста введите ЧИСЛО')

    if table_choice not in [1, 2]:
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
        while True:
            try:
                action_choice = int(input("    Выберите действие: "))
                break
            except ValueError:
                print('Пожалуйста введите ЧИСЛО')

        if action_choice == 1:
            break
        elif action_choice == 2:
            insert_data(table)
        elif action_choice == 3:
            get_all_data(table)
        else:
            print("Неверный номер действия :( попробуйте ещё раз.")