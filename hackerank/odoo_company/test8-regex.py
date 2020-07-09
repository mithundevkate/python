'''Write a regular expression to match strings containing both "Odoo" and "#rules" in any order.
'''

import re
match_str = re.compile('(?i)(?:Odoo.*#rules|#rules.*Odoo)')
str = input()

if match_str.match(str):
    print('Yes')

