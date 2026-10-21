"""
Package: service
Package for configuring application logic and extensions
"""
import sys
import logging
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service import config
from service.common import log_handlers

# Create Flask app
app = Flask(__name__)
app.config.from_object(config)

# Initialize Talisman security headers
talisman = Talisman(app)

# Initialize CORS
CORS(app)

# Import routes and models after app creation
# pylint: disable=wrong-import-position, circular-imports
from service import routes, models  # noqa: F401 E402
from service.common import error_handlers  # noqa: F401

# Set up logging for production
log_handlers.init_app(app)

app.logger.info(16 * "=")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(16, "="))
app.logger.info(16 * "=")

try:
    models.init_db(app)  # Make database tables
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot initialize the database", error)
    sys.exit(4)

app.logger.info("Service initialized!")
