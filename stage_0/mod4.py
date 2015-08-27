import package_import_test.pm1
import sys

# package relative import
# "from . import" is added in py files in packages 
# and cannot exec directly,
# should be exec after import to other files


print(sys.path)