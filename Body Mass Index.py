#Body Mass Index
m = int(input("Введите свой вес в килограммах:\n"))
h_sm = int(input("Введите свой рост в сантиметрах: \n"))
h = float(h_sm/100)
BMI = m/h**2
print ("Индекс вашей массы тела =",BMI)