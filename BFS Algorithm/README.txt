Wrestler
By Aurora Weiden
Due Date: July 29th, 2019

For wrester.py the user  needs to run "python wrestler.py" in the command line.  The user must go into the code and at the top of
the program the user can change what document is read in (under #user can change this field).  The file must be in the correct format.

The program then runs readInFile to extract the necessary info from  the document and make a dictionary of sets where the key in the 
wrestler and the names in the set are those that the reference wrestler has a rivilary with.  

The dictionary of sets is then run through BFS with rivarly sorting for the first key and subsequently for any wrestlers that are disjoint 
from the first run wrestler.