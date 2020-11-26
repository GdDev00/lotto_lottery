from city import City
from ticket import Ticket
from random import randrange

class Extraction:
    def __init__(self):
        self.extraction = Extraction._extract()

    @staticmethod
    #Generate a lotto extraction dict
    #It is composed by a dictionary, key are the city index (please refer city class)
    #and value are 5 random number
    def _extract():
        extraction_dict = {}

        for key in range(0,len(City.get_cities())-1):
            temp_num = randrange(1,91)
            temp_extracted_number = []
            for _ in range(5):
                while True:
                    if temp_num not in temp_extracted_number:
                        temp_extracted_number.append(temp_num)
                        break
                    else:
                        temp_num = randrange(1,91)
            extraction_dict[key] = temp_extracted_number
        
        return extraction_dict

    #return the generated lotto dictionary
    def get_extraction(self):
        return self.extraction

    #check if a ticket is winning
    #
    #@parameter ticket -> the ticket to check
    #
    #@return -> the gross_win,net_win
    #@       -> if the tiken is loser, it returns 0,0
    def check_winning(self, ticket):
        gross_win,net_win = 0,0
        is_all_city = False
        matching_numbers = 0

        #-- CHECK IF TIKET IS ON ALL CITY --#
        
        #get "Tutte" index
        tutte_index = City.get_city_index_by_name("Tutte")

        #check if played city are all
        if ticket.get_city().get_city_index() == tutte_index:
            is_all_city = True
            #chek the matching numbers in every city
            for i in range(len(City.get_cities())-1):
                temp_matching_numbers = self._check_matching_numbers(i, ticket.get_numbers(),\
                                    ticket.get_minimum_number_amount(ticket.get_bets_type()))
                # ticket is winning
                if temp_matching_numbers > 0:
                    matching_numbers += temp_matching_numbers

        #ticket is played on only one city
        else:
            #check the matching numbers in one city
            matching_numbers = self._check_matching_numbers(ticket.get_city().get_city_index(),\
                            ticket.get_numbers(), ticket.get_minimum_number_amount(ticket.get_bets_type()))

        # ticket is winning
        if matching_numbers > 0:           
            gross_win, net_win = Extraction._calculate_win((len(ticket.get_numbers())), \
                                    matching_numbers, ticket.get_money(), ticket.get_bets_type(),is_all_city)
                        
        #return both gross and net win
        #these variable are initilized to 0 so if the ticket is loser it returns 0,0
        return gross_win, net_win


    #check matching number in one route
    #
    #@parameter city_index          -> the city index to check (refer to City class)
    #@parameter tck_numbers         -> a list of numbers to check if are matching
    #@parameter  min_numbers_needed -> minimum numbers needed to win
    #
    #@return -> the matching numbers
    #@       -> 0, it the ticket haven't any matching numbers
    def _check_matching_numbers(self, city_index, tck_numbers, min_numbers_needed):
        matching_number_count = 0

        for number in tck_numbers:
            if number in self.extraction[city_index]:
                matching_number_count += 1

        if matching_number_count < min_numbers_needed:
            matching_number_count = 0

        return matching_number_count


    def __str__(self):
        return_str = "" 
        for city,value in self.extraction.items():
            city_name = City.get_city_name_by_index(city)

            return_str += "{:8}: ".format(city_name)
            for num in value:
                return_str += "{:2d}  ".format(num)
            return_str += "\n"

        return return_str