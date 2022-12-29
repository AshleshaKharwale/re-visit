import yaml
import pymysql

with open("secret.yaml", "r") as f:
    doc = yaml.load(f, Loader=yaml.FullLoader)
    print(doc)
    # breakpoint()


conn = pymysql.connect(**doc)

print(conn)