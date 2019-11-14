import traceback
from flask import Flask, request
from flask_cors import CORS

from bin.common import AppConfigurations
# from bin.core.services.login import login_user
from bin.core.services.leavesService import

# creating app
app = Flask(__name__)

# --------------------------------------------- REGISTER BLUEPRINTS ----------------------------------------------------

app.register_blueprint(login_user)

# ---------------------------------- CORS configurations for Service endpoints -----------------------------------------

CORS(app, resources={
    r"/*": {"origins": "*"}
})

# ----------------------------------------------------------------------------------------------------------------------
service_port = AppConfigurations.service_port
service_host = AppConfigurations.service_host

if __name__ == '__main__':
    try:
        print(('Starting service @ port ' + str(service_port)))
        app.run(host=str(service_host), port=int(service_port), debug=True, threaded=True, use_reloader=False)
    except:
        traceback.print_exc()
