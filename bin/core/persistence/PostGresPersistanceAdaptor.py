from bin.utils.PostGresUtility import PostgresUtility
from datetime import datetime

# Logger
# logger = Logging.get_logger()

output = {
    "status": False,
    "data": []
}

header_content = [
    {
        "key": "employee_name",
        "label": "Name"
    },
    {
        "key": "from_date",
        "label": "From"
    },
    {
        "key": "to_date",
        "label": "To"
    },
    {
        "key": "leave_type",
        "label": "Type"
    },
    {
        "key": "reason",
        "label": "Reason"
    }
]


class PostgresQueries(object):

    @staticmethod
    def create_table_leave():
        try:
            a = PostgresUtility()
            create_table_command = "CREATE TABLE LEAVES_CUSTOM_APPS(id serial PRIMARY KEY," \
                                   "employee_name VARCHAR (50) NOT NULL," \
                                   "employee_id VARCHAR (50) NOT NULL," \
                                   "employee_role VARCHAR (50)," \
                                   "leave_type VARCHAR NOT NULL," \
                                   "from_date TIMESTAMP NOT NULL," \
                                   "to_date TIMESTAMP NOT NULL," \
                                   "applied_on TIMESTAMP NOT NULL," \
                                   "reason VARCHAR (200)," \
                                   "status VARCHAR (50))"
            print(create_table_command)
            a.create_table(create_table_command=create_table_command)
        except Exception as e:
            # logger.error(str(e))
            raise Exception(str(e))

    @staticmethod
    def insert_leave_leaves_custom_apps(leave_item):
        try:
            # PostgresUtility()
            table_name = 'LEAVES_CUSTOM_APPS'
            leave_item['status'] = 'in-progress'
            header_keys = ('employee_name', 'employee_id', 'employee_role', 'leave_type', 'from_date', 'to_date',
                           'applied_on', 'reason', 'status')
            body_string = ''
            for header in header_keys:
                if header_keys.index(header) < len(header_keys) - 1:
                    body_string += "'" + leave_item[header] + "',"
                else:
                    body_string += "'" + leave_item[header] + "'"
            insert_command = "INSERT INTO " + table_name + "(" + ",".join(header_keys) + ") VALUES(" + body_string + ")"
            PostgresUtility().insert_new_record(insert_command=insert_command)
            # logger.info('created table leaves')
            output['status'] = True
            return output
        except Exception as e:
            # logger.error(str(e))
            raise Exception(str(e))
            return output

    @staticmethod
    def edit_leave_leaves_custom_apps(leave_item):
        try:
            print(leave_item)
        except Exception as e:
            # logger.error(str(e))
            raise Exception(str(e))

    @staticmethod
    def delete_leave_leaves_custom_apps(leave_item):
        try:
            print(leave_item)
        except Exception as e:
            # logger.error(str(e))
            raise Exception(str(e))

    @staticmethod
    def get_all_leaves_custom_apps():
        output['data'] = {}
        output['data']['bodyContent'] = []
        output['data']['headerContent'] = header_content
        try:
            header_keys = [
                'id',
                'employee_name',
                'employee_id',
                'role',
                "leave_type",
                "from_date",
                "to_date",
                'applied_on',
                "reason",
                "status"
            ]
            fetch_all_command = "SELECT * FROM LEAVES_CUSTOM_APPS"
            body_content = PostgresUtility().query_all(fetch_all_command=fetch_all_command)
            for row in body_content:
                obj = {}
                for i, content in enumerate(row):
                    if header_keys[i] == 'from_date' or header_keys[i] == 'to_date' or header_keys[i] == 'applied_on':
                        obj[header_keys[i]] = str(content)
                    else:
                        obj[header_keys[i]] = content

                output['data']['bodyContent'].append(obj)
            # logger.info('created table leaves')
            print(output['data'])
            output['status'] = True
            return output
        except Exception as e:
            # logger.error(str(e))
            raise Exception(str(e))

    @staticmethod
    def delete_leave_custom_leaves():
        try:
            drop_table_command = "DROP TABLE LEAVES_CUSTOM_APPS"
            PostgresUtility().drop_table(drop_table_command)
        except Exception as e:
            # logger.error(str(e))
            raise Exception(str(e))

    @staticmethod
    def get_emp_teams_by_id(id_value):
        try:
            result = PostgresUtility().get_item_by_id('emp_map_team', 'emp_id', id_value)
            output['data'] = []
            for index, team in enumerate(result[1]):
                output['data'].append(team['id'])
            print(output["data"])
            output['status'] = True
            return output
        except Exception as e:
            raise Exception(str(e))

    @staticmethod
    def get_employees_details():
        try:
            fetch_all_command = "SELECT * FROM emp_details"
            result = PostgresUtility().query_all(fetch_all_command=fetch_all_command)
            print(result)
            output["data"] = []
            for index, value in enumerate(result):
                obj = {'id': value[1], 'label': value[0], 'role': value[2]}
                output['data'].append(obj)
            output['status'] = True
            return output
        except Exception as e:
            raise Exception(str(e))

    @staticmethod
    def get_teams_details():
        try:
            fetch_all_command = "SELECT * FROM zs_ca_teams"
            result = PostgresUtility().query_all(fetch_all_command=fetch_all_command)
            print(result)
            output["data"] = []
            for index, value in enumerate(result):
                obj = {'id': value[0], 'label': value[1]}
                output['data'].append(obj)
            output['status'] = True
            return output
        except Exception as e:
            raise Exception(str(e))

# if __name__ == '__main__':
# PostgresQueries().create_table_leave()
# PostgresQueries().insert_leave_leaves_custom_apps(
#     {'employee_name': 'y1', 'employee_id': '12345', 'employee_role': 'role',
#      'leave_type': 'leave_type89',
#      'from_date': '1999-01-08', 'to_date': '1999-01-08', 'applied_on': '1999-01-08'})
# PostgresQueries().delete_leave_custom_leaves()
