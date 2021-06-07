import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('attendance.csv', encoding='utf_8')

# count = df.groupby('Name').sum()
# print(count['Price'])

# df['BMI'] = df['Weight'] / (df['Height'] ** 2)

# print(df)

# plt.rcParams['font.family'] = 'TakaoGothic'
# df[['BMI']].plot.bar()
# plt.xticks(df.index, df.Name, fontname="MS Gothic")

# plt.show()

# -------------------
df = pd.read_csv('./attendance.csv', encoding='utf_8')

df.plot()
plt.show()


