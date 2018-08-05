# pip install -U allure-behave
# pip install -U json2html

import os

currentPath = os.getcwd()
print(currentPath)
cmd = "cd com/behave && behave -t @add,@sub,@div,@mul --junit -f json -o reports/1.json"
os.system(cmd)

