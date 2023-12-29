import random, pprint
# from typing import List
from collections import defaultdict

"""
https://stackoverflow.com/questions/53144535/pythons-string-formatting-throws-error-when-applied-within-mysql
https://stackoverflow.com/questions/72478807/inserting-values-into-mysql-database-via-ssh-in-python-works-only-temporarily
https://stackoverflow.com/questions/40310511/remotely-connect-to-mysql-with-python-mysql-connector
https://stackoverflow.com/questions/20818155/not-all-parameters-were-used-in-the-sql-statement-python-mysql
https://stackoverflow.com/questions/58948094/connect-to-a-mysql-database-server-through-a-shell-script
https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone
"""


# MAKE DUMMY DATA
# def make_dummy_data(print_option: bool) -> List[List[str, str]]:
def make_dummy_data(print_option):
  ids = ['id1', 'id2', 'id3']
  numbers = []
  dates = ['2023-12-27', '2023-12-28', '2023-12-29']
  for i in range(len(ids)):
    for _ in range(3):
      number = ''
      for _ in range(12):
        number += str(random.randrange(0, 10))
      numbers.append([str(number) + ids[i], dates[i]])
  if print_option:
    pprint.pprint(numbers)
  return numbers


# CONNECT MYSQL DATABASE
import mysql.connector

cnx = mysql.connector.connect(
  host='hostname',
  database='database_name',
  user='user',
  password='password',
  port=3306,
  consume_results=True,
  autocommit=True)


# INSERT DUMMY DATA
# def insert_dummy_data(dummy_data: List[List[str, str]]) -> None:
def insert_dummy_data(cursor, dummy_data):  
  query = f'INSERT INTO client_access(client_id, check_dt) VALUES(%s, %s)'
  for number in numbers:
    result = cursor.execute(query, number)


def sort_ids(rows):
  result = defaultdict(list)
  for row in rows:
    same_id = ''
    name = row[0]
    date = row[7]
    if len(name) > 24:
      same_id = name[12:]
    else:
      same_id = name[:]
    result[same_id] = [name, date]
    print(result)

if cnx and cnx.is_connected():
  cursor = cnx.cursor()
  numbers = make_dummy_data(True)
  # insert_dummy_data(cursor, numbers)
  query = 'SELECT * FROM client_access'
  result = cursor.execute(query)
  rows = cursor.fetchall()
  # for row in rows:
  #    pprint.pprint(row)
  sort_ids(rows)
  cursor.close()
  cnx.close()
