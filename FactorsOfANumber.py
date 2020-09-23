Number = 99999999999999
factors = []
for i in range(1,1000000):
    Calculation = Number / i
    if i > Number:
        break
    if Calculation.is_integer():
        factors.append(i)
print(str(factors).strip("[").strip("]"))