#Время суток

current_time = (input ("Введите текущее время. Например 18:55.\n"))
current_hour = current_time.replace(":","")
current_hour = int(current_hour)
if 0 <= current_hour < 500:
    print("Доброй ночи")
elif 500 <= current_hour < 1200:
    print("Доброе утро")
elif 1200 <= current_hour < 1600:
    print("Добрый день")
elif 1600 <= current_hour <= 2359:
    print("Добрый вечер")
else:
    print("Добрый...Попробуйте ещё раз")