a, b = int(input("Enter a: ")), int(input("Enter b: "))
res = []
for i in range(a, b + 1):
  hop_le = True
  for c in str(i):
    if int(c) % 2 == 0:
      hop_le = False
      break
  if hop_le:
    res.append(str(i))
print(",".join(res))
