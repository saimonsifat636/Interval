import pandas as pd

    
    
    

data=pd.read_csv('account.csv')
print('\n\n',data,'\n\n')



# print(data.to_string())
print(pd.options.display.max_rows) 


# current situation we can contain maximum 60 row . If rows are greater than 60 ,we will see only 1st and last 5 row.
# to solve this we need to increase the amount of rows and that's how we  can be see all of our data.
pd.options.display.max_rows=9999
print(data) 
print(pd.options.display.max_rows)