"""
step 1 : connect to database
step 2: create cursor
step 3: execute query using cursor
        a. if query is to modify table ( insert, update, delete) --> connection.commit()
step 4: close connection
"""

import pymysql
#step1

connection = pymysql.connect(user="root",
                             host="localhost",
                             port=3306,
                             password='Ash@95kh',
                             database="starwarsdb")
#step2
cursor1 = connection.cursor()

#step3
# result1 = cursor1.execute("show tables;")
# print(result1)
# tables = cursor1.fetchall()
# for table in tables:
#     print(table)
#
# cursor2 = connection.cursor()
# result2 = cursor2.execute("select * from species_sample;")
# print(result2)
# char_data = cursor2.fetchall()
# for char in char_data:
#     print(char)

cursor3 = connection.cursor()
result3 = cursor3.execute("insert into species_sample values (104, '4 cm', '10 days', Null)")
connection.commit()
print(result3)

#step 4
connection.close()


