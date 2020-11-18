from city import City
from random import randrange

class Extraction:
    def __init__(self):
        self.extraction = Extraction._extract()

    @staticmethod
    def _extract():
        extraction_dict = {}

        for key in range(len(City.ALLOWED_CITIES_DICT)-1):
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
                    
    def __str__(self):
        return_str = "" 
        for city,value in self.extraction.items():
            city_name = City.get_city_name_by_index(city+1)

            return_str += "{:8}: ".format(city_name)
            for num in value:
                return_str += "{:2d}  ".format(num)
            return_str += "\n"

        return return_str