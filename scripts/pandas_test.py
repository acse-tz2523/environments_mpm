import pandas as pd
from envtest import my_pandas_use

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
print(my_pandas_use(data))


