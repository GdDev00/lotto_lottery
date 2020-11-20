import argparse

from lotto.ticket import Ticket
from lotto.city import City
from lotto.bet_type import BetType
from lotto.print_utils import PrintUtils

MAX_BILLS = 5


#generate tickets
#@parameter n_ticket -> number of ticket to generate
#@return -> a ticket list
def generate_tickets(n_ticket):
    ticekt_list = []
    
    for i in range(n_ticket):
        PrintUtils.print_table_row("Ticket {0}".format(i+1))

        #------------------#
        #SELECT TYPE OF BET
        bet_type_list = []

        PrintUtils.print_line("Please, choose the type of bet:")
        #print choose options
        for key, value in enumerate(BetType.get_bets_type(),1):
            PrintUtils.print_line("{0}: {1}".format(key,value))
        selected_bet_type = input("- ")

        while True:
            if selected_bet_type.isdigit()==True:
                selected_bet_type = int(selected_bet_type)-1
                if BetType.is_bet_type_allowed(selected_bet_type) == True:
                    bet_type_list.append(BetType(selected_bet_type))
                    break
            
            PrintUtils.print_line("The value must be a valid integer number from the range!")
            selected_bet_type = input("- ")

        #print selected value
        print_str = ""
        for bet in bet_type_list:
            print_str+= bet.get_bet_type_name() + " "

        PrintUtils.print_table_row(print_str)
        print()


        #---------------#
        #SELECT CITY
        city = None

        PrintUtils.print_line("Please, choose the city:")
        #print choose option
        for key,value in enumerate(City.get_cities(),1):
            PrintUtils.print_line("{0}: {1}".format(key,value))
        
        selected_city = input("- ")

        while True:
            if selected_city.isdigit()==True:
                selected_city = int(selected_city)-1
                if City.is_city_index_allowed(selected_city) == True:
                    city = City(selected_city)
                    break

            PrintUtils.print_line("The value must be a valid integer number from the range!")
            selected_city = input("- ")

        PrintUtils.print_table_row(city.get_city_name())
        print()

        #--------------#
        # SELECT NUMBER AMOUNT
        PrintUtils.print_line("Please, how many numbers do you want to play?")
        PrintUtils.print_line("You can play at least {0} and a max of 10 numbers".format(Ticket.get_minimum_number_amount(bet_type_list)))
        numbers_amount = input("- ")

        while True:
            if numbers_amount.isdigit() == True:
                numbers_amount = int(numbers_amount)
                if Ticket.is_number_amount_allowed(bet_type_list,numbers_amount) == True:
                    break

            PrintUtils.print_line("You can play at least {0} and a max of 10 numbers!".format(Ticket.get_minimum_number_amount(bet_type_list)))
            numbers_amount = input("- ")

        #generate Ticket
        ticekt_list.append(Ticket(city,bet_type_list,numbers_amount))

    return ticekt_list

def print_tickets(tickets_list):
    for ind, ticket in enumerate(tickets_list):
        ticket_str = str(ticket)
        line = ticket_str.splitlines()

        PrintUtils.print_header_line("Italian lottery")
        PrintUtils.print_line("Ticket {0}".format(ind+1),1)
        PrintUtils.print_line(line[0]) #city
        PrintUtils.print_line(line[1]) #bet
        PrintUtils.print_line("--- --- --- --- --- --- ---",1)
        PrintUtils.print_line(line[2],1)#numbers
        PrintUtils.print_footer_line("Good luck!")

        print("\n\n")


def main():
    parser = argparse.ArgumentParser(description="Lotto ticket")
    parser.add_argument("-n", type=int, help='amount of ticket or numbers', choices=list(range(1,MAX_BILLS+1)))
    args = parser.parse_args()
    n_of_tickets = args.n

    while True:
        PrintUtils.print_header_line("Italian Lottery - Ticket")

        #no paramater from cli
        if(n_of_tickets == None):
            PrintUtils.print_line("How many tickets do you want generate?")
            PrintUtils.print_line("Please, write a number between 1-{}; 0 to exit:".format(MAX_BILLS)) 

            n_of_tickets = input("- ")
            while n_of_tickets.isdigit()==False or int(n_of_tickets)>MAX_BILLS:
                PrintUtils.print_line("The value must be a valid integer number!")
                n_of_tickets = input("- ")
            
            n_of_tickets = int(n_of_tickets)

        #exit
        if n_of_tickets == 0:
            PrintUtils.print_line("Quitting...")
            quit(0)

        print()

        #generate x numbers
        tickets = generate_tickets(n_of_tickets)
        
        #print tickets
        print()
        PrintUtils.print_table_row("Here are the tickets:")
        print()
        print()
        print_tickets(tickets)

        n_of_tickets = None

if __name__ == "__main__":
    main()