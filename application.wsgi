import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/path/to/your/application')

from app import app as application
