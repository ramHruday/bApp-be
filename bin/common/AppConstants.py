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


class PROJECT(object):
    # success msgs

    # error msgs
    NOT_PRESENT_ERROR_MSG = ":key not present in input payload!"
    # APIs


class PRODUCT(object):
    # Mongo Collection Info
    MONGO_PRODUCT_COLLECTION_NAME = "products"
    # Notification JSON Key
    name = "name"
    sub_type = "subType"
    PRODUCT_ID = "product_id"
    CREATED_TIME = "CreatedTime"
    # APIs
    api_get_products = AppConfigurations.api_service_url + "/getProducts"
    api_update_product = AppConfigurations.api_service_url + "/updateProduct"
    api_create_product = AppConfigurations.api_service_url + "/createProduct"
    api_drop_product = AppConfigurations.api_service_url + "/deleteProduct"


class SUPPLIER(object):
    # Mongo Collection Info
    MONGO_SUPPLIER_COLLECTION_NAME = "suppliers"
    # Notification JSON Key
    supplier = "supplier"
    contact = "contact"
    SUPPLIER_ID = "supplier_id"
    CREATED_TIME = "CreatedTime"
    # APIs
    api_get_suppliers = AppConfigurations.api_service_url + "/getSuppliers"
    api_update_supplier = AppConfigurations.api_service_url + "/updateSupplier"
    api_create_supplier = AppConfigurations.api_service_url + "/createSupplier"
    api_drop_supplier = AppConfigurations.api_service_url + "/deleteSupplier"


class LOCATION(object):
    # Mongo Collection Info
    MONGO_LOCATION_COLLECTION_NAME = "locations"
    # Notification JSON Key
    location = "location_name"
    address = "address"
    LOCATION_ID = "location_id"
    CREATED_TIME = "CreatedTime"
    # APIs
    api_get_locations = AppConfigurations.api_service_url + "/getLocations"
    api_update_location = AppConfigurations.api_service_url + "/updateLocation"
    api_create_location = AppConfigurations.api_service_url + "/createLocation"
    api_drop_location = AppConfigurations.api_service_url + "/deleteLocation"


class BRANDS(object):
    # Mongo Collection Info
    MONGO_BRAND_COLLECTION_NAME = "brands"
    # Notification JSON Key
    brand_series = "brand_series"
    brand_name = "brand_name"
    brand_rep = "brand_rep"
    brand_contact = "brand_contact"
    BRAND_ID = "brand_id"
    CREATED_TIME = "CreatedTime"
    # APIs
    api_get_brands = AppConfigurations.api_service_url + "/getBrands"
    api_update_brand = AppConfigurations.api_service_url + "/updateBrand"
    api_create_brand = AppConfigurations.api_service_url + "/createBrand"
    api_drop_brand = AppConfigurations.api_service_url + "/deleteBrand"


class INVENTORY(object):
    # Mongo Collection Info
    MONGO_INVENTORY_COLLECTION_NAME = "inventory"
    # Notification JSON Key
    product_id = "product_id"
    supplier_id = "supplier_id"
    location_id = "location_id"
    brand_id = "brand_id"
    created_at = "created_at"
    updated_at = "updated_at"
    updated_by = "updated_by"
    created_by = "created_by"
    kmi = "kmi"
    quantity = "quantity"
    mrp = "mrp"
    INVENTORY_ID = "inventory_id"
    # APIs
    api_get_inventory = AppConfigurations.api_service_url + "/getInventory"
    api_update_inventory = AppConfigurations.api_service_url + "/updateInventory"
    api_create_inventory = AppConfigurations.api_service_url + "/createInventory"
    api_drop_inventory = AppConfigurations.api_service_url + "/deleteInventory"


class Login(object):
    USER_NAME = "userName"
    PASSWORD = "password"
    login_key = "login_json"

    # APIsapi_service_url
    api_user_login = AppConfigurations.api_service_url + "/userLogin"
    api_project_details = AppConfigurations.api_service_url + "/projectDetails"
    login_conf_path = "conf/login_Conf.json"
    metadata_conf_path = "conf/metadata_conf.json"

    # Mongo
    MONGO_USER_DETAILS = "access_control_details"


class MongoConstants(object):
    # initializing status constants
    uid_collection_name = "unique_keys"
    unique_id_key = "unique_id"
    doc_type_key = "doc_type"
    success_key = "success"
    failure_key = "failed"
    status_key = "status"
    result_key = "Result: "
    error_key = "error: "

    # status keys
    success_status = {status_key: success_key, result_key: ""}
    failed_status = {status_key: failure_key, error_key: ""}
