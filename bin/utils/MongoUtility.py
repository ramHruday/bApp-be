"""
Mongo Utility
"""

from bin.utils import Logging

# Logger
logger = Logging.get_logger()
mongo_authentication = ''


class MongoUtility(object):
    """
    This contains various methods for mongo
    """

    def __init__(self, mongo_host, mongo_port):
        """

        :param mongo_host:
        :param mongo_port:
        """
        # try:
        # Mongo object
        # if mongo_authentication:
        # self.mongo_obj = MongoClient(host=mongo_host, port=mongo_port,username=mongo_username, password=mongo_password)
        # Db connection
        # else:
        # self.mongo_obj = MongoClient(host=mongo_host, port=mongo_port)
        # Db connection

        # except Exception as e:
        # logger.exception("Exception in mongo object creation in mongo utility " + str(e))

    def delete_db(self, database_name):
        return ''

    def query_mongo_by_condition(self, database_name, collection_name, condition):
        """

        :param database_name: Database Name
        :param collection_name: Collection Name
        :param condition: Records will be fetched based on this condition
        :return: Records that be fetched from a particular database, collection and condition
        """
        try:
            # write mongo_query
            return {"status_key": 'ok'}
        except Exception as e:
            return {"status_key": 'ok'}
