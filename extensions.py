import re
s = input("File name: ")
if re.findall(".gif", s):
    print("image/gif")
elif re.findall(".jpg", s) or re.findall(".jpeg", s):
    print("image/jpeg")
elif re.findall(".png", s):
    print("image/png")
elif re.findall(".pdf", s):
    print("application/pdf")
elif re.findall(".txt", s):
    print("text/plain")
elif re.findall(".zip", s):
    print("application/zip")
else:
    print("application/octet-stream")