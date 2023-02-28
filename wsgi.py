import os
from app import app

# Get the environment variable or set to 'default'
config_name = os.getenv('FLASK_CONFIG', 'default')



if __name__ == '__main__':
    app.run()
