from city import City
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

    #check if some numbers are in the corrispective city index
    #@return -> the number of matching numbers
    #@return -1 if the parameter are not valid!
    def check_matching_number(self, city_index, numbers_to_check):
        #check parameter
        if City.is_city_index_allowed(city_index) == False or \
            isinstance(numbers_to_check,list) == False:
            return -1

        matching_number_count = 0

        # check if the city is "Tutte"
        tutte_index = City.get_city_index_by_name("Tutte")
        if city_index == tutte_index:
            for tck_val in numbers_to_check:
                for key, extract_value in self.extraction.items():
                    if tck_val in extract_value:
                        matching_number_count+=1

        #city isn't "Tutte"
        else:
            for tck_val in numbers_to_check:
                if tck_val in self.extraction[city_index]:
                    matching_number_count+=1

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