from flask import Flask
from flask import request
from flask_cors import CORS


import uuid
import json

app = Flask(__name__)

output_json = {
    "status": False, "message": "error"
}

CORS(app)


@app.route("/addProduct", methods=['POST'])
def register_function():
    try:
        if request.method == 'POST':
            if request.is_json:
                input_data = request.get_json()
                result = [{}]
                print(result)
                if result['status']:
                    output_json['status'] = True
                    output_json['message'] = "Product added."
            else:
                output_json['status'] = False
                output_json['message'] = "error within the input data/ input not a json"
        return output_json
    except Exception as e:
        output_json['status'] = False
        output_json['data'] = None
        output_json['message'] = str(e)
        return output_json


@app.route("/updateLeave", methods=['POST'])
def update_leave_function():
    try:
        if request.method == 'POST':
            if request.is_json:
                input_data = request.get_json()
                result = [{}]
                print(result)
                if result['status']:
                    output_json['status'] = True
                    output_json['message'] = "Leave added."
            else:
                output_json['status'] = False
                output_json['message'] = "error within the input data/ input not a json"
        return output_json
    except Exception as e:
        output_json['status'] = False
        output_json['data'] = None
        output_json['message'] = str(e)
        return output_json


@app.route("/deleteProduct", methods=['POST'])
def disapprove_leave_function():
    try:
        if request.method == 'POST':
            if request.is_json:
                input_data = request.get_json()
                result = [{}]
                print(result)
                if result['status']:
                    output_json['status'] = True
                    output_json['message'] = "Leave added."
            else:
                output_json['status'] = False
                output_json['message'] = "error within the input data/ input not a json"
        return output_json
    except Exception as e:
        output_json['status'] = False
        output_json['data'] = None
        output_json['message'] = str(e)
        return output_json


@app.route("/fetchLeaves", methods=['POST'])
def fetch_leaves_all_function():
    try:
        if request.method == 'POST':
            result = [{}]
            if result['status']:
                output_json["status"] = True
                output_json["message"] = "Success"
        return json.dumps(output_json)
    except Exception as e:
        output_json['status'] = False
        output_json['data'] = None
        output_json['message'] = str(e)
        return output_json


@app.route("/getEmpTeams", methods=['POST'])
def get_emp_related_role_team():
    try:
        if request.method == 'POST':
            input_data = request.get_json()
            result = [{}]
            if result['status']:
                output_json["status"] = True
                output_json["message"] = "Success"
        return json.dumps(output_json)
    except Exception as e:
        output_json['status'] = False
        output_json['data'] = None
        output_json['message'] = str(e)
        return output_json


@app.route("/getEmployees", methods=['POST'])
def get_employees():
    try:
        if request.method == 'POST':
            result = [{}]
            if result['status']:
                output_json["status"] = True
                output_json["message"] = "Success"
        return json.dumps(output_json)
    except Exception as e:
        output_json['status'] = False
        output_json['data'] = None
        output_json['message'] = str(e)
        return output_json


@app.route("/getTeamList", methods=['POST'])
def get_teams():
    try:
        if request.method == 'POST':
            result = [{}]
            if result['status']:
                output_json["status"] = True
                output_json["message"] = "Success"
        return json.dumps(output_json)
    except Exception as e:
        output_json['status'] = False
        output_json['data'] = None
        output_json['message'] = str(e)
        return output_json


def create_product_id():
    """
    This function will create a schedulerid
    :return: return JSON object with scheduler Id.
    """
    try:
        product_id = '{0}{1}'.format('product_', generate_uuid())
        return product_id
    except Exception:
        message = "Creating query id failed"
        raise Exception(message)


def generate_uuid():
    """
    :return: 5 digit UUID
    """
    uuid_temp = uuid.uuid4()
    return str(uuid_temp)[:5]


if __name__ == '__main__':
    app.run(port=8080)
