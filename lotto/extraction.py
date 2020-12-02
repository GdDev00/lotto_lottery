from city import City
from ticket import Ticket
from random import randrange

class Extraction:
    #a possible combination table
    #key are the played number
    #value are the combination, index of value are referred to the bet type
    #for example 2:[2,1] ->
    #   2 -> played number [2(two combination for ambata), 1 combination for ambo]
    winning_combination_table = {1: [1],
                                 2: [2, 1],
                                 3: [3, 3, 1],
                                 4: [4, 6, 4, 1],
                                 5: [5, 10, 10, 5, 1],
                                 6: [6, 15, 20, 15, 6],
                                 7: [7, 21, 35, 35, 21],
                                 8: [8, 28, 56, 70, 56],
                                 9: [9, 36, 84, 126, 126],
                                 10:[10, 45, 120, 210, 252]}
    
    
    #a winning table for 1€
    #key are the played number
    #value are the winning money, index of value are referred to the bet type
    gross_winning_money_table =  {1: [11.23],
                                  2: [5.61, 250],
                                  3: [3.74, 83.33, 4500],
                                  4: [2.80, 41.66, 1125, 120000],
                                  5: [2.24, 25, 450, 24000, 6000000],
                                  6: [1.87, 16.66, 225, 8000, 1000000],
                                  7: [1.60, 11.90, 128.57, 3428.57, 285714.28],
                                  8: [1.40, 8.92, 80.35, 1714.28, 107142.85],
                                  9: [1.24, 6.94, 53.57, 952.38, 47619.04],
                                  10: [1.12, 5.55, 37.50, 571.42, 23809.52]}
 


 
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


    #calculate the win money of a ticket
    #
    #@parameter numbers_amount   -> the amount of played number
    #@parameter numbers_matching -> the numbers matching (result of _check_matching_numbers function)
    #@parameter money_played     -> the money played
    #@parameter bets_types_list  -> a list of played bets type (refer to BetType class)
    #@parameter is_all_city      -> True if the winning is on all city, False if not
    #
    #@return gross_win and net_win tuple
    #
    @staticmethod
    def _calculate_win(numbers_amount, numbers_matching, money_played, bets_types_list,is_all_city):  
        gross_win = 0.0          

        #get the index of all played bets type
        bets_type_index = []
        for element in bets_types_list:
            bets_type_index.append(element.get_bet_type_index())


        #check for each bet type what are the winning combination
        #for example, if you played 4 numbers and you play ambo and quaterna,
        #you win the quaterna and, at the same time, 6 ambo
        combination_lst = []

        #get the winning bets type
        #for example if you play quaterna and cinquina but you take only quaterna
        #this variable is = 3 (in the BetType class, 3 is the index of quaterna)
        if numbers_matching == 1:
            win_bets_type = bets_type_index[0:1] 
        else:
            win_bets_type = bets_type_index[0:numbers_matching-1] #-1 because index starts from 0!
        

        #add all combination to combination_lst
        for bet in win_bets_type:
            combination_lst.append(Extraction.winning_combination_table[numbers_matching][bet])
        
        #calculate money win for each combination for a played of 1€
        for ind, multiplier in enumerate(combination_lst):
            gross_win += multiplier * Extraction.gross_winning_money_table[numbers_amount][bets_type_index[ind]]

        #moltiplicate the win for the money played 
        gross_win = gross_win * money_played

        #round the win to two decimal number
        gross_win = round(gross_win,2)
        
        #if are played on all city, the win need to be divided by 10 
        if is_all_city:
            gross_win = gross_win / 10

        #cannot win more than € 6.000.000
        if gross_win > 6000000:
            gross_win = 6000000

        #calculate the net win
        net_win = Extraction._calculate_net_win(gross_win)

        return (gross_win,net_win)


    #If the win is other 500€, i need to apply a tax of 8%
    #So if the win are other 500, it return the net win
    @staticmethod
    def _calculate_net_win(money):
        if money > 500:
            WITHHOLDIN_TAX = 0.08 # 8%
            tax = money * WITHHOLDIN_TAX
            return (money - tax)
        else:
            return money



    #return a str of extraction
    def __str__(self):
        return_str = "" 
        for city,value in self.extraction.items():
            city_name = City.get_city_name_by_index(city)

            return_str += "{:8}: ".format(city_name)
            for num in value:
                return_str += "{:2d}  ".format(num)
            return_str += "\n"

        return return_str
