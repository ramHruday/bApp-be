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

    def get_products(self):
        """
        This Method is used to Get the Products in Database
        :param input_json:
        :return:
        """
        try:
            output_json = {}
            total_product_data = list(self.mongo_db_object.find_all(AppConfigurations.MONGO_DATABASE,
                                                                    AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME))
            output_json = total_product_data
            return AppConstants.result_success_template(output_json)

        except Exception as e:
            print("Error while fetching the Product Data.", str(e))

    def update_product(self, input_json):
        """
        This method is used to update the product data
        :param input_json: product obj,
        :return:
        """
        try:
            if AppConstants.PRODUCT.PRODUCT_ID not in input_json \
                    or (input_json[AppConstants.PRODUCT.PRODUCT_ID] is None
                        or input_json[AppConstants.PRODUCT.PRODUCT_ID] == ""):
                print(AppConstants.PRODUCT.PRODUCT_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPProductException(AppConstants.PRODUCT.PRODUCT_ID +
                                         AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            product_data = list(self.mongo_db_object.find_json(
                {AppConstants.PRODUCT.PRODUCT_ID: input_json[AppConstants.PRODUCT.PRODUCT_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME))

            if product_data:
                try:
                    response = self.mongo_db_object.update_one(
                        {AppConstants.PRODUCT.PRODUCT_ID: input_json[AppConstants.PRODUCT.PRODUCT_ID]},
                        input_json, AppConfigurations.MONGO_DATABASE,
                        AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME)
                    print("Successfully updated product")
                except Exception as e:
                    print(e, 'exception in updating product')
                return AppConstants.result_success_template("successfully updated the product data")
            else:
                print("No PRODUCT found with the specified ID")
                raise BPProductException("No PRODUCT found with the specified ID")
        except Exception as e:
            raise BPProductException(e)

    def delete_product(self, input_json):
        """
        This method is delete the product
        :param input_json: product obj,
        :return:
        """
        try:
            if AppConstants.PRODUCT.PRODUCT_ID not in input_json \
                    or (input_json[AppConstants.PRODUCT.PRODUCT_ID] is None
                        or input_json[AppConstants.PRODUCT.PRODUCT_ID] == ""):
                print(AppConstants.PRODUCT.PRODUCT_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPProductException(AppConstants.PRODUCT.PRODUCT_ID +
                                         AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            product_data = list(self.mongo_db_object.find_json(
                {AppConstants.PRODUCT.PRODUCT_ID: input_json[AppConstants.PRODUCT.PRODUCT_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME))
            print(product_data)
            if product_data:
                try:
                    response = self.mongo_db_object.remove(product_data[0], AppConfigurations.MONGO_DATABASE,
                                                           AppConstants.PRODUCT.MONGO_PRODUCT_COLLECTION_NAME)
                    print("Successfully deleted product")
                    return AppConstants.result_success_template("successfully updated the product data")
                except Exception as e:
                    print(e, 'exception in deleting product')
            else:
                print("No PRODUCT found with the specified ID")
                raise BPProductException("No PRODUCT found with the specified ID")
        except Exception as e:
            raise BPProductException(e)


