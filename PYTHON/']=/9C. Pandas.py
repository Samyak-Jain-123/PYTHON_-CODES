import pandas as pd 

x=pd.Series([1,2,3,4,5]) 
print(x)
print(type(x))                                                      # <class 'pandas.Series'>

y=pd.Series([1,2,3,4,5], index=["a", "b", "c", "d", "e" ]) 
print(y)
print(y.size)                                                       # 5
print(y.index)                                                      # Index(['a', 'b', 'c', 'd', 'e'], dtype='str')
print(y.values)                                                     # [1 2 3 4 5]
print(y.name)                                                       # None


Name=["A", "B", "C", "D", "E"]
Marks=[50,70,60,70,90]

x = pd.Series(Marks, index = Name, name= "Class X Marks")
print(x) 
print(x.name)                                                       # Class X Marks

print(x.max())                                                      # 90
print(x.min())                                                      # 50

print(x.mean())                                                     # 68.0
print(x.median())                                                   # 70.0
print(x.mode())                                                     # 0    70

print(x.var())                                                      # 220.0
print(x.std())                                                      # 14.832396974191326

print(x.count())                                                    # 5


maps = {"A":32,
        "B":78,
        "C":12,
        "D":87}
x = pd.Series(maps)
print(x)

# CSV FILES --> Comma Separted Value Files
df = pd.read_csv('Lecture 9/DATA.csv')
print(df) 
print(type(df))

df = pd.read_csv('Lecture 9/DATA.csv',index_col="S_No").squeeze(True)
print(df) 
print(type(df))

# True --> Boolean Values
# true --> Variable


# Functions used in Series

x=pd.Series([1,1,3,6,4,2,35,7,3,1,3,2])

print(x.head())                             # By default first 5 records
print(x.head(7))

print(x.tail())                             # By default last 5 records
print(x.tail(7)) 

print(x.value_counts())                     #   Displays no of values

print(x.sort_values())
print(x.sort_values(ascending=False))
print(x.sort_values(ascending=False).head(6))
print(x.sort_values(ascending=False).values[0])




#Practise 1 
Name=["A", "B", "C", "D", "E"]
Marks=[50,60,70,80,90]

x = pd.Series(Marks, index = Name, name= "Class X Marks")
print(x, x.name)

print("MARKS OF B: ", x["B"])

print("AVG MARKS OF CLASS: ",x.mean())

print(x.sort_values(ascending=False).head(1),print("TOPPER"))
