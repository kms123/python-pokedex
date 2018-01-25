import os
from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib'))
