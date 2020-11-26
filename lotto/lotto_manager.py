from lotto.ticket import Ticket
from lotto.city import City
from lotto.bet_type import BetType
from lotto.print_utils import PrintUtils
from lotto.extraction import Extraction

class LottoManager():
    #generate tickets
    #@parameter n_ticket -> number of ticket to generate
    #@return -> a ticket list
    @staticmethod
    def generate_tickets(n_ticket):
        ticket_list = []
        
        for i in range(n_ticket):
            PrintUtils.print_table_row("Ticket {0}".format(i+1),1)
            print()
            #------------------#
            #SELECT TYPE OF BET
            bet_type_list = []

            PrintUtils.print_table_row("- Please, choose the type of bet:")
            #print choose options
            for key, value in enumerate(BetType.get_bets_type(),1):
                PrintUtils.print_line("{0}: {1}".format(key,value))
            selected_bet_type = input("- ")

            while True:
                if selected_bet_type.isdigit():
                    selected_bet_type = int(selected_bet_type)-1
                    if BetType.is_bet_type_allowed(selected_bet_type):
                        bet_type_list.append(BetType(selected_bet_type))
                        break
                print()
                PrintUtils.print_line("The value must be a valid integer number from the range!")
                selected_bet_type = input("- ")

            #print selected value
            print_str = ""
            for bet in bet_type_list:
                print_str+= bet.get_bet_type_name() + " "

            PrintUtils.print_table_row("- Selected: {}".format(print_str))
            print()


            #---------------#
            #SELECT CITY
            city = None

            PrintUtils.print_table_row("Please, choose the city:")
            #print choose option
            for key,value in enumerate(City.get_cities(),1):
                PrintUtils.print_line("{:2d}: {}".format(key,value))
            
            selected_city = input("- ")

            while True:
                if selected_city.isdigit():
                    selected_city = int(selected_city)-1
                    if City.is_city_index_allowed(selected_city):
                        city = City(selected_city)
                        break
                print()
                PrintUtils.print_line("The value must be a valid integer number from the range!")
                selected_city = input("- ")

            PrintUtils.print_table_row("- Selected: {}".format(city.get_city_name()))
            print()

            #--------------#
            # SELECT NUMBER AMOUNT
            PrintUtils.print_table_row("Please, how many numbers do you want to play? \
                You can play at least {0} and a max of 10 numbers".format(Ticket.get_minimum_number_amount(bet_type_list)))
            numbers_amount = input("- ")

            while True:
                if numbers_amount.isdigit():
                    numbers_amount = int(numbers_amount)
                    if Ticket.is_number_amount_allowed(bet_type_list,numbers_amount):
                        break
                print()                
                PrintUtils.print_line("You can play at least {0} and a max of 10 numbers!".format(Ticket.get_minimum_number_amount(bet_type_list)))
                numbers_amount = input("- ")
            print()


            #--------------#
            # SELECT MONEY TO PLAY
            PrintUtils.print_table_row("Please, how much do you want to play?\
                                        The minimum bet on a Lotto ticket is € 1.00\
                                        The maximum is € 200.00 with denominations of € 0.50")
            money = input("- ")

            while True:
                try:
                    money = float(money)
                    if Ticket.is_money_allowed(money):
                        break
                except:
                    pass
                print()
                PrintUtils.print_line("Please, write a valid numeric value!")  
                money = input("- ")


            #GENERATE TICKET
            ticket_list.append(Ticket(city,bet_type_list,numbers_amount,money))
            print("\n\n")

        return ticket_list

    #print the tickets
    @staticmethod
    def print_tickets(tickets_list):
        print()
        PrintUtils.print_table_row("Here are the tickets:")
        print()
        for ind, ticket in enumerate(tickets_list):
            ticket_str = str(ticket)
            line = ticket_str.splitlines()

            PrintUtils.print_header_line("Italian lottery")
            PrintUtils.print_line("Ticket {0}".format(ind+1),1)
            PrintUtils.print_line(line[0],1) #city
            PrintUtils.print_line(line[1],1) #bet
            PrintUtils.print_line(line[2],1) #money
            PrintUtils.print_line("--- --- --- --- --- --- ---",1)
            PrintUtils.print_line(line[3],1)#numbers
            PrintUtils.print_footer_line("Good luck!")

            print("\n\n")

    #return a Lotto Extraction
    @staticmethod
    def extract_numbers():
        return Extraction()

    @staticmethod
    #print an extraction
    def print_extractions(extraction):
        PrintUtils.print_header_line("Italian Lottery - Extraction")

        extraction_str = str(extraction)
        lines = extraction_str.splitlines()
        for line in lines:
            PrintUtils.print_line(line,1)
        PrintUtils.print_horizontal_line_separator()
        print()
    
    @staticmethod
    #check if many tickets are winning
    def check_ticket_is_winning(extraction, tickets_list):
        for ind, ticket in enumerate(tickets_list,1):
            gross_win = 0.0
            net_win = 0.0
            gross_win, net_win = extraction.check_winning(ticket)

            PrintUtils.print_horizontal_line_separator()

            if gross_win > 0.0:
                PrintUtils.print_line("Ticket {0} is WINNING :)".format(ind),1)

                #formatting money
                formatted_float = "{:,.2f}".format(gross_win)
                main_currency, fractional_currency = formatted_float.split(".")[0], formatted_float.split(".")[1]
                new_main_currency = main_currency.replace(",", ".")
                currency = new_main_currency + "," + fractional_currency

                PrintUtils.print_line("Win: € {}".format(currency),1)

                if gross_win > 500.0:
                    PrintUtils.print_line("You have win more than 500€, so it is applicated a withholding tax of 8%")
                    PrintUtils.print_line("Your net win is: € {0}".format(net_win),1)

            else:
                PrintUtils.print_line("Ticket {0} is LOSER :(".format(ind),1)

            PrintUtils.print_horizontal_line_separator()
            