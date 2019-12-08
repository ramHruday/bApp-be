import traceback
from flask import Flask, request
from flask_cors import CORS

from bin.common import AppConfigurations
from bin.core.services import productServices
from bin.core.services import supplierServices
from bin.core.services import locationServices
from bin.core.services import brandServices

# creating app
app = Flask(__name__)

# --------------------------------------------- REGISTER BLUEPRINTS ----------------------------------------------------

app.register_blueprint(productServices.product)
app.register_blueprint(supplierServices.supplier)
app.register_blueprint(locationServices.location)
app.register_blueprint(brandServices.brand)

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
