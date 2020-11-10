# lotto_lottery
The purpose of the entire project is to create the Italian Lotto game in Python 3.\
For more info check about the game check: https://www.sisal.it/lotto/come-si-gioca .\
For the project purpose, **it completely ignore "ruota nazionale" and the "estratto determinato" play type.**

The project is composed by 4 level. In this branch, it is developed the first level.

* ## Level 1: Lotto Ticket Generator
  Level one of this project requires to develop a lotto ticket generator\
  Software asks how many tickets to generate (1 to max 5), the city (aka Routa), the type of bill and the amount of numbers to generate.\
  It generates random ticket and, as output, it prints a visual representation of a lotto ticket.

  **Example of a visual representation**\
  (one ticket with five numbers in the city of Roma and with Ambo as type of game)
  ```
  +---------------------------------+
  +         Italian Lottery         +
  +---------------------------------+
  +              Ticket             +
  + Routa: ROMA                     +
  + Type: AMBO                      +
  +           --- --- ---           +
  +         28 70 30 25 66          +
  +---------------------------------+
  +            Good Luck!           +
  +---------------------------------+
  ```

  ## Composition
  All the project modules are in *lib* folder:
  * *lotto.py* contains all the main functions and classes;
  * *display_table_lib.py* is a custom module used for generate a visual representation of ticket;
 
  ## How to launch
  From the root folder launch *game.py* in the command line and follow the instructions.
  
