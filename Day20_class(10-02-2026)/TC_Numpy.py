import numpy as np
import pandas as pd

arr = np.array([10,20,3,30,400])
print("array: ",arr)
print("sum: ",np.sum(arr))
print("mean: ",np.mean(arr))
print("multiply by 2: ",np.multiply(arr,2))

data = {
    "Name":["abhi","varma","krishna"],
    "Age":[21,22,23],
    "City":["Bangalore","Chennai","Hyderabad"]

}

df = pd.DataFrame(data)
print(df)
print(df["City"])

print(df[df["Age"]>21])

df["salary"] = [50000,30000,40000]
print(df)