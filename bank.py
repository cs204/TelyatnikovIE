import re
s = input("Приветствие: ")
if re.match("здравствуйте", s):
    print("$0")
elif re.match("з", s):
    print("$20")
else:
    print("$100")