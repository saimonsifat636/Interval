import pandas as pd

pd.options.display.max_rows=999
data=pd.read_csv('data.csv')
print(data,'\n\n')
pop=data.dropna()   #this will remove all the row that has no element and give a new dataframe. If we don't want new dataframe we can use "inplace = True "........... which will change the original data
# pop=data.dropna(inplace=True) 

print(pop)

#  if we don't want to lose our row then we can use ........"fillna(replacible_value,inplace=True)".....
# refill=data.fillna(130,inplace=True)   #-> this will fill all the element that has null value to 130
# print(refill)

#To fill specific col we need to give that col name like ............"fillna(colname:{130})".............
# specific=data.fillna({"Calories":144444444})
# print(specific)


# fillna -> mean
m=data['Calories'].mean()
print('\n\n',m,'\n\n')
data=data.fillna({'Calories':m},inplace=True)
print(data)


# find mode-> most frequent number

freq=data['Calories'].mode()[0,1]
print(freq)