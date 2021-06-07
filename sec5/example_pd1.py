import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('attendance.csv')
ax = df.plot(x='Date', y='OfficeWork', title='Attendances')
df.plot(y='TeleWork', ax=ax)

plt.xlabel('日数', fontname='MS Gothic')
plt.ylabel('人数', fontname='MS Gothic')

plt.show()