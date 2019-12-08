from bin.common import AppConfigurations
from bin.common import AppConstants
from bin.exception.exception import BPSupplierException, BPProjectInitializationException
from bin.utils.MongoUtility import MongoUtility


class SupplierHandler(object):
    def __init__(self):
        try:
            self.mongo_db_object = MongoUtility(
                AppConfigurations.MONGO_HOST
            )
        except BPProjectInitializationException:
            raise BPProjectInitializationException("Exception while initializing Project Handler.")

    def create_supplier(self, input_json):
        try:
            print(input_json)
            if AppConstants.SUPPLIER.supplier not in input_json \
                    or (input_json[AppConstants.SUPPLIER.supplier] is None
                        or input_json[AppConstants.SUPPLIER.supplier] == ""):
                print('name not present')
                raise BPSupplierException(AppConstants.SUPPLIER.supplier +
                                          AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.SUPPLIER.contact not in input_json \
                    or (input_json[AppConstants.SUPPLIER.contact] is None
                        or input_json[AppConstants.SUPPLIER.contact] == ""):
                print(AppConstants.SUPPLIER.contact + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPSupplierException(AppConstants.SUPPLIER.contact +
                                          AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            input_json[AppConstants.SUPPLIER.SUPPLIER_ID] = self.mongo_db_object.UUID_generator(
                AppConstants.SUPPLIER.SUPPLIER_ID)
            self.mongo_db_object.insert_one(input_json, AppConfigurations.MONGO_DATABASE,
                                            AppConstants.SUPPLIER.MONGO_SUPPLIER_COLLECTION_NAME)
            return AppConstants.result_success_template("Successfully Created a Supplier")
        except Exception as e:
            print(e)

    def get_suppliers(self):
        """
        This Method is used to Get the Suppliers in Database
        :param input_json:
        :return:
        """
        try:
            output_json = {}
            total_suppliers = list(self.mongo_db_object.find_all(AppConfigurations.MONGO_DATABASE,
                                                                 AppConstants.SUPPLIER.MONGO_SUPPLIER_COLLECTION_NAME))
            output_json = total_suppliers
            return AppConstants.result_success_template(output_json)

        except Exception as e:
            print("Error while fetching the Supplier Data.", str(e))

    def update_supplier(self, input_json):
        """
        This method is used to update the supplier data
        :param input_json: supplier obj,
        :return:
        """
        try:
            if AppConstants.SUPPLIER.SUPPLIER_ID not in input_json \
                    or (input_json[AppConstants.SUPPLIER.SUPPLIER_ID] is None
                        or input_json[AppConstants.SUPPLIER.SUPPLIER_ID] == ""):
                print(AppConstants.SUPPLIER.SUPPLIER_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPSupplierException(AppConstants.SUPPLIER.SUPPLIER_ID +
                                          AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            supplier_data = list(self.mongo_db_object.find_json(
                {AppConstants.SUPPLIER.SUPPLIER_ID: input_json[AppConstants.SUPPLIER.SUPPLIER_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.SUPPLIER.MONGO_SUPPLIER_COLLECTION_NAME))

            if supplier_data:
                try:
                    response = self.mongo_db_object.update_one(
                        {AppConstants.SUPPLIER.SUPPLIER_ID: input_json[AppConstants.SUPPLIER.SUPPLIER_ID]},
                        input_json, AppConfigurations.MONGO_DATABASE,
                        AppConstants.SUPPLIER.MONGO_SUPPLIER_COLLECTION_NAME)
                    print("Successfully updated supplier")
                except Exception as e:
                    print(e, 'exception in updating supplier')
                return AppConstants.result_success_template("successfully updated the supplier data")
            else:
                print("No Supplier found with the specified ID")
                raise BPSupplierException("No Supplier found with the specified ID")
        except Exception as e:
            raise BPSupplierException(e)

    def delete_supplier(self, input_json):
        """
        This method is delete the supplier
        :param input_json: supplier obj,
        :return:
        """
        try:
            if AppConstants.SUPPLIER.SUPPLIER_ID not in input_json \
                    or (input_json[AppConstants.SUPPLIER.SUPPLIER_ID] is None
                        or input_json[AppConstants.SUPPLIER.SUPPLIER_ID] == ""):
                print(AppConstants.SUPPLIER.SUPPLIER_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPSupplierException(AppConstants.SUPPLIER.SUPPLIER_ID +
                                          AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            supplier_data = list(self.mongo_db_object.find_json(
                {AppConstants.SUPPLIER.SUPPLIER_ID: input_json[AppConstants.SUPPLIER.SUPPLIER_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.SUPPLIER.MONGO_SUPPLIER_COLLECTION_NAME))
            print(supplier_data)
            if supplier_data:
                try:
                    response = self.mongo_db_object.remove(supplier_data[0], AppConfigurations.MONGO_DATABASE,
                                                           AppConstants.SUPPLIER.MONGO_SUPPLIER_COLLECTION_NAME)
                    print("Successfully deleted supplier")
                    return AppConstants.result_success_template("successfully updated the supplier data")
                except Exception as e:
                    print(e, 'exception in deleting supplier')
            else:
                print("No Supplier found with the specified ID")
                raise BPSupplierException("No Supplier found with the specified ID")
        except Exception as e:
            raise BPSupplierException(e)
