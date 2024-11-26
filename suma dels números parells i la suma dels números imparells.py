sumapar = 0
sumainpar = 0
for num in [1,4,5,67,34,55,78,90,2,44,65,33,35,50]:
    if num % 2 == 0:
        sumapar = num + sumapar
        
    else:
        sumainpar = num + sumainpar
        

print(f"la suma par es: {sumapar}")
print(f"la suma inpar es: {sumainpar}")