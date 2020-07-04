import pandas as pd

###DATAFRAME
#this is how you create a dataframe, a table with columns yes and no
x=pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
#print(x)

y=pd.DataFrame({"Helga":["work","play"], "Piero":["study","read"], "Matteo":["cry", "play"] })
#print(y)

# The list of row labels used in a DataFrame
#is known as an Index.
# We can assign values to it by using an index parameter in our constructor
y=pd.DataFrame({"James":["work","play"],
                "Piero":["clean","read"],
                "John":["cry", "play"]},
                index=['bad stuff','nice stuff'])
print(y)
print("")
print("next example")

print("")

####SERIES

serie=pd.Series(["Berto", "Matteo", "Giacomo", "Giovanni", "Antonio"], index=["bravo","triste","felice","mangia","nonesiste"], name="un nome")
print(serie)
