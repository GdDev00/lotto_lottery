from lotto.lotto import *
from lotto.print_utils import PrintUtils

MAX_BILLS = 5

#Generate x random ticket
#@params tickets_number -> the number of ticket that you want generate
#@return                -> a list with all the ticket
def generate_tickets(tickets_number):

    tickets_list = []

    for i in range(tickets_number):
        PrintUtils.print_table_row("Ticket %d" %(i+1))

        #------------------#
        #SELECT TYPE OF BILL
        print("Please, select the type of bill: ")
        #print all type of bill 
        for type_bill in Type:
            print("%d: %s" %(type_bill.value,type_bill.name))

        selected_type_bill = input("- ")
        while selected_type_bill.isdigit()==False or int(selected_type_bill)>len(Type):
            print("The value must be a valid integer number!")
            selected_type_bill = input("- ")
        selected_type_bill = int(selected_type_bill)
        PrintUtils.print_table_row(Type(selected_type_bill).name)
        print()

        #------------#
        #SELECT ROUTE
        print("Please, select the route: ")
        #print all routes
        for route in Ruote:
            print("%d: %s" %(route.value,route.name))
        
        selected_route = input("- ")
        while selected_route.isdigit()==False or int(selected_route)>len(Ruote):
            print("The value must be a valid integer number!")
            selected_route = input("- ")
        
        selected_route = int(selected_route)
        PrintUtils.print_table_row(Ruote(selected_route).name)
        print()

        #--------------#
        #SELECT AMOUNT OF NUMBERS
        min_amount = Type(selected_type_bill).value
        print("You have chosen %s, so have to play at least %d number and a max of 10 numbers"\
            %(Type(selected_type_bill).name,min_amount))

        print("Please, how many number do you want to play?")
        number_amount = input("- ")
        while number_amount.isdigit()==False or int(number_amount)<min_amount or int(number_amount)>10:
            print("The value must be a valid integer number!")
            number_amount = input("- ")
        number_amount = int(number_amount)

        #GENERATE TICKET
        ticket = Ticket(number_amount,selected_type_bill,selected_route)

        tickets_list.append(ticket)

        print()
        print()
        
    return tickets_list

def main():
    PrintUtils.print_ticket_header_line()   
    PrintUtils.print_table_row("Ticket generator") 
    print()

    print("How many tickets do you want generate?")
    print("Please, write a number between 1-%d; 0 to exit:"%MAX_BILLS) 
    n_of_tickets = input("- ")
    while n_of_tickets.isdigit()==False or int(n_of_tickets)>MAX_BILLS:
        print("The value must be a valid integer number!")
        n_of_tickets = input("- ")
    
    n_of_tickets = int(n_of_tickets)

    #exit
    if n_of_tickets == 0:
        print("Quitting...")
        quit(0)

    #generate ticket
    tickets = generate_tickets(n_of_tickets)

    #print ticket
    for ticket in tickets:
        ticket.print()
        print()
        print()
    main()

main()