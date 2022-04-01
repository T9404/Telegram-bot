import psycopg2
from data import config


def create_base():
    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS subcribers(
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(255) NULL,
                                user_id BIGINT NOT NULL
                                );""")
    connect.commit()
    connect.close()


def add_subscriber(name, user_id):

    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()

    cursor.execute(f'SELECT FROM subcribers WHERE user_id = {user_id}')
    data = cursor.fetchone()

    if data is None:
        cursor.execute(
            f"INSERT INTO subcribers(name, user_id) VALUES('{name}', {user_id});")
        connect.commit()
        text = 'You have successfully subscribed! ✔'
    else:
        text = 'Such a subscriber already exists😵'

    connect.close()

    return text


def unsubscribers(user_id):
    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()
    cursor.execute(f'SELECT FROM subcribers WHERE user_id = {user_id}')
    data = cursor.fetchone()

    if data is None:
        text = 'You were not subscribed to unsubscribe! 🔫'
    else:
        cursor.execute(f'DELETE FROM subcribers WHERE user_id = {user_id}')
        connect.commit()
        text = 'You have successfully unsubscribed! ❎'

    return text


def get_subscribers():
    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM subcribers')
    users = cursor.fetchall()

    if len(users) == 0:
        text = "Let's have a list of subscribers!"
        return text
    else:
        return users


def message_to_subscribers():
    create_base()
    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM subcribers')
    users = cursor.fetchall()

    user_list = []

    for user in users:
        user_list.append(user[2])

    return user_list
