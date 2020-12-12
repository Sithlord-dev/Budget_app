Here is a little function that instantiate objects based on different budget categories like *food*, *clothing*, and *entertainment*. It comes along with a class that has the following methods: 
   * `deposit` : accepts an amount and description. 
   * `withdraw` : similar to the `deposit`.
   * `get_balance` : returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
   * `transfer` : accepts an amount and another budget category as arguments.
   * `check_funds` : accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` 
                     otherwise.

When the budget object is printed it displays:
   * A title line of 30 characters where the name of the category is centered in a line of `*` characters.
   * A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then
     the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
   * A line displaying the category total.

Here is an example of the output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the `Category` class, a function `create_spend_chart` that takes a list of categories as an argument and returns a bar chart with the percentage spent in each category passed in to the function. Here is an example:
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

This was a project exercise in Freecodecamp.org.
