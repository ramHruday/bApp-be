"""Postgres Utility"""

import psycopg2

from bin.common import AppConfigurations


class PostgresUtility:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(host=AppConfigurations.DATABASE_HOST,
                                               port=AppConfigurations.DATABASE_PORT,
                                               dbname=AppConfigurations.DATABASE_NAME,
                                               user=AppConfigurations.DATABASE_USER,
                                               password=AppConfigurations.DATABASE_PASSWORD)
            self.connection.autocommit = True
            print('connected to db')
            self.cursor = self.connection.cursor()
        except Exception as e:
            raise e

    def create_table(self, create_table_command):
        # create_table_command = "CREATE TABLE pet(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL)"
        print(create_table_command)
        self.cursor.execute(create_table_command)

    def insert_new_record(self, insert_command):
        try:
            # new_record = ("cat1", "12")
            # insert_command = "INSERT INTO pet(name, age) VALUES('" + new_record[0] + " ',' " + new_record[1] + ")"
            self.cursor.execute(insert_command)
        except Exception as e:
            raise e

    def query_all(self, fetch_all_command):
        try:
                # fetch_all_command = "SELECT * FROM pet"
            print(fetch_all_command)
            self.cursor.execute(fetch_all_command)
            # print(self.cursor.fetchall())
            leaves = self.cursor.fetchall()
            print(leaves)
            return leaves
        except Exception as e:
            raise e

    def update_record(self):
        update_command = "UPDATE pet SET age=10 where id=1"
        self.cursor.execute(update_command)

    def drop_table(self, drop_table_command):
        # drop_table_command = "DROP TABLE pet"
        self.cursor.execute(drop_table_command)

    def insert_team_map(self):
        insert_command = "INSERT INTO emp_map_team (emp_id,team) VALUES  ( 'sa12345','[{'label': 'CCM_MDP', " \
                         "'role':'lead'},{'label': 'Allergen', 'role':'dev'}]')"
        self.cursor.execute(insert_command)

    def get_item_by_id(self, table_name, column, value):
        query_command = "SELECT * FROM " + table_name + " WHERE " + column + " = '" + value + "';"
        self.cursor.execute(query_command)
        row_item = self.cursor.fetchall()
        # print(row_item)
        return row_item[0]

    def get_by_column_name(self, table_name, column):
        query_command = "SELECT "+column+" FROM " + table_name + ";"
        print(query_command)
        self.cursor.execute(query_command)
        result = self.cursor.fetchall()
        print(result)
        return result

    # if __name__ == '__main__':
#     database_connection = PostgresUtility()
# database_connection.create_table()
# database_connection.insert_new_record()
# database_connection.update_record()
# database_connection.drop_table()
