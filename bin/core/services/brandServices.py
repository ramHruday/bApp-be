import json

from flask import request, Blueprint

from flask import request

import uuid
import json

from bin.common import AppConstants
from bin.core.handlers.brand_handler import BrandHandler

output_json = {
    "status": False, "message": "error"
}
brandHandle = BrandHandler()

# ---------------------------------- Flask Blueprint --------------------------------------------------

brand = Blueprint("brand", __name__)


# --------------------------------------- Configuration ------------------------------------------------


@brand.route(AppConstants.BRANDS.api_create_brand, methods=[AppConstants.POST])
def create_brand():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = brandHandle.create_brand(input_data)
            print(response)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@brand.route(AppConstants.BRANDS.api_update_brand, methods=[AppConstants.POST])
def update_brand_function():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = brandHandle.update_brand(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@brand.route(AppConstants.BRANDS.api_drop_brand, methods=[AppConstants.POST])
def delete_brand_function():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = brandHandle.delete_brand(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@brand.route(AppConstants.BRANDS.api_get_brands, methods=[AppConstants.GET])
def fetch_all_brands():
    if request.method == 'GET':
        try:
            brand_data = brandHandle.get_brands()
            response = brand_data
            return json.dumps(response, default=str)
        except Exception as e:
            print(e, ': error while fetching from brand service')
            return str(e)
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))
