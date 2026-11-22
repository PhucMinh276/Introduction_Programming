a, b = int(input("Enter a: ")), int(input("Enter b: "))
mode = input("Enter sum type (odd/even): ")
res = []
for i in range(a, b + 1):
  tong = 0
  for c in str(i):
    tong += int(c)
  if (mode == "le" and tong % 2 != 0) or (mode == "chan" and tong % 2 == 0):
    res.append(str(i))
print(",".join(res))