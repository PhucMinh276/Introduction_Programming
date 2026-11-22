a, b = int(input("Enter a: ")), int(input("Enter b: "))
res = []
for i in range(a, b + 1):
  le = 0
  chan = 0
  for c in str(i):
    if int(c) % 2 != 0:
      le += 1
    else:
      chan += 1
  if le == 2 and chan == 2:
    res.append(str(i))
print(",".join(res))