import pandas as pd

#Question 5
#part 5a
import pandas as pd
ct = pd.read_csv("congress.csv")
#to check heading of data
ct.head(10)
#part 5b 1
#to check rows and columns
ct.shape
#3822 rows, that means there are 3822 observations in this dataset.
#part 5b 2
#to count number of house and senate in "chamber"
chambers = ct[["congress","chamber"]].groupby("chamber").agg("count")
#to change heading to "count"
chambers.columns = ["count"]
chambers.head()
#part 5c
ca = ct[["congress","age"]].groupby("congress").agg("mean")
ca.head(1)
#part 5d
ct[["firstname","lastname","age"]].groupby("age").max()
#the oldest senator in this data is J. Thurmond
