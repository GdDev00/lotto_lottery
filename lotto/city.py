class City:
    ALLOWED_CITIES_DICT = {1:"Bari", 2:"Cagliari", 3:"Firenze", 4:"Genova", 5:"Milano", 6:"Napoli", 7:"Palermo",\
         8:"Roma", 9:"Torino", 10:"Venezia", 11:"Tutte"}

    #Class init method
    def __init__(self, city_index):
        #validate input
        if City.is_city_index_allowed(city_index):
            self._city_index = city_index
        else:
            raise ValueError("City is not valid!")

    #GET METHODS
    def get_city_index(self):
        return self._city_index

    def get_city_name(self):
        return self.ALLOWED_CITIES_DICT[self._city_index]
            
    #Check if a city index is allowed
    #@parameter city_index -> the city index to check
    #@return -> True if the index exists
    #        -> False if not
    @staticmethod
    def is_city_index_allowed(city_index):
        if isinstance(city_index,int):
            if city_index in City.ALLOWED_CITIES_DICT.keys():
                return True

        return False


    #Return city index by the city name
    #@parameter city name -> city name to find
    #@return -> city numerical index
    #@       -> if the city isn't fount, it returns -1
    @staticmethod
    def get_city_index_by_name(city_name):
        if isinstance(city_name,str):          
            city_name = city_name.strip()
            city_name = city_name.capitalize()

            for key,value in City.ALLOWED_CITIES_DICT.items():
                if value == city_name:
                    return key
        
        return -1



    #Return city name by its numerical index
    #@parameter city_index -> numerical city index to find
    #@return -> city name, empty string if the index is not found
    @staticmethod
    def get_city_name_by_index(city_index):
        if City.is_city_index_allowed(city_index) == True:
            return City.ALLOWED_CITIES_DICT[city_index]
        else:
            return ""