import pymysql
import toml


with open("secrets.toml", "r") as foo:
    config = toml.load(foo)
    dbconfig = config.get("mysqldb")
    print(dbconfig)

    connection = pymysql.connect(**dbconfig)
    print(connection)
