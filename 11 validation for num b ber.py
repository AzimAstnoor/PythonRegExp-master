import re
date = "Hello, My number is 989-097-4840"
regex = re.findall("\d{3}-\d{3}-\d{4}", date)
if regex:
    print("Valide")
else:
    print("invalide")