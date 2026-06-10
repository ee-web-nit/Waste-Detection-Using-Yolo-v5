from WasteDetection.logger import logging
from WasteDetection.exception import AppException
import sys
try:
    a = 1 / 0

except Exception as e:
    raise AppException(e, sys)