# Option 1
from module_test import price_module

price_module.price(3)
price_module.price_morning(4)

# Option 2
import price_module as mv

mv.price(3)
mv.price_morning(4)

# Option 3
from price_module import *

price(3)
price_morning(4)

# Option 4
from price_module import price, price_morning

price(3)
price_morning(4)

# Option 5
from price_module import price as p

p(5)