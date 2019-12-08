import json

from flask import request, Blueprint

from flask import request

import uuid
import json

from bin.common import AppConstants
from bin.core.handlers.supplier_handler import SupplierHandler

output_json = {
    "status": False, "message": "error"
}
supplierHandle = SupplierHandler()

# ---------------------------------- Flask Blueprint --------------------------------------------------

supplier = Blueprint("supplier", __name__)


# --------------------------------------- Configuration ------------------------------------------------


@supplier.route(AppConstants.SUPPLIER.api_create_supplier, methods=[AppConstants.POST])
def create_supplier():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = supplierHandle.create_supplier(input_data)
            print(response)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@supplier.route(AppConstants.SUPPLIER.api_update_supplier, methods=[AppConstants.POST])
def update_supplier_function():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = supplierHandle.update_supplier(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@supplier.route(AppConstants.SUPPLIER.api_drop_supplier, methods=[AppConstants.POST])
def delete_supplier_function():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = supplierHandle.delete_supplier(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@supplier.route(AppConstants.SUPPLIER.api_get_suppliers, methods=[AppConstants.GET])
def fetch_all_suppliers():
    if request.method == 'GET':
        try:
            supplier_data = supplierHandle.get_suppliers()
            response = supplier_data
            return json.dumps(response, default=str)
        except Exception as e:
            print(e, ': error while fetching from supplier service')
            return str(e)
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))
