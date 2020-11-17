class BetType():
    BET_TYPE_DICT = {1:"Ambata",2:"Ambo",3:"Terna",4:"Quaterna",5:"Cinquina"}

    def __init__(self,type_index):
        #validate input
        if BetType.is_bet_type_allowed(type_index) == True:
            self._type_index = type_index
        else:
            raise ValueError("Bet type is not valid!")

    #GET METHODS
    def get_bet_type_index(self):
        return self._type_index

    def get_bet_type_name(self):
        return self.BET_TYPE_DICT[self._type_index]
    

    #Check if the bet type index is valid
    #@parameter type_index -> the type to find
    #@return True -> if the index is valid
    #@return False-> if the index ISN'T valid
    @staticmethod
    def is_bet_type_allowed(type_index):
        if isinstance(type_index,int):
            if type_index in BetType.BET_TYPE_DICT.keys():
                return True
        
        return False

    #Get bet type name from the index
    #@parameter type_index -> the type index to find
    #@return -> type name
    #@return -> Empty string if the index is not valid
    @staticmethod
    def get_bet_type_name_by_index(type_index):
        if BetType.is_bet_type_allowed(type_index) == True:
            return BetType.BET_TYPE_DICT[type_index]
        else:
            return ""

    #Get bet type index from the bet type name
    #@parmater type_name -> the type name to find
    #@return -> type_index
    #@return -> -1 if the index is not valid
    @staticmethod
    def get_bet_type_index_by_value(type_name):
        if isinstance(type_name,str)==True:
            type_name = type_name.strip()
            type_name = type_name.capitalize()

            for key, value in BetType.BET_TYPE_DICT.items():
                if value == type_name:
                    return key
        
        return -1