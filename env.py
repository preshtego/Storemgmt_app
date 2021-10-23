import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG_VALUE = os.environ.get('DEBUG_VALUE')

print(STOREMGMT_SECRET_KEY)
print(STOREMGMT_DEBUG_VALUE)