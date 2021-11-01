
def main_menu():
    allowed_chars = ["1", "2", "3", "4", "q", "Q"]
    while True:
        user_main_menu = input('\nZahlenumrechner...\nBitte wählen Sie ....'
                               '\n(1) Hexadezimalzahl umwandeln.'
                               '\n(2) Dezimalzahl umwandeln.'
                               '\n(3) Oktalzahl umwandeln.'
                               '\n(4) Dualzahl umwandeln.'
                               '\n(q) Beenden.'
                               '\nIhre Wahl: ')

        if user_main_menu in allowed_chars:
            return user_main_menu
        else:
            print("......Fehlerhafte Eingabe!.......")

""" ------ Calculation Functions --------"""


def mult_pow(list, base):
    potenz = 0  # has to increment for each loop
    final_list = []
    for element in list:
        element = element * (base ** potenz)
        potenz +=1                          #we increment the potenz
        final_list.append(element)           #an add the element to the final_list
    return final_list


def hex_values(list):
    hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    list_result = []
    for element in list:
        element = int(element)
        if element >= 10 and element <= 15:
            if element in hex.keys():
                result = hex.get(element)
                list_result.append(result)
        else:
            list_result.append(str(element))
    return list_result


def dec_to(num,base):    # parameter 1 : num (int) decimal number to convert, base (int) base of the system
                        #returns list of integer
    list_1 = []
    while num > 0:     #  so it will stop when the integer resulting of the division is 0
        i, d = divmod(num, base)
        list_1.append(str(d))
        num = i
    ergebnis = list_1[::-1]
    return ergebnis


def hex_to_dec(num):
    dictionary = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}  #use dictionary to store the values
    list_1 = list(num)              #will save the input in a list
    list_results = []              #convert string of input into a list

   # -------- converting the letter to numerical values --------
    for element in list_1: #we loop through list_1 that contains the user entry
        if element.isalpha():       #if the element is a letter
            for key, value in dictionary.items():   #and if the letter is in dictionary
                if element == value:
                    list_results.append(int(key))       #we will save the results in list_results
        elif element.isdigit():                         #if the element is a number we will added to list_results
                list_results.append(int(element))
    list_results = list_results[::-1]
    return list_results

"""-------------Extra Fuctions ------------"""

def str_to_int_list(string):
    number_list = []
    for element in string:
        element = int(element)
        number_list.append(element)
    return number_list


def check_chars(list1, num):   #parameter list == list of ints, parameter num == int
    return (all(x in range(0,num) for x in list1))   #returns true if all numbers are in range


""" ---------- Menus ----------------- """

def menu_hexa():
    allowed_letters = ["A", "B", "C", "D", "E", "F"]
    number = input("Bitte Zahl für Umrechnung eingeben: ").upper()
    number = list(number)
    for element in number:
        if element.isalpha():
            if element not in allowed_letters:
                print("Bitte nur Ziffern oder die Buchstaben A,B,C,D,E,F verwenden")
                menu_hexa()
            #else:
                #break

    user_menu_2 = input('\nEingebene Zahl umrechnen in...'
                        '\n(d) Dezimalzahl'
                        '\n(o) Oktalzahl umwandeln.'
                        '\n(b) Dualzahl umwandeln.'
                        '\nIhre Wahl: ').lower()

    if user_menu_2 == "d":
        a = hex_to_dec(number)
        b = mult_pow(a, 16)
        print("Ergebnis: ", sum(b))
        main_prog()


    elif user_menu_2 == "o":
        a = hex_to_dec(number)
        b = mult_pow(a, 16)
        c = sum(b)
        d = dec_to(c, 8)
        print("Ergebnis: ", "".join(d))
        main_prog()

    elif user_menu_2 == "b":
        a = hex_to_dec(number)
        b = mult_pow(a, 16)
        c = sum(b)
        d = dec_to(c, 2)
        print("Ergebnis: ", "".join(d))
        main_prog()

    #else:
        #menu_hexa()


def menu_dec():
    number = input("Bitte Zahl für Umrechnung eingeben: ")
    a = number.isdigit()
    if a is True:
        number = int(number)
        user_menu_2 = input('\nEingebene Zahl umrechnen in...'
                            '\n(h) Hexadezimalzahl'
                            '\n(o) Oktalzahl umwandeln.'
                            '\n(b) Dualzahl umwandeln.'
                            '\nIhre Wahl: ').lower()

        if user_menu_2 == "h":
            a = dec_to(number,16)
            b = (hex_values(a))
            print ("Ergebnis: " + "".join(b))

        elif user_menu_2 =="o":
            ergebnis = dec_to(number,8)
            print("Ergebnis: " + "".join(ergebnis))

        elif user_menu_2 == "b":
            ergebnis = dec_to(number,2)
            print("Ergebnis: " + "".join(ergebnis))
    else:
        print("Bitte verwenden Sie nur Ziffern!")
        menu_dec()

def menu_okta():
    number = input("Bitte Zahl für Umrechnung eingeben: ")
    a = str_to_int_list(number)
    b = check_chars(a,8)   #returns false if the numbers are higher than 8 less than 0
    if b is True:

        user_menu_2 = input('\nEingebene Zahl umrechnen in...'
                            '\n(h) Hexadezimalzahl'
                            '\n(d) Dezimalzahl'
                            '\n(b) Dualzahl'
                            '\nIhre Wahl: ').lower()

        if user_menu_2 == "h":
            a = str_to_int_list(number)
            b = a[::-1]
            c = mult_pow(b, 8)
            d = sum(c)                  # gives decimal number
            e = dec_to(d, 16)
            f = (hex_values(e))
            print("Ergebnis: " + "".join(f))

        elif user_menu_2 == "d":
            a = str_to_int_list(number)
            b = a[::-1]
            c = mult_pow(b, 8)
            d = sum(c)
            print("Ergebnis: ",d)


        elif user_menu_2 == "b":                #Works !
            a = str_to_int_list(number)
            b = a[::-1]
            c = mult_pow(b, 8)
            d = sum(c)
            e = dec_to(d, 2)
            print("Ergebnis: " + "".join(e))

    else:
        print("Bitte verwenden Sie die Ziffern von 0 bis 7")
        menu_okta()

def menu_bin():
    number = input("Bitte Zahl für Umrechnung eingeben: ")
    a = number.isdigit()
    if a is True:
        a = str_to_int_list(number)
        b = check_chars(a,2)   #returns false if the numbers are higher than 8 less than 0
        if b is True:
            user_menu_2 = input('\nEingebene Zahl umrechnen in...'
                                '\n(h) Hexadezimalzahl'
                                '\n(d) Dezimalzahl'
                                '\n(o) Oktalzahl umwandeln.'
                                '\nIhre Wahl: ').lower()

            if user_menu_2 == "h":                          # Works!!!!
                a = str_to_int_list(number)  # transform string input to a int list and saves in variable
                b = a[::-1]  # reverse the list so the pow are ok
                c = mult_pow(b, 2)
                d = sum(c)                  #dec number
                e = dec_to(d,16)            #gives number values
                f = hex_values(e) #transforms numbers to letters representaion hex
                print("Ergebnis: ", "".join(f))

            if user_menu_2 == "d":                      # Works !!!!
                a = str_to_int_list(number)   #transform string input to a int list and saves in variable
                b = a[::-1]    #reverse the list so the pow are ok
                c = mult_pow(b, 2)
                d = sum(c)
                print("Ergebnis: ", d)
            if user_menu_2 == "o":                      # Works !!!!
                a = str_to_int_list(number)  # transform string input to a int list and saves in variable
                b = a[::-1]  # reverse the list so the pow are ok
                c = mult_pow(b, 2)
                d = sum(c)  # dec number
                e = dec_to(d, 8)  # gives number values
                f = hex_values(e)  # transforms numbers to letters representaion hex
                print("Ergebnis: ", "".join(f))
        else:
            print("Bitte verwenden Sie nur die Ziffern 0 und 1")
            menu_bin()
    else:
        print("Bitte verwenden Sie nur die Ziffern 0 und 1")
        menu_bin()



"""--------  Main Program ----------  """


def main_prog():
    user_selection = main_menu()
    while user_selection != "q":
        if user_selection == "1":
            menu_hexa()
            press_enter = input("\nWeiter mit der Eingabe-Taste ")
            user_selection = main_menu()

        elif user_selection == "2":
            menu_dec()
            press_enter = input("\nWeiter mit der Eingabe-Taste ")
            user_selection = main_menu()

        elif user_selection == "3":
            menu_okta()
            press_enter = input("\nWeiter mit der Eingabe-Taste ")
            user_selection = main_menu()

        elif user_selection == "4":             # works !!!
            menu_bin()
            press_enter = input("\nWeiter mit der Eingabe-Taste ")
            user_selection = main_menu()


main_prog()