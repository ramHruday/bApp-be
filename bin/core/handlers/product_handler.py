import json
import time
import datetime
import traceback
from scripts.constants import app_configuration
from scripts.constants import app_constants
from scripts.exceptions.mr_exceptions import MRNotificationException, MRConnectionException, \
    MRProjectHandlerException
from scripts.logging import mr_logging
from scripts.utils.mongo_utility import MongoUtility
from scripts.utils.general_utils import get_unique_id, get_current_time_in_epoch
from datetime import datetime
import time
import calendar

logger = mr_logging.get_logger()
class NotificationHandler(object):
    def __init__(self):
        try:
            self.mongo_db_object = MongoUtility(
                app_configuration.MONGO_HOST,
                app_configuration.MONGO_PORT
            )
        except MRConnectionException:
            logger.error(str(traceback.print_exc()))
            raise MRConnectionException("Exception while initializing Notification Handler.")


    def create_product(self, input_json):
        try:
            logger.info("check the mandatory keys are present in json or not")
            logger.info("Starting create notification:"+str(input_json))
            if app_constants.Notification.TYPE not in input_json \
                    or (input_json[app_constants.Notification.TYPE] is None
                        or input_json[app_constants.Notification.TYPE] == ""):
                logger.error(app_constants.Notification.TYPE + app_constants.Projects.NOT_PRESENT_ERROR_MSG,
                             exc_info=True)
                raise MRNotificationException(app_constants.Notification.TYPE +
                                              app_constants.Projects.NOT_PRESENT_ERROR_MSG)
            if app_constants.Notification.MESSAGE not in input_json \
                    or (input_json[app_constants.Notification.MESSAGE] is None
                        or input_json[app_constants.Notification.MESSAGE] == ""):
                logger.error(app_constants.Notification.MESSAGE + app_constants.Projects.NOT_PRESENT_ERROR_MSG,
                             exc_info=True)
                raise MRNotificationException(app_constants.Notification.MESSAGE +
                                              app_constants.Projects.NOT_PRESENT_ERROR_MSG)
            # input_json[app_constants.Notification.CREATED_TIME]=datetime.datetime.now()
            input_json[app_constants.Notification.CREATED_TIME] = int(get_current_time_in_epoch() / 1000) * 1000
            input_json[app_constants.Notification.NOTIFICATION_ID] = self.mongo_db_object.UUID_generator(app_constants.Notification.NOTIFICATION_ID)
            input_json[app_constants.Notification.ISREAD]=False
            self.mongo_db_object.insert_one(input_json, app_configuration.MONGO_DATABASE, app_constants.Notification.MONGO_NOTIFICATIONS_COLLECTION_NAME)
            logger.info("Notification created time:"+str(input_json[app_constants.Notification.CREATED_TIME]))
            logger.info("Successfully created notification")
            return app_constants.result_success_template("Successfully Created a Notification")
        except MRNotificationException as e:
            logger.debug("Error While inserting Notification", exc_info=True)
            raise MRNotificationException(str(e))


    def get_notification(self,input_json):
        """
        This Method is used to Get the Notifications in Database
        :param input_json:
        :return:
        """
        try:
            # Notification_obj=NotificationHandler()
            # Notification_obj.insert_notifcation({app_constants.notification.TYPE:"Test",app_constants.notification.MESSAGE:"Test"})
            logger.debug("Checking if input is having any time")
            logger.info("Starting get notification:"+str(input_json))
            output_json ={"notification":[],
                          "progress":[]}
            progress = self.fetch_progress_data()
            output_json["progress"] = progress
            notification = []
            if app_constants.Notification.time not in input_json or (input_json[app_constants.Notification.time] is None
                                                                     or input_json[app_constants.Notification.time] == ""):
                logger.info("fetching all the Notifications data from the database")
                total_notification_data = self.mongo_db_object.find_all_sort (app_configuration.MONGO_DATABASE,
                                                                         app_constants.Notification.MONGO_NOTIFICATIONS_COLLECTION_NAME,"CreatedTime",-1)
                if total_notification_data.count() != 0:
                    for notification_obj in total_notification_data:
                        del notification_obj['_id']
                        try:
                            datetime_obj_date = notification_obj[app_constants.Notification.CREATED_TIME]
                            # string_date = datetime_obj_date.strftime("%Y-%m-%d %H:%M:%S")
                            string_date = datetime.fromtimestamp(datetime_obj_date/1000).strftime('%Y-%m-%d %H:%M:%S')
                            notification_obj[app_constants.Notification.CREATED_TIME] = string_date
                            notification.append(notification_obj)
                        except Exception as e:
                            logger.exception(str(e))
                output_json["notification"] = notification
                logger.info("Completed get notification:")
                logger.info("notification:" + str(notification))
                return app_constants.result_success_template(output_json)
            else:
                logger.info("searching notifications above the requested time"+str(input_json["time"]))
                timestamp = datetime.strptime(input_json["time"], '%Y-%m-%dT%H:%M:%S.%fZ')
                logger.info("timestamp:"+str(timestamp))
                epoch_time = time.mktime(timestamp.timetuple())
                logger.info("converted epoch time:"+str(epoch_time))
                epoch_time = epoch_time *1000
                notification_data=self.mongo_db_object.find_items_greater_than_date(app_constants.Notification.CREATED_TIME, epoch_time, app_configuration.MONGO_DATABASE, app_constants.Notification.MONGO_NOTIFICATIONS_COLLECTION_NAME)
                if notification_data.count()!=0:
                    for notification_obj in notification_data:
                        del notification_obj['_id']
                        try:
                            datetime_obj_date = notification_obj[app_constants.Notification.CREATED_TIME]
                            # string_date = datetime_obj_date.strftime("%Y-%m-%d %H:%M:%S")
                            string_date = datetime.fromtimestamp(datetime_obj_date/1000).strftime('%Y-%m-%d %H:%M:%S')
                            notification_obj[app_constants.Notification.CREATED_TIME]=string_date
                            notification.append(notification_obj)
                        except Exception as e:
                            logger.exception(str(e))
                output_json["notification"] = notification
                logger.info("Completed get notification:")
                logger.info("notification:"+str(notification))
                return app_constants.result_success_template(output_json)
        except MRNotificationException as e:
            logger.error("Error while fetching the Notification Data.", exc_info=True)
            raise MRNotificationException(str(e))

    def update_notification(self,input_json):
        """
        This method is used to update the read status of a notification
        :param input_json: notification Id, Readstatus
        :return:
        """
        try:
            logger.info("check the mandatory keys are present in json or not")
            logger.info("Starting update notification:"+str(input_json))
            if app_constants.Notification.NOTIFICATION_ID not in input_json \
                    or (input_json[app_constants.Notification.NOTIFICATION_ID] is None
                        or input_json[app_constants.Notification.NOTIFICATION_ID] == ""):
                logger.error(app_constants.Notification.NOTIFICATION_ID + app_constants.Projects.NOT_PRESENT_ERROR_MSG,
                             exc_info=True)
                raise MRNotificationException(app_constants.Notification.NOTIFICATION_ID +
                                              app_constants.Projects.NOT_PRESENT_ERROR_MSG)

            if app_constants.Notification.ISREAD not in input_json \
                    or (input_json[app_constants.Notification.ISREAD] is None
                        or input_json[app_constants.Notification.ISREAD] == ""):
                logger.error(app_constants.Notification.ISREAD + app_constants.Projects.NOT_PRESENT_ERROR_MSG,
                             exc_info=True)
                raise MRNotificationException(app_constants.Notification.ISREAD +
                                              app_constants.Projects.NOT_PRESENT_ERROR_MSG)
            logger.debug("Searching for notification data in the database")
            notification_data=self.mongo_db_object.find_json({app_constants.Notification.NOTIFICATION_ID:input_json[app_constants.Notification.NOTIFICATION_ID]}, app_configuration.MONGO_DATABASE, app_constants.Notification.MONGO_NOTIFICATIONS_COLLECTION_NAME)
            if notification_data.count():
                for notification_obj in notification_data:
                    notification_obj[app_constants.Notification.ISREAD]=input_json[app_constants.Notification.ISREAD]
                    self.mongo_db_object.update_one({app_constants.Notification.NOTIFICATION_ID:input_json[app_constants.Notification.NOTIFICATION_ID]}, notification_obj, app_configuration.MONGO_DATABASE, app_constants.Notification.MONGO_NOTIFICATIONS_COLLECTION_NAME)
                logger.info("Successfully updated nofification")
                return app_constants.result_success_template("successfully updated the notification data")
            else:
                logger.debug("No Notification found with the specified ID")
                raise MRNotificationException("No Notification found with the specified ID")
        except  MRNotificationException as e:
            logger.error("Error while updating the Notification data",exc_info=True)
            raise MRNotificationException(str(e))

    def drop_notification(self):
        """
        This method is used to drop notification collection
        :return:
        """
        try:
            logger.debug("Dropping notification collection in the database")
            self.mongo_db_object.drop_collection(app_configuration.MONGO_DATABASE,
                                                 app_constants.Notification.MONGO_NOTIFICATIONS_COLLECTION_NAME)

            return app_constants.result_success_template("successfully deleted the notification data")
        except  MRNotificationException as e:
            logger.error("Error while updating the Notification data", exc_info=True)
            raise MRNotificationException(str(e))


