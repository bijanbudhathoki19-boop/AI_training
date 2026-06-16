import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "Salary": [70000, 80000, 65000, 90000],
    "Department": ["HR", "IT", "Finance", "Marketing"]
}

df = pd.DataFrame(data)
print(df)