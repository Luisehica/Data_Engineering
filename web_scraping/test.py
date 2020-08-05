from newspaper_receipe import _remove_new_lines_from_body2
import pandas as pd

text = ['\nThis is a newline.\nThis is another newline','\n this is just one newline']
df = pd.DataFrame(text,index=[0,1])
df.columns = ['body']
df = _remove_new_lines_from_body2(df)
print(df)
