import pymysql


def get_db_connection(db_name):
    connection = pymysql.connect(user="root",
                                 host="localhost",
                                 port=3306,
                                 password='Ash@95kh',
                                 database=db_name)
    # breakpoint()
    return connection


with get_db_connection("starwarsdb") as conn:
    cur = conn.cursor()
    cur.execute("select * from film;")
    film_data = cur.fetchall()
    print(list(film_data))


# with open("abc.txt") as fobj:
#     pass
#
