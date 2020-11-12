_MAX_TERMINAL_LINE_LENGHT = 35

class PrintUtils():

    #print a table horizontal line seperator
    #ex:
    #    "+-----------+"
    @staticmethod
    def print_horizontal_line_separator():
        print("+",end="")    
        for _ in range(_MAX_TERMINAL_LINE_LENGHT-2):
            print("-",end="")
        print("+")


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
            print("+",end=" ")

            if len(line)> _MAX_TERMINAL_LINE_LENGHT:
                print(line,end="")
            else:
                newLine = line

                #add right spaces 
                while len(newLine)<_MAX_TERMINAL_LINE_LENGHT-3:
                    newLine += " "

                print(newLine,end="")

            print("+")
        
        #align center
        elif align == 1:
            print("+",end="")

            if(len(line) > _MAX_TERMINAL_LINE_LENGHT):
                print(line,end="")
            else:        
                # calculate the number of left spaces
                left_spaces = ((_MAX_TERMINAL_LINE_LENGHT-1-len(line))//2)

                #add left spaces
                newLine = " " * left_spaces

                newLine += line

                #add the right spaces
                while (len(newLine)<_MAX_TERMINAL_LINE_LENGHT-2):
                    newLine += " "

                print(newLine,end="")

            print("+")

        #align right
        elif align == 2:
            print("+",end="")
            
            if len(line)>_MAX_TERMINAL_LINE_LENGHT:
                print(line)
            else:
                n_of_spaces = _MAX_TERMINAL_LINE_LENGHT-len(line)-2
                newLine = " " * n_of_spaces
                newLine += line
                print(newLine,end="")
            print("+")
        
        #align parameter not valid
        else:
            raise ValueError("Align parameter is not valid!")

    #print ticket header line
    @staticmethod
    def print_ticket_header_line():
        PrintUtils.print_table_row("Italian Lottery",1)

    #print ticket footer line
    @staticmethod
    def print_ticket_footer_line():
        PrintUtils.print_table_row("Good Luck!",1)