# input = "000520123456"
# Output = "520123456"

import re
input = "000520123456"
# print(re,[^[0]],input)
print(re.sub(r'^0*', '', input))
