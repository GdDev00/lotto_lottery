import argparse
from lotto.lotto_manager import LottoManager
from lotto.print_utils import PrintUtils

MAX_BILLS = 5


def main():
    parser = argparse.ArgumentParser(description="Lotto ticket")
    parser.add_argument("-n", type=int, help='amount of ticket or numbers', choices=list(range(1,MAX_BILLS+1)))
    args = parser.parse_args()
    n_of_tickets = args.n

    lotto_manager = LottoManager()

    while True:
        PrintUtils.print_header_line("Italian Lottery - Ticket")

        #no paramater from cli
        if(n_of_tickets == None):
            PrintUtils.print_line("How many tickets do you want generate?")
            PrintUtils.print_line("Please, write a number between 1-{}; 0 to exit:".format(MAX_BILLS)) 

            n_of_tickets = input("- ")
            while True:
                if n_of_tickets.isdigit( )== False or int(n_of_tickets) > MAX_BILLS:
                    PrintUtils.print_line("The value must be a valid integer number!")
                    n_of_tickets = input("- ")
                else:
                    break
            
            n_of_tickets = int(n_of_tickets)

        #user wants exit
        if n_of_tickets == 0:
            PrintUtils.print_line("Quitting...")
            quit(0)

        print()

        #generate x numbers
        tickets = lotto_manager.generate_tickets(n_of_tickets)
        
        #print tickets
        lotto_manager.print_tickets(tickets)

        #generate and print extractions
        extraction = lotto_manager.extract_numbers()
        lotto_manager.print_extractions(extraction)

        #check extractions
        lotto_manager.check_winning(extraction, tickets)

        n_of_tickets = None
        print("\n \n \n")
    print() 
    

if __name__ == "__main__":
    main()