from config import session
from time import sleep


def read_sql(filename):
    with open(session.sql_dir.joinpath(filename), "r", encoding='utf-8') as file:
        return file.read()


sleep(1)
session.execute(read_sql("tables.sql"))
sleep(1)
session.execute(read_sql("procedures.sql"))
sleep(1)
session.execute(read_sql("functions.sql"))
