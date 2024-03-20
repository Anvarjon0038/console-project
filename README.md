# console-project
This code is a console program for budget management. It allows users to keep track of their income and expenses, as well as view their current balance.

How it works:

1: The user sees the main menu with possible operations: viewing the balance, expenses, income, adding expenses and income, and exiting the program.
2: Data on income and expenses are stored in the lists doxod (income) and rasxod (expenses).
3: The get_balance() function calculates and displays your total income, total expenses, and current balance.
4: The function t(s) measures the execution time of an operation.
5: The p(op) function asks the user for the amount and description of the transaction, then adds this data to the appropriate list (income or expenses) and saves it to a file.
6: The save() function saves income and expense data to the text file "text.txt".
7: The load() function loads data from the "text.txt" file when the program starts.
8: The main program loop prompts you to select an option from a menu and performs the corresponding operation.


This code provides a simple but effective way to manage finances through a console interface.
