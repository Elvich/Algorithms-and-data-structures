strok = input("Введите строку: ")
strok = list(strok)

if len(strok)%2!=0:
    print("Строку нельзя разделить")
else:
    if strok[:len(strok)//2] == strok[len(strok)//2:]:
        print("Строку можно разделить")
    else:
        print("Части строки не одинаковы")
