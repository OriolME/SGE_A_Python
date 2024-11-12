salari = 30000
if salari < 15000:
    iva = 0
elif salari < 30000:
    iva = 10
else:
    iva = 24


print(salari * iva / 100)
