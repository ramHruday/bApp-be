import json

from flask import request, Blueprint

from flask import request

import uuid
import json

from bin.common import AppConstants
from bin.core.handlers.inventory_handler import InventoryHandler

output_json = {
    "status": False, "message": "error"
}
inventoryHandle = InventoryHandler()

# ---------------------------------- Flask Blueprint --------------------------------------------------

inventory = Blueprint("inventory", __name__)


# --------------------------------------- Configuration ------------------------------------------------


@inventory.route(AppConstants.INVENTORY.api_create_inventory, methods=[AppConstants.POST])
def create_inventory():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = inventoryHandle.create_inventory(input_data)
            print(response)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@inventory.route(AppConstants.INVENTORY.api_update_inventory, methods=[AppConstants.POST])
def update_inventory_function():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = inventoryHandle.update_inventory(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@inventory.route(AppConstants.INVENTORY.api_drop_inventory, methods=[AppConstants.POST])
def delete_inventory_function():
    if request.method == 'POST':
        try:
            input_data = json.loads(request.get_data())
            response = inventoryHandle.delete_inventory(input_data)
            return json.dumps(response)
        except Exception as e:
            return json.dumps(AppConstants.result_error_template(str(e)))
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))


@inventory.route(AppConstants.INVENTORY.api_get_inventory, methods=[AppConstants.GET])
def fetch_all_inventorys():
    if request.method == 'GET':
        try:
            inventory_data = inventoryHandle.get_inventory()
            response = inventory_data
            return json.dumps(response, default=str)
        except Exception as e:
            print(e, ': error while fetching from inventory service')
            return str(e)
    else:
        return json.dumps(AppConstants.result_error_template(AppConstants.method_not_supported))
