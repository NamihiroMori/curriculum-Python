import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')

# 直近3日間のデータの定義
x = np.array([0.0, 1.0, 2.0])       # x軸
y1 = np.array([8.00, 10.00, 0.00])   # y軸(勤務時間)
y2 = np.array([3.00, 1.00, 10.00])   # y軸(勉強時間)

# グラフの描画
fig, ax = plt.subplots(1,2, figsize=(8.0, 6.0))

# タイトル
ax[0].set_title('「母里南陽」の直近3日間の勤務時間', fontname='MS Gothic')
ax[1].set_title('「母里南陽」の直近3日間の勉強時間', fontname='MS Gothic')

# データ
ax[0].plot(x, y1, label='time(h)')
ax[1].plot(x, y2, label='time(h)')

# 凡例
ax[0].legend()
ax[1].legend()

# y軸目盛を小数点にする
ax[0].yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))
ax[1].yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))

plt.show()