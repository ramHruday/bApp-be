from bin.common import AppConfigurations
from bin.common import AppConstants
from bin.exception.exception import BPBrandException, BPProjectInitializationException
from bin.utils.MongoUtility import MongoUtility


class BrandHandler(object):
    def __init__(self):
        try:
            self.mongo_db_object = MongoUtility(
                AppConfigurations.MONGO_HOST
            )
        except BPProjectInitializationException:
            raise BPProjectInitializationException("Exception while initializing Project Handler.")

    def create_brand(self, input_json):
        try:
            print(input_json)
            if AppConstants.BRANDS.brand_series not in input_json \
                    or (input_json[AppConstants.BRANDS.brand_series] is None
                        or input_json[AppConstants.BRANDS.brand_series] == ""):
                print('brand name not present')
                raise BPBrandException(AppConstants.BRANDS.brand_series +
                                       AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.BRANDS.brand_name not in input_json \
                    or (input_json[AppConstants.BRANDS.brand_name] is None
                        or input_json[AppConstants.BRANDS.brand_name] == ""):
                print(AppConstants.BRANDS.brand_name + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPBrandException(AppConstants.BRANDS.brand_name +
                                       AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            input_json[AppConstants.BRANDS.BRAND_ID] = self.mongo_db_object.UUID_generator(
                AppConstants.BRANDS.BRAND_ID)
            self.mongo_db_object.insert_one(input_json, AppConfigurations.MONGO_DATABASE,
                                            AppConstants.BRANDS.MONGO_BRAND_COLLECTION_NAME)
            return AppConstants.result_success_template("Successfully Created a Brand")
        except Exception as e:
            print(e)

    def get_brands(self):
        """
        This Method is used to Get the Brands in Database
        :param input_json:
        :return:
        """
        try:
            output_json = {}
            total_brands = list(self.mongo_db_object.find_all(AppConfigurations.MONGO_DATABASE,
                                                              AppConstants.BRANDS.MONGO_BRAND_COLLECTION_NAME))
            output_json = total_brands
            return AppConstants.result_success_template(output_json)

        except Exception as e:
            print("Error while fetching the Brand Data.", str(e))

    def update_brand(self, input_json):
        """
        This method is used to update the brand data
        :param input_json: brand obj,
        :return:
        """
        try:
            if AppConstants.BRANDS.BRAND_ID not in input_json \
                    or (input_json[AppConstants.BRANDS.BRAND_ID] is None
                        or input_json[AppConstants.BRANDS.BRAND_ID] == ""):
                print(AppConstants.BRANDS.BRAND_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPBrandException(AppConstants.BRANDS.BRAND_ID +
                                       AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            brand_data = list(self.mongo_db_object.find_json(
                {AppConstants.BRANDS.BRAND_ID: input_json[AppConstants.BRANDS.BRAND_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.BRANDS.MONGO_BRAND_COLLECTION_NAME))

            if brand_data:
                try:
                    response = self.mongo_db_object.update_one(
                        {AppConstants.BRANDS.BRAND_ID: input_json[AppConstants.BRANDS.BRAND_ID]},
                        input_json, AppConfigurations.MONGO_DATABASE,
                        AppConstants.BRANDS.MONGO_BRAND_COLLECTION_NAME)
                    print("Successfully updated brand")
                except Exception as e:
                    print(e, 'exception in updating brand')
                return AppConstants.result_success_template("successfully updated the brand data")
            else:
                print("No Brand found with the specified ID")
                raise BPBrandException("No Brand found with the specified ID")
        except Exception as e:
            raise BPBrandException(e)

    def delete_brand(self, input_json):
        """
        This method is delete the brand
        :param input_json: brand obj,
        :return:
        """
        try:
            if AppConstants.BRANDS.BRAND_ID not in input_json \
                    or (input_json[AppConstants.BRANDS.BRAND_ID] is None
                        or input_json[AppConstants.BRANDS.BRAND_ID] == ""):
                print(AppConstants.BRANDS.BRAND_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPBrandException(AppConstants.BRANDS.BRAND_ID +
                                       AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            brand_data = list(self.mongo_db_object.find_json(
                {AppConstants.BRANDS.BRAND_ID: input_json[AppConstants.BRANDS.BRAND_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.BRANDS.MONGO_BRAND_COLLECTION_NAME))
            print(brand_data)
            if brand_data:
                try:
                    response = self.mongo_db_object.remove(brand_data[0], AppConfigurations.MONGO_DATABASE,
                                                           AppConstants.BRANDS.MONGO_BRAND_COLLECTION_NAME)
                    print("Successfully deleted brand")
                    return AppConstants.result_success_template("successfully updated the brand data")
                except Exception as e:
                    print(e, 'exception in deleting brand')
            else:
                print("No Brand found with the specified ID")
                raise BPBrandException("No Brand found with the specified ID")
        except Exception as e:
            raise BPBrandException(e)
