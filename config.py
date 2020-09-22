# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  


# Database
DATABASE = 'movies.db'


# A secret key that will be used for securely signing the session cookie
# and can be used for any other security related needs by extensions or 
# your application. It should be a long random string of bytes, although 
# unicode is accepted too.
SECRET_KEY = "secret"