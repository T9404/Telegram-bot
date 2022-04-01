from data import config
import psycopg2


def create_table():
    connect = psycopg2.connect(
        dbname=config.dbname, user=config.user, password=config.password, host=config.host)
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS news(
                                link varchar,
                                title varchar NOT NULL,
                                content varchar,
                                publish_date varchar
                                );""")
    connect.commit()
    connect.close()


def del_table():
    connect = psycopg2.connect(
        dbname=config.dbname, user=config.user, password=config.password, host=config.host)
    cursor = connect.cursor()
    cursor.execute("""DROP TABLE news""")
    connect.commit()


def insert_news(col1, col2, col3, col4):
    create_table()

    connection = psycopg2.connect(
        dbname=config.dbname, user=config.user, password=config.password, host=config.host)
    cursor = connection.cursor()

    insert_query = """INSERT INTO news (link, title, content, publish_date) VALUES (%s, %s, %s, %s)"""
    item_tuple = (col1, col2, col3, col4)
    cursor.execute(insert_query, item_tuple)
    connection.commit()


def check_news(title_search):
    connection = psycopg2.connect(
        dbname=config.dbname, user=config.user, password=config.password, host=config.host)

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM news WHERE title = %s', (title_search, ))
    data = cursor.fetchone()

    if data is None:
        connection.close()
        return False
    else:
        print('[X] Such a record already exists.')
        connection.close()
        return True


def get_data_from_db():
    connection = psycopg2.connect(
        dbname=config.dbname, user=config.user, password=config.password, host=config.host)

    cursor = connection.cursor()
    cursor.execute("""SELECT title, link, publish_date FROM news""")
    data_set = cursor.fetchmany(5)

    return data_set
