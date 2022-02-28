from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

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
    jobs_data = {"team_leader": [1, 1, 1, 1],
                 "job": ["deployment of residential modules 1 and 2", "cleaning modules 1 and 2",
                         "cooking", "determining the route"],
                 "work_size": [15, 20, 20, 20],
                 "collaborations": ["2, 3", "1, 3", "1, 2", "1, 2, 3"],
                 "start_date": [datetime.datetime.now() for i in range(4)],
                 "is_finished": [False, False, False, False]}
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

        jobs = Jobs()
        jobs.team_leader = jobs_data["team_leader"][num]
        jobs.job = jobs_data["job"][num]
        jobs.work_size = jobs_data["work_size"][num]
        jobs.collaborations = jobs_data["collaborations"][num]
        jobs.start_date = jobs_data["start_date"][num]
        jobs.is_finished = jobs_data["is_finished"][num]
        db_sess.add(jobs)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()