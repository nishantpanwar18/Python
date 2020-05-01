
import re
import sys

regex_pattern = r"...\."


test_string = input()

match1 = re.findall(regex_pattern, test_string)

print(match1)

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())