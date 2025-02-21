nomer = int (input ("Введи номер месяца:\n"))
def month_to_season (nomer):
    if nomer in range (3,6):
        print ("Весна")
    elif nomer in range (6,9):
        print ("Лето")
    elif nomer in range (9,12):
        print ("Осень")
    elif nomer in {12,1,2}:
        print ("Зима")
    else:
        print ("Ввел некорректный месяц")

month_to_season (nomer)

