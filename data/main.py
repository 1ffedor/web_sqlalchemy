from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    users = {"name": ["Ridley", "Vladimir", "Petr", "Yan"],
             "surname": ["Scott", "Evgrafov", "Smirnov", "Solntsev"],
             "age": [21, 17, 30, 20],
             "position": ["captain", "sailor", "cook", "navigator"],
             "speciality": ["research engineer", "programmer", "chef", "geographer"],
             "address": ["module_1" for i in range(4)],
             "email": ["scott_chief@mars.org", "Vladimir.E@mars.org", "22Petr22@mars.org", "yayan@mars.org"]}
    db_sess = db_session.create_session()
    for num in range(4):
        user = User()
        user.name = users["name"][num]
        user.surname = users["surname"][num]
        user.age = users["age"][num]
        user.position = users["position"][num]
        user.speciality = users["speciality"][num]
        user.address = users["address"][num]
        user.email = users["email"][num]
        db_sess.add(user)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()