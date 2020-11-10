#LEARNING PATH 1
from enum import Enum
from display_table_lib import *
import random

#enum with all the Route (city) of the bill
class Ruote(Enum):
    BARI = 1
    CAGLIARI = 2
    FIRENZE = 3
    GENOVA = 4
    MILANO = 5
    NAPOLI = 6
    PALERMO = 7
    ROMA = 8
    TORINO = 9
    VENEZIA = 10
    TUTTE = 11

#enum with all the type of bill
class Type(Enum):
    AMBATA = 1
    AMBO = 2
    TERNO = 3
    QUATERNA = 4
    CINQUINA = 5

class Ticket():
    
    #INIT!
    def __init__(self, amount_number, bill_type, route):

        #check the validity of the type
        if(bill_type > 0 and bill_type <= len(Type)):
            self._bill_type = bill_type
        else:
            raise ValueError("The entered number is not included in the allowed type range!")

        #check if the amount of number is valid and if it consistent with the chosen type
        if amount_number > 0 and amount_number <= 10:
            if amount_number >= Type(bill_type).value:
                self._amount_number = amount_number
            else:
                raise ValueError("the amount of number is not consistent with the chosen type!")
        else:
            raise ValueError("the amount of number must be an integer and it cannot be greater than 10!")


        #check the validity of the route
        if (route > 0 and route <= len(Ruote)):
            self._route = route
        else:
            raise ValueError("The entered number is not included in the allowed route range!")

        #generate ticket
        self._generate()

    #generate random ticket
    def _generate(self):
        number_list = []

        for _ in range(self._amount_number):
            #generate a random number between 1-90
            number = random.randrange(1,90)
            
            #check if the number is already in the extracted numbers
            if number not in number_list:
                number_list.append(number)
        
        self._numbers = number_list

    #print the ticket 
    def print(self):
        print_ticket_header_line()
        print_line("Ticket",1)
        print_line("Routa: %s" %(Ruote(self._route).name))
        print_line("Type: %s" %(Type(self._bill_type).name))
        number = ""
        for num in self._numbers:
            number += str(num) +" "
        print_line("--- --- ---",1)
        print_line(number,1)
        print_ticket_footer_line()
