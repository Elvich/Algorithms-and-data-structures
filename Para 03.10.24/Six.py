strok = input("Введите строку: ")

if strok[len(strok)-1] == "1":
    print(f"{strok} рубль")
elif strok[len(strok)-1] == "2" or strok[len(strok)-1] == "3" or strok[len(strok)-1] == "4":
    if len(strok)>1 and strok[len(strok)-2]=="1":
        print(f"{strok} рублей")
    else:
        print(f"{strok} рубля")
else:
    print(f"{strok} рублей")
