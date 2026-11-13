import  pandas as pd

data=[100,45,200,1000]
info={"karim":22,"rakim":23,"sahid":21,"kaka":33,"abbas":44}
series=pd.Series(data, index = ["a","b","c","d"])
student=pd.Series(info)
print(series)
print(series.loc["d"])
print(series.loc["a"])  #"loc" -> this for location by label
series.loc['a']=12344
print(series.loc["a"])
#"iloc" -> this for location by integer label(depending on the position it will find them)
print(series.iloc[3])
print(student)