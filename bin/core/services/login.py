"""
login Services
"""
import json
from flask import request, Blueprint
from bin.utils import Logging
from bin.core.application import loginAC

# Logger
logger = Logging.get_logger()

# Login Blueprint
login_user = Blueprint("login_user", __name__)


@login_user.route("/validate", methods=["POST"])
def login():
    """
    Api Endpoint for listing login
    :return:
    """
    try:
        logger.debug("Inside list workflow approval granularity")
        # Request JSON
        input_json = json.loads(request.get_data())
        response = loginAC.validate_user(input_json)
        return json.dumps(response)
    except Exception as e:
        # Error Response
        logger.error(str(e))
        message = 'falied'
        return {"status": "error", "message": message}
