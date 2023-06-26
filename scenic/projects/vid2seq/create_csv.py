import pandas as pd

list_of_str = ['a woman is talking with a man', 'woman touches her belly', 'woman writes down']
list_of_start = [0,19000,46000]
list_of_end = [57000,20000,54000]
df = pd.DataFrame(zip(list_of_str, list_of_start, list_of_end), columns = ["caption", "start", "end"])
df.to_csv("example.csv", index=None)