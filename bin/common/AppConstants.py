# Response keys
success_key = "success"
failure_key = "failed"
import os
import __root__
from bin.common import AppConfigurations

CONFIGURATION_FILE = os.path.join(__root__.path(), "conf\\application.conf")

# Methods
GET = "GET"
POST = "POST"

# Error message constants
method_not_supported = "Method not supported!"
NOT_PRESENT_ERROR_MSG = " not present in input json"
exception_message = '{"status":True, "status_message":"Server error, please contact your administrator"}'
method_error_message = '{"status": True, "message": "Method not supported!"}'
success_status = {"status": "success", "result": "Data received successfully"}


def result_success_template(data, status="success"):
    return {
        "status": status,
        "result": data
    }


def result_error_template(message=None, error_type="application"):
    if message:
        return {
            "status": "error",
            "type": error_type,
            "result": message
        }
    else:
        return {
            "status": "error",
            "type": error_type,
            "result": "Error while processing the request"
        }


def result_exist_template(message=None, error_type="version_exist"):
    if message:
        return {
            "status": "error",
            "type": error_type,
            "result": message
        }
    else:
        return {
            "status": "error",
            "type": error_type,
            "result": "Error while processing the request"
        }


class Notification(object):
    # Mongo Collection Info
    MONGO_PRODUCT_COLLECTION_NAME = "products"
    # Notification JSON Key
    name = "name"
    sub_type = "subType"
    CREATED_TIME = "CreatedTime"
    # APIs
    api_get_products = AppConfigurations.api_service_url + "/getProducts"
    api_update_product = AppConfigurations.api_service_url + "/updateProduct"
    api_create_product = AppConfigurations.api_service_url + "/createProduct"
    api_drop_product = AppConfigurations.api_service_url + "/dropProduct"


class Login(object):
    USER_NAME = "userName"
    PASSWORD = "password"
    login_key = "login_json"

    # APIsapi_service_url
    api_user_login = AppConfigurations.api_service_url + "/userLogin"
    api_project_details = AppConfigurations.api_service_url + "/projectDetails"
    login_conf_path = "conf/login_Conf.json"
    metadata_conf_path = "conf/metadata_conf.json"

    #Mongo
    MONGO_USER_DETAILS = "access_control_details"

