import parser
import pandas as pd

a, columns = parser.get_data()
data = pd.DataFrame(data=a).transpose()
data.columns = columns
print(data)
data.to_excel("keymap.xls")
