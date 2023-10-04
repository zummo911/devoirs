age = int (input ("Enter your age "))
if age >= 18:
    print ("You can vote!")
else:
    print ("You can't vote :(")

text = str (input ())
if len (text) > 0:
    print ("Text len", len (text))
else:
    print ("Empty string")

text = str (input ())
if len (text) == 0:
    print ("Empty string")
else:
    print (f"Text len = (len (text)) ")
while True:
    user_message = str(input("Пожалуйста, введите ввод \n"))
    if user_message != "q":
        print("Класс!")
    else:
        print ("Неправильная буква")

