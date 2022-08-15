from abc import abstractmethod, ABCMeta

# singleton and abstract method
import psycopg2
import psycopg2.extras


class DBConnector(metaclass=ABCMeta):
    _instance = None

    def __new__(cls, _uri, _name, _username, _password, _port):
        if cls._instance is None:
            print('Creating db connector with parameters : {} {} {} {} {}'.format(
                _uri, _name, _username, _password, _port
            ))
            cls._instance = super(DBConnector, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def disconnect(self): pass

    @abstractmethod
    def get_tables(self): pass

    @abstractmethod
    def get_status(self): pass


class PostgresSQLCon(DBConnector):
    def __init__(self, _uri, _name, _username, _password, _port):
        self.conn = None
        self.schema = None
        self.uri = _uri
        self.name = _name
        self.username = _username
        self.password = _password
        self.port = _port
        self.is_connected = False

    def connect(self):
        self.conn = psycopg2.connect(dbname=self.name,
                                     user=self.username,
                                     password=self.password,
                                     host=self.uri,
                                     port=self.port)
        if self.conn:
            self.is_connected = True
            print("PostgreSQL connected.")

    def disconnect(self):
        self.conn = None
        self.is_connected = False
        print("PostgreSQL disconnected.")

    def get_tables(self):
        if self.is_connected:
            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            # TODO: use Django postgresql ORM instead [Important!]
            cursor.execute("""SELECT table_name
                              FROM information_schema.tables
                              WHERE table_schema != 'pg_catalog'
                              AND table_schema != 'information_schema'
                              AND table_type='BASE TABLE'
                              ORDER BY table_name""")
            tables = cursor.fetchall()
            cursor.close()
            return tables
        return None

    def get_status(self):
        return self.is_connected


class MySQLCon(DBConnector):
    def __init__(self, _uri, _name, _username, _password, _port):
        self.conn = None
        self.schema = None
        self.uri = _uri
        self.name = _name
        self.username = _username
        self.password = _password
        self.port = _port
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        print("MySQL connected.")

    def disconnect(self):
        self.is_connected = False
        print("MySQL disconnected.")

    def get_tables(self):
        return self.schema

    def get_status(self):
        return self.is_connected


class SQLServerCon(DBConnector):
    def __init__(self, _uri, _name, _username, _password, _port):
        self.conn = None
        self.schema = None
        self.uri = _uri
        self.name = _name
        self.username = _username
        self.password = _password
        self.port = _port
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        print("SQLServerCon connected.")

    def disconnect(self):
        self.is_connected = False
        print("SQLServerCon disconnected.")

    def get_tables(self):
        return self.schema

    def get_status(self):
        return self.is_connected


class OracleCon(DBConnector):
    def __init__(self, _uri, _name, _username, _password, _port):
        self.conn = None
        self.schema = None
        self.uri = _uri
        self.name = _name
        self.username = _username
        self.password = _password
        self.port = _port
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        print("OracleCon connected.")

    def disconnect(self):
        self.is_connected = False
        print("OracleCon disconnected.")

    def get_tables(self):
        return self.schema

    def get_status(self):
        return self.is_connected


# factory, use this factory if all db settings are same
class DbFactory:

    def __init__(self, _uri, _name, _username, _password, _port):
        self.uri = _uri
        self.name = _name
        self.username = _username
        self.password = _password
        self.port = _port

    def get_connector(self, db_type):
        factory = None
        if db_type == "psql":
            factory = PostgresSQLCon(self.uri, self.name, self.username, self.password, self.port)
        elif db_type == "oracle":
            factory = OracleCon(self.uri, self.name, self.username, self.password, self.port)
        elif db_type == "mysql":
            factory = MySQLCon(self.uri, self.name, self.username, self.password, self.port)
        elif db_type == "sqlserver":
            factory = SQLServerCon(self.uri, self.name, self.username, self.password, self.port)
        else:
            print("ERROR: unknown db type.")
        return factory


if __name__ == "__main__":  # pragma: no cover

    uri = 'localhost'
    name = 'name'
    username = 'username'
    password = 'password'
    port = 5432

    db_factory = DbFactory(uri, name, username, password, port)

    psql_db = db_factory.get_connector('psql')
    psql_db.connect()
    print(psql_db.get_tables())

    # oracle_db = db_factory.get_connector('oracle')
    # oracle_db.connect()
