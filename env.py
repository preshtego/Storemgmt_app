import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG_VALUE = os.environ.get('DEBUG_VALUE')

print(SECRET_KEY)
print(DEBUG_VALUE)