import mysql.connector
class UseDatabase:

    def __init__(self,config: dict)->None:
        self.configuration=config

    def __enter__(self)->'cursor':
        self.conn=mysql.connector.connect(**self.configuration)
        self.cursor=self.conn.cursor()
        return self.cursor

    def __exit__(self,exc_type,exc_value,exc_trace)->None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        
     def __pop__(self)->:
        self.conn=mysql.connector.connect(**self.configuration)
        self.next=self.conn.data()
        return self.data

