month = input("Введите текущий месяц: ")
month = month.lower()
if month in ["сентябрь", "октябрь", "ноябрь"]:
    print("Сейчас осень!")
elif month in ["декабрь", "январь", "февраль"]:
    print("Сейчас зима!")
elif month in ["март", "апрель", "май"]:
    print("Сейчас весна!")
elif month in ["июнь", "июль", "август"]:
    print("Сейчас лето!")
else:
    print("Сейчас...Сложно сказать")


