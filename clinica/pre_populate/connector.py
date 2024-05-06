import psycopg2
from dotenv import load_dotenv


class Database:
    def __init__(self, database, user, password, host, port):
        self.conn = None
        self.cur = None
        self.string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

    def execute(self, query, data: tuple = None, fetchone=False, commit=False):
        try:
            self.conn = psycopg2.connect(self.string)
            self.cur = self.conn.cursor()
            self.cur.execute(query, data)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        else:
            if commit:
                self.conn.commit()
            return self.cur.fetchall() if not fetchone else self.cur.fetchone()
        finally:
            try:
                self.conn.close()
                self.cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
