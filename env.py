import os

STOREMGMT_SECRET_KEY = os.environ.get('STORE_SECRET_KEY')
STOREMGMT_DEBUG_VALUE = os.environ.get('STORE_DEBUG_VALUE')

print(STOREMGMT_STORE_SECRET_KEY)
print(STOREMGMT_DEBUG_VALUE)