from random import randrange

class Ticket():
    def __init__(self,city, bets_type_list, numbers_amount, money):

        self._city = city #city

        self._bets_type_list = bets_type_list #list(bet_type)

        #check numbers amount validity
        if Ticket.is_number_amount_allowed(bets_type_list,numbers_amount):
            self._numbers_amount = numbers_amount
            self._numbers = Ticket._generate_numbers(self._numbers_amount)
        else:
            raise ValueError("The number amount is not coerent with the bet type list!")

        #check money validity
        if Ticket.is_money_allowed(money):
            self._money = money
        else:
            raise ValueError("Money are incorrect!")
    
    def get_city(self):
        return self._city

    def get_numbers(self):
        return self._numbers   

    def get_bets_type(self):
        return self._bets_type_list
    
    def get_money(self):
        return self._money

    def __str__(self):
        #print city
        return_str = "City: {0}\n".format(self._city.get_city_name())

        #print bet
        return_str += "Bet type: "
        for bet in self._bets_type_list:
            return_str += bet.get_bet_type_name() + ", "
        #remove last ", " from end string
        return_str = return_str[0:-2]
        return_str += "\n"

        #print money
        return_str += "Bet money: {}€\n".format(self._money)

        #print numbers
        return_str += ""
        for number in self._numbers:
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
        
        return sorted(number_list)

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

    @staticmethod
    def is_money_allowed(money):
        if isinstance(money, float):
            if money >= 1.00 and money <=200.00:
                if money % 0.50 == 0: #money are a multiple of 0.50 cents
                    return True
        return False