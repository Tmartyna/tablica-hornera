# jak maja wygladac tabele:
# input1    [ a 3 = -12, a 2 = 16, a 1 = 7, a 0 = 1 ]   
# input2    [ a 3 = 1, a 0 = 8 ]
# output1     | -12 | 16 | 7 | 1 |
#         0,5 | -12 | 10 | 2 | 0 |
#
# output2     | 1 |  0 | 0 | 8 |  
#          -2 | 1 | -2 | 4 | 0 | 


def tablica_hornera(wspolczynniki, pierwiastek):
    if len(wspolczynniki) > 6:
        return "Błąd: Zbyt wiele współczynników, program przyjmuje tylko 6."
    s = int(wspolczynniki[0].split(" ")[1])
    for wspolczynnik in wspolczynniki:
        if int(wspolczynnik.split(" ")[1]) != s:
            blad = "Błąd, pominąłeś a " + str(s) + " "
            return blad
        else:
            s = int(s) - 1


    wspol = 0 
    p = 0 
    top = ""
    bot = ""

    def wys():
        nonlocal top, bot
        dlugoscp = len(str(pierwiastek)) + 1
        if wspolczynnik == wspolczynniki[0]:
            top = dlugoscp * " " + "| " + str(wspol) + " |"
            bot = str(pierwiastek) + " | " + str(p) + " |"
        elif wspolczynnik == wspolczynniki[-1]:
            top = top + str(wspol) + " |"
            bot = bot + str(p) + " |"
        else:
            top = top + str(wspol) + " |"
            bot = bot + str(p) + " |"

    for wspolczynnik in wspolczynniki:
        wspol = int(wspolczynnik.split(" ")[3])

        if p == 0:
            p = wspol
        else:
            p = p * pierwiastek + wspol
        wys()

    if p != 0:
        string = top + "\n" + bot
    else:
        string = "Błąd: 0 nie działa w tablicy Hornera."
    return string
   
  #              | wspol | wspol | wspol | wspol | "\n"
  #  pierwiastek |   p   |   p   |   p   |   p   |