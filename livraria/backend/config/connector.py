import mysql.connector


class Connector:
    __instance: 'Connector' = None

    def __new__(cls, *args, **kwargs) -> 'Connector':
        if cls.__instance is None:
            cls.__instance = super(Connector, cls).__new__(cls)
        return cls.__instance

    def __init__(self, **kwargs) -> None:
        self.conn = None
        self.cur = None
        self.response = None

        self.params = kwargs.get('params')

    def __connect(self) -> mysql.connector.connection:
        return mysql.connector.connect(**self.params)

    def execute(self, sql: str, data: tuple = None, fetchone: bool = False, commit: bool = False):
        try:
            self.conn = self.__connect()
            self.cur = self.conn.cursor(dictionary=True)
            self.cur.execute(sql, data)
            response = self.cur.fetchone() if fetchone else self.cur.fetchall()
        except (mysql.connector.Error, AttributeError, TypeError) as err:
            print(err)
            raise ConnectionError
        else:
            if commit:
                self.conn.commit()
            return response
        finally:
            try:
                self.cur.close()
                self.conn.close()
            except (mysql.connector.Error, AttributeError, TypeError) as err:
                print(err)
                raise ConnectionError
