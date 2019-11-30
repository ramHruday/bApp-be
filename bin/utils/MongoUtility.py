

__author__ = 'hruday)'


from pymongo import MongoClient
import uuid


from bin.common.AppConstants import MongoConstants
#


def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv


def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv


class MongoUtility(object):
    def __init__(self, mongo_host, mongo_port, user_name=None, password=None):
        try:
            self.__mongo_OBJ__ = MongoClient(
                host=mongo_host,
                port=mongo_port
            )
        except Exception as e:
            print(e)

    def insert_one(self, json_data, database_name, collection_name):
        """
        To insert single document in collection
        :param json_data:
        :param database_name:
        :param collection_name:
        :return: id
        """
        try:
            try:
                mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert_one(json_data)
            except:
                if "_id" in json_data:
                    del json_data["_id"]
                mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert(json_data, check_keys=False)
                return mongo_response
            # logger.debug("Inserted document in mongo")
            return mongo_response.inserted_id
        except Exception as e:
            print(e)
            # logger.error("Error in inserting document: " + str(e))


    def insert_many(self, json_data, database_name, collection_name):
        """
        To insert multiple documents in collection
        :param json_data:
        :param collection_name:
        :param database_name:
        :return: response
        """
        try:
            mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert_many(json_data)
            json_mongo_response_object = mongo_response
            # logger.debug("Inserted documents in mongo")
            return json_mongo_response_object
        except Exception as e:
            print(e)
            # logger.error("Error in inserting document: " + str(e))


    def find_json(self, json_data, database_name, collection_name):
        """
        To find all document in collection based on the condition provided.
        :param json_data:
        :param database_name:
        :param collection_name:
        :return: response object
        """
        try:
            db = self.__mongo_OBJ__[database_name]
            mongo_response = db[collection_name].find(json_data)
            # logger.debug("Fetched results from mongo")
            return mongo_response
        except Exception as e:
            print(e)
            # logger.error("Error in finding document: " + str(e))



    def find_all(self, database_name, collection_name):
        """
        To find all the documents
        :param database_name:
        :param collection_name:
        :return: response object
        """
        try:
            db = self.__mongo_OBJ__[database_name]
            mongo_response = db[collection_name].find()
            # logger.debug("Fetched results from mongo")
            return mongo_response
        except Exception as e:
            print(e)
            # logger.error("Error in finding document: " + str(e))



    def remove(self, json_data, database_name, collection_name):
        """
        To delete document from collection
        :param json_data:
        :param database_name:
        :param collection_name:
        :return: success
        """
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].remove(json_data)
            # logger.debug("Deleted document from mongo")
            return "success"
        except Exception as e:
            print(e)
            # logger.error("Error in deleting document: " + str(e))


    def drop_collection(self, database_name, collection_name):
        """
        To delete collection from database
        :param database_name:
        :param collection_name:
        :return: success
        """
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection.drop_collection(collection_name)
            # logger.debug("Deleted collection from mongo")
            return "success"
        except Exception as e:
            print(e)
            # logger.error("Error in deleting collection: " + str(e))


    def update_one(self, condition, json_data, database_name, collection_name):
        """
        To update single document
        :param condition:
        :param json_data:
        :param database_name:
        :param collection_name:
        :return: success
        """
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].update_one(condition, {"$set": json_data})
            # logger.debug("Updated document from mongo")
            return "success"
        except Exception as e:
            print(e)
            # logger.error("Error in updating document: " + str(e))


    def update(self, condition, json_data, database_name, collection_name):
        """
        To update single document without using set
        :param condition:
        :param json_data:
        :param database_name:
        :param collection_name:
        :return: success
        """
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].update(condition, json_data)
            # logger.debug("Updated document from mongo")
            return "success"
        except Exception as e:
            print(e)
            # logger.error("Error in updating document: " + str(e))


    def update_by_removing_keys(self, condition, json_data, database_name, collection_name):
        """
        To update single document (removing the keys)
        :param condition:
        :param json_data:
        :param database_name:
        :param collection_name:
        :return: success
        """
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].update_one(condition, {"$unset": json_data})
            # logger.debug("Updated document from mongo")
            return "success"
        except Exception as e:
            print(e)
            # logger.error("Error in updating document: " + str(e))


    def aggregate_query(self, json_data, database_name, collection_name):
        """
        To search using aggregate query
        :param json_data:
        :param database_name:
        :param collection_name:
        :return: response object
        """
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].aggregate(json_data)
            # logger.debug("Fetched results from mongo")
            return mongo_response
        except Exception as e:
            print(e)
            # logger.error("Error in aggreation query: " + str(e))


    def close_connection(self):
        """
        To close the mongo connection
        :return:
        """
        try:
            if self.__mongo_OBJ__ is not None:
                self.__mongo_OBJ__.close()
            # logger.debug("Mongo connection closed")
        except Exception as e:
            print(e)
            # logger.error("Error during closing of connection: " + str(e))


    def find_item_containing_key_in_sub_json_object(self, condition_array, database_name, collection_name):
        """
        This function return item which contains provided JSON key inside sub json of mongodb record.
        :param: condition_array
        :param: database_name
        :param: collection_name
        :return: This function return item which contains provided JSON key inside sub json of mongodb record.
        """
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongodb_response = database_connection[collection_name].find({"$or": condition_array})
            mongodb_response = list(mongodb_response)[0]
            return mongodb_response
        except Exception as e:
            print(e)
            # logger.error("Error in finding document: " + str(e))


    def find_item_containing_key_in_sub_json_object_list(self, condition_array, database_name, collection_name):
        """
        This function return item which contains provided JSON key inside sub json of mongodb record.
        :param: condition_array
        :param: database_name
        :param: collection_name
        :return: This function return item which contains provided JSON key inside sub json of mongodb record.
        """
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongodb_response = database_connection[collection_name].find({"$or": condition_array})
            mongodb_response = list(mongodb_response)
            return mongodb_response
        except Exception as e:
            print(e)
            # logger.error("Error in finding document: " + str(e))


    def find_items_greater_than_date(self, datekey, value, database_name, collection_name):
        """
        This function takes date as parameter and returns the json data greater than these date
        :param date:
        :param database_name:
        :param collection_name:
        :return:
        """
        try:
            # mongodb_response = self.__mongo_OBJ__[database_name][collection_name].find(
            #     {datekey: {"$gte": parser.parse(value)}})
            mongodb_response = self.__mongo_OBJ__[database_name][collection_name].find(
                {datekey: {"$gt": value}})
            return mongodb_response
        except Exception as e:
            print(e)
            # logger.error("Error in finding document: " + str(e))


    @staticmethod
    def fetch_records_from_object(body):
        """

        :param body:
        :return: list
        """
        final_list = []
        try:
            for doc in body:
                final_json = doc
                final_list.append(final_json)
        except Exception as e:
            status_message = "could not fetch records from object", str(e)
            MongoConstants.failed_status[MongoConstants.error_key] = status_message
            # logger.exception(MongoConstants.failed_status)
        return final_list

    def read(self, json_data, database_name, collection_name):
        """

        :param json_data:
        :param database_name:
        :param collection_name:
        :return: response
        """
        response = []
        try:
            db = self.__mongo_OBJ__[database_name]
            mongo_response = db[collection_name].find(json_data)
            response = self.fetch_records_from_object(mongo_response)
            status_message = "Successfully got the record from db"
            MongoConstants.success_status[MongoConstants.result_key] = status_message
            # logger.info(MongoConstants.success_status)

        except Exception as e:
            status_message = "Failed to fetch record from db", str(e)
            MongoConstants.failed_status[MongoConstants.error_key] = status_message
            # logger.exception(MongoConstants.failed_status)
        return response

    def UUID_generator(self, type):
        """
        :param type:
        :return:
        """
        id = uuid.uuid4()
        id = str(id).replace("-", "")
        # hex_int = int(id, 16)
        # id = str(hex_int + 0x200)[:8]
        return type+"_" + id

    def rename_collection(self, database_name, old_name, new_name):
        """
        To find all the documents
        :param database_name:
        :param collection_name:
        :return: response object
        """
        try:
            db = self.__mongo_OBJ__[database_name]
            mongo_response = db[old_name].rename(new_name)
            # logger.debug("Renamed the collection")
            return mongo_response
        except Exception as e:
            print(e)
            # logger.error("Error in renaming collection: " + str(e))


    def delete_key(self, key, database_name, collection_name):
        """
        To delete key in all documents in a collection
        :param database_name:
        :param collection_name:
        :return: success
        """
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].update_many({}, {'$unset': {key: 1}})
            # logger.debug("Updated document from mongo")
            return "success"
        except Exception as e:
            print(e)