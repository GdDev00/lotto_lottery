# lotto_lottery
The purpose of the entire project is to create the Italian Lotto game in Python 3.\
For more info check about the game check: https://www.sisal.it/lotto/come-si-gioca .\
For the project purpose, **it completely ignore "ruota nazionale" and the "estratto determinato" play type.**

The project is composed by 4 level. In this branch, it is developed the second level.
* ## Level 2: Lotto Fake Extraction
Level two of this project requires to add a lotto number extraction phase and to check if some of the tickets you generated result winners.
**Example**\
```
+---------------------------------+
+  Italian Lottery - Extraction   +
+---------------------------------+
+ Bari    : 86  21  22  79  58    +
+ Cagliari: 75   2   1  36  34    +
+ Firenze :  7  13  85  23  55    +
+ Genova  : 30  84  27  17  62    +
+ Milano  :  6  19  46  32  82    +
+ Napoli  : 72  28  14  46  54    +
+ Palermo : 30  16  82   9  49    +
+ Roma    : 49  85  46   1  28    +
+ Torino  : 69  65  64  45  44    +
+ Venezia : 45   3  28  65  54    +
+---------------------------------+

+---------------------------------+
+      Ticket 1 is LOSER :(       +
+---------------------------------+
```
Compared to the first level, a class called "extraction" has been added. 
All the business logic functions are enclose into LottoManager class

* ## Level 1: Lotto Ticket Generator
  Level one of this project requires to develop a lotto ticket generator.\
  Software asks how many tickets to generate (1 to max 5), the city (aka Routa), the type of bill and the amount of numbers to generate.\
  It generates random ticket and, as output, it prints a visual representation of this.

  **Example of a visual representation**\
  (one ticket with five numbers in the city of Roma and with Ambo as type of game)
  ```
  +---------------------------------+
  +         Italian Lottery         +
  +---------------------------------+
  +              Ticket             +
  + City: ROMA                      +
  + Type: AMBO                      +
  +           --- --- ---           +
  +         28 70 30 25 66          +
  +---------------------------------+
  +            Good Luck!           +
  +---------------------------------+
  ```

  ## Composition
  All the project modules are in *lotto* folder:
  * *lotto.py* is the business logic of the project;
  * subfolder *lotto* contains all the project classes;
  * *print_utils.py* is a custom module used for generate a visual representation of ticket;
 
  ## How to launch
  From the root folder launch *game.py* in the command line and follow the instructions.
