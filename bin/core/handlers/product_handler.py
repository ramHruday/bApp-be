from bin.common import AppConfigurations
from bin.common import AppConstants
from bin.exception.exception import BPProductException, BPProjectInitializationException
from bin.utils.MongoUtility import MongoUtility


class ProductHandler(object):
    def __init__(self):
        try:
            self.mongo_db_object = MongoUtility(
                AppConfigurations.MONGO_HOST
            )
        except BPProjectInitializationException:
            raise BPProjectInitializationException("Exception while initializing Project Handler.")

    def create_product(self, input_json):
        try:
            print(input_json)
            if AppConstants.PRODUCT.name not in input_json \
                    or (input_json[AppConstants.PRODUCT.name] is None
                        or input_json[AppConstants.PRODUCT.name] == ""):
                print('name not present')
                raise BPProductException(AppConstants.PRODUCT.name +
                                         AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.PRODUCT.sub_type not in input_json \
                    or (input_json[AppConstants.PRODUCT.sub_type] is None
                        or input_json[AppConstants.PRODUCT.sub_type] == ""):
                print(AppConstants.PRODUCT.sub_type + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPProductException(AppConstants.PRODUCT.sub_type +
                                         AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            input_json[AppConstants.PRODUCT.PRODUCT_ID] = self.mongo_db_object.UUID_generator(
                AppConstants.PRODUCT.PRODUCT_ID)
            self.mongo_db_object.insert_one(input_json, AppConfigurations.MONGO_DATABASE,
                                            AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME)
            return AppConstants.result_success_template("Successfully Created a Product")
        except Exception as e:
            print(e)

    def get_products(self, input_json):
        """
        This Method is used to Get the Products in Database
        :param input_json:
        :return:
        """
        try:
            output_json = {"product": []}
            if AppConstants.PRODUCT.PRODUCT_ID not in input_json or (input_json[AppConstants.PRODUCT.PRODUCT_ID] is None
                                                                     or input_json[
                                                                         AppConstants.PRODUCT.PRODUCT_ID] == ""):
                print("fetching all the Products data from the database")
                total_product_data = self.mongo_db_object.find_all(AppConfigurations.MONGO_DATABASE,
                                                                        AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME)
                print(total_product_data)
                output_json["product"] = total_product_data
                return AppConstants.result_success_template(output_json)
        except Exception as e:
            print("Error while fetching the Product Data.", str(e))

    def update_product(self, input_json):
        """
        This method is used to update the read status of a product
        :param input_json: product Id, Readstatus
        :return:
        """
        try:
            if AppConstants.PRODUCT.PRODUCT_ID not in input_json \
                    or (input_json[AppConstants.PRODUCT.PRODUCT_ID] is None
                        or input_json[AppConstants.PRODUCT.PRODUCT_ID] == ""):
                print(AppConstants.PRODUCT.PRODUCT_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPProductException(AppConstants.PRODUCT.PRODUCT_ID +
                                         AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            print("Searching for product data in the database")
            product_data = self.mongo_db_object.find_json(
                {AppConstants.PRODUCT.PRODUCT_ID: input_json[AppConstants.PRODUCT.PRODUCT_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME)
            if product_data.count():
                for product_obj in product_data:
                    self.mongo_db_object.update_one(
                        {AppConstants.PRODUCT.PRODUCT_ID: input_json[AppConstants.PRODUCT.PRODUCT_ID]},
                        product_obj, AppConfigurations.MONGO_DATABASE,
                        AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME)
                print("Successfully updated nofification")
                return AppConstants.result_success_template("successfully updated the product data")
            else:
                print("No PRODUCT found with the specified ID")
                raise BPProductException("No PRODUCT found with the specified ID")
        except  Exception as e:
            raise BPProductException(e)

    def drop_product(self):
        """
        This method is used to drop product collection
        :return:
        """
        try:
            self.mongo_db_object.drop_collection(AppConfigurations.MONGO_DATABASE,
                                                 AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME)

            return AppConstants.result_success_template("successfully deleted the product data")
        except Exception as e:
            raise BPProductException(e)
