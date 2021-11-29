import pyperclip

dd = pyperclip.paste()
with open("text.txt", "w") as fp:
    fp.write(dd)
    fp.close()
# print(dd)

res = ""
lines = dd.split("\n")
for line in lines:
    line = line
    if not line.strip():
        continue
    if line.endswith(" \r"):
        res += line[0:-2]
    else:
        res += line + "\n"

print(res)

with open("text2.txt", "w") as fp:
    fp.write(res)
    fp.close()
