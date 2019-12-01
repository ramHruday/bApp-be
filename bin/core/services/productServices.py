import json

from flask import request, Blueprint

from flask import request

import uuid
import json

from bin.common import AppConstants
from bin.core.handlers.product_handler import ProductHandler

output_json = {
    "status": False, "message": "error"
}
productHandle = ProductHandler()

# ---------------------------------- Flask Blueprint --------------------------------------------------

product = Blueprint("product", __name__)


# --------------------------------------- Configuration ------------------------------------------------


@product.route(AppConstants.PRODUCT.api_create_product, methods=[AppConstants.POST])
def create_product():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = productHandle.create_product(input_data)
            print(response)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@product.route(AppConstants.PRODUCT.api_update_product, methods=[AppConstants.POST])
def update_product_function():
    try:
        if request.method == 'POST':
            if request.is_json:
                input_data = json.loads(request.get_data())
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


@product.route(AppConstants.PRODUCT.api_drop_product, methods=[AppConstants.POST])
def delete_product_function():
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


@product.route(AppConstants.PRODUCT.api_get_products, methods=[AppConstants.GET])
def fetch_all_products():
    if request.method == 'GET':
        try:
            output_json = []
            print(request)
            output_json["data"] = productHandle.get_products()
            return json.dumps(output_json)
        except Exception as e:
            output_json['status'] = False
            output_json['data'] = None
            output_json['message'] = str(e)
            return output_json
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))
