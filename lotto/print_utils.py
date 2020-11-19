#Custom module used for generate a visual representation of ticket

class PrintUtils():
    _MAX_TERMINAL_LINE_LENGHT = 35

    #print a table horizontal line seperator
    #ex:
    #    "+-----------+"
    @staticmethod
    def print_horizontal_line_separator():
        print("+{:-<33}+".format('-'))

    #print a table row
    #ex. 
    #    +--------+
    #    +  line  +
    #    +--------+
    #@params "line" -> the line to print
    #@params "align"-> the alignment mode
    #           0 = left
    #           1 = center
    #           2 = right
    @staticmethod
    def print_table_row(line, align = 0):
        PrintUtils.print_horizontal_line_separator()
        PrintUtils.print_line(line,align)
        PrintUtils.print_horizontal_line_separator()

    #print a custom table line
    #ex. 
    #    +  line   +
    #@params "line" -> the line to print
    #@params "align"-> the alignment mode
    #           0 = left
    #           1 = center
    #           2 = right
    @staticmethod
    def print_line(line, align = 0):
        #align left
        if align == 0:
            print("+ {:31} +".format(line))

        #center align
        elif align == 1:
           print("+ {:^31} +".format(line))
        
        #right align
        elif align == 2:
            print("+ {:>31} +".format(line))

        #align parameter not valid
        else:
            raise ValueError("Align parameter is not valid!")

    #print ticket header line
    @staticmethod
    def print_header_line(text):
        PrintUtils.print_table_row(text,1)

    #print ticket footer line
    @staticmethod
    def print_footer_line(text):
        PrintUtils.print_table_row(text,1)