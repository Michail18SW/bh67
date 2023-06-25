from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, PositiveInt

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    jobs = relationship("Job", back_populates="user")


class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)
    specialty = Column(String)
    experience = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="job")


class UserSchema(BaseModel):
    name: str
    age: PositiveInt


engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def create_user(name: str, age: int):
    with Session() as session:
        user_schema = UserSchema(name=name, age=age)
        user = User(**user_schema.dict())
        session.add(user)
        session.commit()
        return user


def add_job(user_id: int, specialty: str, experience: int):
    with Session() as session:
        job = Job(specialty=specialty, experience=experience, user_id=user_id)
        session.add(job)
        session.commit()
        return job


def get_all_users():
    with Session() as session:
        return session.query(User).all()


def get_all_jobs():
    with Session() as session:
        return session.query(Job).all()


def print_table_list():
    print("    1. Пользователи")
    print("    2. Вакансии")


def print_actions_list():
    print("    1. Назад к списку таблиц")
    print("    2. Внести данные")
    print("    3. Получить все данные")


def insert_data(chart):
    if chart == "user":
        name = input("    Введите имя: ")
        age = int(input("    Введите возраст: "))
        try:
            user = create_user(name, age)
            print(f"    Пользователь создан с id {user.id}")
        except ValueError as e:
            print(f"Validation error: {e}")
    elif chart == "job":
        specialty = input("    Введите профессию: ")
        experience = int(input("    Введите опыт работы по специальности(лет): "))
        user_id = int(input("    Введите id пользователя: "))
        job = add_job(user_id, specialty, experience)
        print(f"    Вакансия создана с id {job.id}")


def get_all_data(chart):
    if chart == "user":
        users = get_all_users()
        if users:
            for user in users:
                print(f"    id: {user.id}, name: {user.name}, age: {user.age}")
        else:
            print('В таблице "Пользователи" пока нет данных. Вы можете их добавить прямо сейчас.')
    elif chart == "job":
        jobs = get_all_jobs()
        if jobs:
            for job in jobs:
                print(
                    f"    id: {job.id}, specialty: {job.specialty}, experience: {job.experience}, user_id: {job.user_id}")
        else:
            print('В таблице "Вакансии" пока нет данных. Вы можете их добавить прямо сейчас.')


while True:
    print('Список таблиц: ')
    print_table_list()
    table_choice = int(input("    Выберите таблицу: "))
    if table_choice not in [1, 2]:
        print("Неверный номер таблицы :( попробуйте ещё раз.")
        continue

    if table_choice == 1:
        print('Выбрана таблица "Пользователи"')
        chart = "users"
    elif table_choice == 2:
        print('Выбрана таблица "Вакансии"')
        chart = "jobs"
    else:
        print('Неверный номер таблицы :( попробуйте ещё раз.')

    while True:
        print('Действия с таблицами: ')
        print_actions_list()
        action_choice = int(input("    Выберите действие: "))

        if action_choice == 1:
            break
        elif action_choice == 2:
            insert_data(chart)
        elif action_choice == 3:
            get_all_data(chart)
        else:
            print('Неверный номер действия :( попробуйте ещё раз.')