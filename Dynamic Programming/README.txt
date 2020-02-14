Shopping Spree
By Aurora Weiden
Due Date: July 15th, 2019

For shopping.py the user only needs to run "python shopping.py" in the command line and have a shopping.txt file of the correct
format in their directory

shopping.py:
- readInFile function takes in a file called shopping.txt and empty arrays for the price of each item, 
    weight of each item, and weight capacity of each family member
- Fills empty arrays of the price of each item, weight of each item, and weight capacity of each family member 
    for each test case
- For each test case shoppingSpree uses arrays filled in readInFile and the family member with the max weight capacity to create an OPT
- Results takes in the table made in shoppingSpree as well as the other parameters taken in by shoppingSpree to write "results.txt", 
    which tells you the total price accumulated, and which items each family member got (in reverse order)