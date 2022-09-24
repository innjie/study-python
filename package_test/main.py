# Option 1
import package_test.thailand
trip_to = package_test.thailand.ThailandPackage()
trip_to.detail()

# Option 2
from package_test.thailand import ThailandPackage
trip_to = ThailandPackage
trip_to.detail()

# Option 3
from package_test import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# Option 4
from package_test import *
trip_to = vietnam.VietnamPackage()
# __all__ 에 설정하지 않았으므로 에러 발생
# trip_to = thailand.ThailandPackage()