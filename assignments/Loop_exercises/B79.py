a, b = int(input("Enter a: ")), int(input("Enter b: "))
res = []
for i in range(a, b + 1):
  s = str(i)
  if int(s[0]) + int(s[1]) == int(s[2]) + int(s[3]):
    res.append(str(i))
print(",".join(res))