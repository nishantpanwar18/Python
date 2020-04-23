
import re
import sys

regex_pattern = r"\.\.\.."


test_string = input()

match = re.findall(regex_pattern, test_string)

print(match)