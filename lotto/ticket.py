from random import randrange

class Ticket():
    def __init__(self,city, bets_type_list, numbers_amount):

        self.city = city #city

        self.bets_type_list = bets_type_list #list(bet_type)

        #check numbers amount validity
        if Ticket.is_number_amount_allowed(bets_type_list,numbers_amount):
            self.numbers_amount = numbers_amount
            self.numbers = Ticket._generate_numbers(self.numbers_amount)
        else:
            raise ValueError("The number amount is not coerent with the bet type list!")
    

    def __str__(self):
        return_str = "City: {0}\n".format(self.city.get_city_name())

        #print bet
        return_str += "Bet: "
        for bet in self.bets_type_list:
            return_str += bet.get_bet_type_name() + ", "
        #remove last ", " from end string
        return_str = return_str[0:-2]
        return_str += "\n"

        #print numbers
        return_str += ""
        for number in self.numbers:
            return_str += str(number) + " "
        return_str += "\n"

        return return_str

            

    #private method
    #Generate random numbers for the ticket
    #@return -> a list with generate numbers
    @staticmethod
    def _generate_numbers(number_amount):
        #get the max number to generate
        number_list = []
        for _ in range(number_amount):
            #generate a random number between 1-90
            number = randrange(1,91)
                        
            #check if the number is already in the extracted numbers
            while True:
                if number in number_list:
                    number = randrange(1,91)
                else:
                    break

            number_list.append(number)
        
        return number_list

    @staticmethod
    def is_number_amount_allowed(bets_type_list, number_amount):
        min_bet_type = Ticket.get_minimum_number_amount(bets_type_list)

        if number_amount >= min_bet_type and number_amount <=10:
            return True
        else:
            return False

    @staticmethod
    #get the minimum number to play for the selected bet types
    def get_minimum_number_amount(bets_type_list):
        min_bet_type = 0
        #check in all the bets types what is the minimum number to play
        for bet in bets_type_list:
            if bet.get_bet_type_index()+1 > min_bet_type:
                min_bet_type = bet.get_bet_type_index()+1
        return min_bet_type