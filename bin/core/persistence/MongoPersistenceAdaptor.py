from bin.utils import Logging

# Logger
logger = Logging.get_logger()


class UserLogin(object):
    def __init__(self):
        logger.info(self.__class__)

    def search_user(self, user_name, password):
        """
        This mothos to search user
        :param user_name:
        :param password:
        :return:
        """

        try:
            logger.info(self.__module__)
            results = ''
            # connect db  mongo_obj = MongoUtility(AppConfigurations.mongo_host, int(AppConfigurations.mongo_port))
            query = {
                "username": user_name,
                "password": password
            }
            # results = mongo_obj.query_mongo_by_condition(condition=query, database_name=AppConfigurations.system_db,
            #                                              collection_name=AppConfigurations.user_details_collection)
            # mongo_obj.close_connection()

            return results
        except Exception as e:
            logger.error(str(e))
            raise Exception(str(e))
