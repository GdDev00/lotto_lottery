#Custom module used for generate a visual representation of ticket

class PrintUtils():
    _MAX_TERMINAL_LINE_LENGHT = 51

    #print a table horizontal line seperator
    #ex:
    #    "+-----------+"
    @staticmethod
    def print_horizontal_line_separator():
        print("+{:-<53}+".format('-'))


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
        sub_lines = []

        if len(line) > PrintUtils._MAX_TERMINAL_LINE_LENGHT:
            words = line.split()
            s = ""
            for key, word in enumerate(words):
                if len(s)  + len(word) + 1 < PrintUtils._MAX_TERMINAL_LINE_LENGHT:
                    s = s + word + " "
                else:
                    sub_lines.append(s)
                    s = word + " "

            sub_lines.append(s)
        else:
            sub_lines.append(line)


        for element in sub_lines:
            #align left
            if align == 0:
                print("+ {:51} +".format(element))        
            #align center
            elif align == 1:
                print("+ {:^51} +".format(element))

            #align right
            elif align == 2:
                print("+ {:>51} +".format(element))
            
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