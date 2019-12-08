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
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = productHandle.update_product(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@product.route(AppConstants.PRODUCT.api_drop_product, methods=[AppConstants.POST])
def delete_product_function():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = productHandle.delete_product(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@product.route(AppConstants.PRODUCT.api_get_products, methods=[AppConstants.GET])
def fetch_all_products():
    if request.method == 'GET':
        try:
            product_data = productHandle.get_products()
            response = product_data
            return json.dumps(response, default=str)
        except Exception as e:
            print(e, ': error while fetching from product service')
            return str(e)
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))
