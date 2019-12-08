from bin.common import AppConfigurations
from bin.common import AppConstants
from bin.exception.exception import BPLocationException, BPProjectInitializationException
from bin.utils.MongoUtility import MongoUtility


class LocationHandler(object):
    def __init__(self):
        try:
            self.mongo_db_object = MongoUtility(
                AppConfigurations.MONGO_HOST
            )
        except BPProjectInitializationException:
            raise BPProjectInitializationException("Exception while initializing Project Handler.")

    def create_location(self, input_json):
        try:
            print(input_json)
            if AppConstants.LOCATION.location not in input_json \
                    or (input_json[AppConstants.LOCATION.location] is None
                        or input_json[AppConstants.LOCATION.location] == ""):
                print('location name not present')
                raise BPLocationException(AppConstants.LOCATION.location +
                                          AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            if AppConstants.LOCATION.address not in input_json \
                    or (input_json[AppConstants.LOCATION.address] is None
                        or input_json[AppConstants.LOCATION.address] == ""):
                print(AppConstants.LOCATION.address + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPLocationException(AppConstants.LOCATION.address +
                                          AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
            input_json[AppConstants.LOCATION.LOCATION_ID] = self.mongo_db_object.UUID_generator(
                AppConstants.LOCATION.LOCATION_ID)
            self.mongo_db_object.insert_one(input_json, AppConfigurations.MONGO_DATABASE,
                                            AppConstants.LOCATION.MONGO_LOCATION_COLLECTION_NAME)
            return AppConstants.result_success_template("Successfully Created a Location")
        except Exception as e:
            print(e)

    def get_locations(self):
        """
        This Method is used to Get the Locations in Database
        :param input_json:
        :return:
        """
        try:
            output_json = {}
            total_locations = list(self.mongo_db_object.find_all(AppConfigurations.MONGO_DATABASE,
                                                                 AppConstants.LOCATION.MONGO_LOCATION_COLLECTION_NAME))
            output_json = total_locations
            return AppConstants.result_success_template(output_json)

        except Exception as e:
            print("Error while fetching the Location Data.", str(e))

    def update_location(self, input_json):
        """
        This method is used to update the location data
        :param input_json: location obj,
        :return:
        """
        try:
            if AppConstants.LOCATION.LOCATION_ID not in input_json \
                    or (input_json[AppConstants.LOCATION.LOCATION_ID] is None
                        or input_json[AppConstants.LOCATION.LOCATION_ID] == ""):
                print(AppConstants.LOCATION.LOCATION_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPLocationException(AppConstants.LOCATION.LOCATION_ID +
                                          AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            location_data = list(self.mongo_db_object.find_json(
                {AppConstants.LOCATION.LOCATION_ID: input_json[AppConstants.LOCATION.LOCATION_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.LOCATION.MONGO_LOCATION_COLLECTION_NAME))

            if location_data:
                try:
                    response = self.mongo_db_object.update_one(
                        {AppConstants.LOCATION.LOCATION_ID: input_json[AppConstants.LOCATION.LOCATION_ID]},
                        input_json, AppConfigurations.MONGO_DATABASE,
                        AppConstants.LOCATION.MONGO_LOCATION_COLLECTION_NAME)
                    print("Successfully updated location")
                except Exception as e:
                    print(e, 'exception in updating location')
                return AppConstants.result_success_template("successfully updated the location data")
            else:
                print("No Location found with the specified ID")
                raise BPLocationException("No Location found with the specified ID")
        except Exception as e:
            raise BPLocationException(e)

    def delete_location(self, input_json):
        """
        This method is delete the location
        :param input_json: location obj,
        :return:
        """
        try:
            if AppConstants.LOCATION.LOCATION_ID not in input_json \
                    or (input_json[AppConstants.LOCATION.LOCATION_ID] is None
                        or input_json[AppConstants.LOCATION.LOCATION_ID] == ""):
                print(AppConstants.LOCATION.LOCATION_ID + AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)
                raise BPLocationException(AppConstants.LOCATION.LOCATION_ID +
                                          AppConstants.PROJECT.NOT_PRESENT_ERROR_MSG)

            location_data = list(self.mongo_db_object.find_json(
                {AppConstants.LOCATION.LOCATION_ID: input_json[AppConstants.LOCATION.LOCATION_ID]},
                AppConfigurations.MONGO_DATABASE, AppConstants.LOCATION.MONGO_LOCATION_COLLECTION_NAME))
            print(location_data)
            if location_data:
                try:
                    response = self.mongo_db_object.remove(location_data[0], AppConfigurations.MONGO_DATABASE,
                                                           AppConstants.LOCATION.MONGO_LOCATION_COLLECTION_NAME)
                    print("Successfully deleted location")
                    return AppConstants.result_success_template("successfully updated the location data")
                except Exception as e:
                    print(e, 'exception in deleting location')
            else:
                print("No Location found with the specified ID")
                raise BPLocationException("No Location found with the specified ID")
        except Exception as e:
            raise BPLocationException(e)
