import json

from flask import request, Blueprint

from flask import request

import uuid
import json

from bin.common import AppConstants
from bin.core.handlers.location_handler import LocationHandler

output_json = {
    "status": False, "message": "error"
}
locationHandle = LocationHandler()

# ---------------------------------- Flask Blueprint --------------------------------------------------

location = Blueprint("location", __name__)


# --------------------------------------- Configuration ------------------------------------------------


@location.route(AppConstants.LOCATION.api_create_location, methods=[AppConstants.POST])
def create_location():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = locationHandle.create_location(input_data)
            print(response)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@location.route(AppConstants.LOCATION.api_update_location, methods=[AppConstants.POST])
def update_location_function():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = locationHandle.update_location(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@location.route(AppConstants.LOCATION.api_drop_location, methods=[AppConstants.POST])
def delete_location_function():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = locationHandle.delete_location(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@location.route(AppConstants.LOCATION.api_get_locations, methods=[AppConstants.GET])
def fetch_all_locations():
    if request.method == 'GET':
        try:
            location_data = locationHandle.get_locations()
            response = location_data
            return json.dumps(response, default=str)
        except Exception as e:
            print(e, ': error while fetching from location service')
            return str(e)
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))
