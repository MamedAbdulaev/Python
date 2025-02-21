year= int (input ("Введи год:\n"))
def func(ostatok):
    ostatok=year%4
    if ostatok ==0:
        print ("Visokosniy")
    else:
        print ("nea")

func(year)


