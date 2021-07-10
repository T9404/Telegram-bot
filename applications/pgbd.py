# pip install psycopg2
import psycopg2
from data import config


def create_base():
    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()
#    cursor.execute("""DROP TABLE subcribers""")
#    connect.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS subcribers(
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(255) NULL,
                                user_id BIGINT NOT NULL
                                );""")
    connect.commit()
    connect.close()

# create_base()
# print('База обновлена')


def add_subscriber(name, user_id):
    """Подписка"""
    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()

    # проверяем есть ли подписчик в базе
    cursor.execute(f'SELECT FROM subcribers WHERE user_id = {user_id}')
    data = cursor.fetchone()
    if data is None:
        # если нет, то заносим в базу
        cursor.execute(f"INSERT INTO subcribers(name, user_id) VALUES('{name}', {user_id});")
        connect.commit()
        text = 'Вы успешно подписались! ✔'
    else:
        text = 'Такой подписчик уже существует 😵'
    connect.close()
    return text


def unsubscribers(user_id):
    """Отписка"""
    # надо дописать проверку сущес
    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()
    cursor.execute(f'SELECT FROM subcribers WHERE user_id = {user_id}')
    data = cursor.fetchone()
    if data is None:
        text = 'Вы не были подписаны, что бы отписаться! 🔫'
    else:
        cursor.execute(f'DELETE FROM subcribers WHERE user_id = {user_id}')
        connect.commit()
        text = 'Вы успешно отписались! ❎'
    return text


def get_subscribers():
    """Выводим список подписчиков"""
    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM subcribers')
    users = cursor.fetchall()
    if len(users) == 0:
        text = 'Список подписчиков пуст!'
        return text
    else:
        return users


def message_to_subscribers():
    """Отправляем сообщение подписчикам"""
    create_base()
    connect = psycopg2.connect(dbname=config.dbname, user=config.user,
                               password=config.password, host=config.host)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM subcribers')
    users = cursor.fetchall()
    user_list = []
    for user in users:
        user_list.append(user[2])
    #print(user_list)
    return user_list