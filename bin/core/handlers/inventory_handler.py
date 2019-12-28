from bin.common import AppConfigurations
from bin.common import AppConstants
from bin.exception.exception import BPInventoryException, BPProjectInitializationException
from bin.utils.MongoUtility import MongoUtility


class InventoryHandler(object):
    def __init__(self):
        try:
            self.mongo_db_object = MongoUtility(
                AppConfigurations.MONGO_HOST
            )
        except BPProjectInitializationException:
            raise BPProjectInitializationException("Exception while initializing Project Handler.")

    def create_inventory(self, input_json):
        try:
            print(input_json)
            if AppConstants.INVENTORY.product_id not in input_json \
                    or (input_json[AppConstants.INVENTORY.product_id] is None
                        or input_json[AppConstants.INVENTORY.product_id] == ""):
                raise BPInventoryException(AppConstants.INVENTORY.product_id +
                                           AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.INVENTORY.supplier_id not in input_json \
                    or (input_json[AppConstants.INVENTORY.supplier_id] is None
                        or input_json[AppConstants.INVENTORY.supplier_id] == ""):
                raise BPInventoryException(AppConstants.INVENTORY.supplier_id +
                                           AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.INVENTORY.brand_id not in input_json \
                    or (input_json[AppConstants.INVENTORY.brand_id] is None
                        or input_json[AppConstants.INVENTORY.brand_id] == ""):
                print(AppConstants.INVENTORY.brand_id + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPInventoryException(AppConstants.INVENTORY.brand_id +
                                           AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.INVENTORY.location_id not in input_json \
                    or (input_json[AppConstants.INVENTORY.location_id] is None
                        or input_json[AppConstants.INVENTORY.location_id] == ""):
                print(AppConstants.INVENTORY.location_id + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPInventoryException(AppConstants.INVENTORY.location_id +
                                           AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.INVENTORY.kmi not in input_json \
                    or (input_json[AppConstants.INVENTORY.kmi] is None
                        or input_json[AppConstants.INVENTORY.kmi] == ""):
                print(AppConstants.INVENTORY.kmi + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPInventoryException(AppConstants.INVENTORY.kmi +
                                           AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.INVENTORY.quantity not in input_json \
                    or (input_json[AppConstants.INVENTORY.quantity] is None
                        or input_json[AppConstants.INVENTORY.quantity] == ""):
                print(AppConstants.INVENTORY.quantity + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPInventoryException(AppConstants.INVENTORY.quantity +
                                           AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.INVENTORY.mrp not in input_json \
                    or (input_json[AppConstants.INVENTORY.mrp] is None
                        or input_json[AppConstants.INVENTORY.mrp] == ""):
                print(AppConstants.INVENTORY.mrp + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPInventoryException(AppConstants.INVENTORY.mrp +
                                           AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            input_json[AppConstants.INVENTORY.INVENTORY_ID] = self.mongo_db_object.UUID_generator(
                AppConstants.INVENTORY.INVENTORY_ID)
            self.mongo_db_object.insert_one(input_json, AppConfigurations.MONGO_DATABASE,
                                            AppConstants.INVENTORY.MONGO_INVENTORY_COLLECTION_NAME)
            return AppConstants.result_success_template("Successfully Created a Inventory item")
        except Exception as e:
            print(e)

    def get_inventory(self):
        """
        This Method is used to Get the Inventorys in Database
        :param input_json:
        :return:
        """
        try:
            output_json = {}
            total_inventory = list(self.mongo_db_object.find_all(AppConfigurations.MONGO_DATABASE,
                                                                 AppConstants.INVENTORY.MONGO_INVENTORY_COLLECTION_NAME))
            output_json = total_inventory
            return AppConstants.result_success_template(output_json)

        except Exception as e:
            print("Error while fetching the Inventory Data.", str(e))

    def update_inventory(self, input_json):
        """
        This method is used to update the inventory data
        :param input_json: inventory obj,
        :return:
        """
        try:
            if AppConstants.INVENTORY.INVENTORY_ID not in input_json \
                    or (input_json[AppConstants.INVENTORY.INVENTORY_ID] is None
                        or input_json[AppConstants.INVENTORY.INVENTORY_ID] == ""):
                print(AppConstants.INVENTORY.INVENTORY_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPInventoryException(AppConstants.INVENTORY.INVENTORY_ID +
                                           AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            inventory_data = list(self.mongo_db_object.find_json(
                {AppConstants.INVENTORY.INVENTORY_ID: input_json[AppConstants.INVENTORY.INVENTORY_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.INVENTORY.MONGO_INVENTORY_COLLECTION_NAME))

            if inventory_data:
                try:
                    response = self.mongo_db_object.update_one(
                        {AppConstants.INVENTORY.INVENTORY_ID: input_json[AppConstants.INVENTORY.INVENTORY_ID]},
                        input_json, AppConfigurations.MONGO_DATABASE,
                        AppConstants.INVENTORY.MONGO_INVENTORY_COLLECTION_NAME)
                    print("Successfully updated inventory")
                except Exception as e:
                    print(e, 'exception in updating inventory')
                return AppConstants.result_success_template("successfully updated the inventory data")
            else:
                print("No Inventory found with the specified ID")
                raise BPInventoryException("No Inventory found with the specified ID")
        except Exception as e:
            raise BPInventoryException(e)

    def delete_inventory(self, input_json):
        """
        This method is delete the inventory
        :param input_json: inventory obj,
        :return:
        """
        try:
            if AppConstants.INVENTORY.INVENTORY_ID not in input_json \
                    or (input_json[AppConstants.INVENTORY.INVENTORY_ID] is None
                        or input_json[AppConstants.INVENTORY.INVENTORY_ID] == ""):
                print(AppConstants.INVENTORY.INVENTORY_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPInventoryException(AppConstants.INVENTORY.INVENTORY_ID +
                                           AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            inventory_data = list(self.mongo_db_object.find_json(
                {AppConstants.INVENTORY.INVENTORY_ID: input_json[AppConstants.INVENTORY.INVENTORY_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.INVENTORY.MONGO_INVENTORY_COLLECTION_NAME))
            print(inventory_data)
            if inventory_data:
                try:
                    response = self.mongo_db_object.remove(inventory_data[0], AppConfigurations.MONGO_DATABASE,
                                                           AppConstants.INVENTORY.MONGO_INVENTORY_COLLECTION_NAME)
                    print("Successfully deleted inventory")
                    return AppConstants.result_success_template("successfully updated the inventory data")
                except Exception as e:
                    print(e, 'exception in deleting inventory')
            else:
                print("No Inventory found with the specified ID")
                raise BPInventoryException("No Inventory found with the specified ID")
        except Exception as e:
            raise BPInventoryException(e)
