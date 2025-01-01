import pandas as pd
column=["Conan","Goggins","Batman"]
age=[20,49,50]
df=pd.DataFrame(column)
print(df)#prints with column name as 0

#to display a column name for this:
titled_column={"name":column}
df=pd.DataFrame(titled_column)
print(df)

#to display other columns along with data:
new_columns={"name":column,"age":age,"gender":['male','male','male']}
df=pd.DataFrame(new_columns)
print(df)

#to select value from column
select_column=df["age"]#returns entire age column
select_column=df["age"][2]#returns the 3rd element in the age column
print(select_column)

#to select values from row
select_row=df.iloc[1]#returns entire 2nd row
select_row=df.iloc[1]['name']#returns the value of name in the 2nd row
print(select_row)

