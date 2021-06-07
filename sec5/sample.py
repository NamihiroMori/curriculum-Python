import pandas as pd
import matplotlib.pyplot as plt

def query_bot(hoge, max_rows=5, **option):
    df = pd.read_excel(hoge, **option)
    df['名前'] = df['名前'].str.replace('\u3000', ' ')
    with pd.option_context('display.max_rows', max_rows):
        while x := input('> '):
            try:
                result = df.query(x)
                print(result)
            except:
                print('クエリを正しくしてください')

# names = ['名前', 'クラス', '部活', '実施月', '英語']
# df = pd.read_excel('./Pandas英語の成績.xlsx', header=1, names=names)

# # 表記ゆれを解消
# df['名前'] = df['名前'].str.replace('\u3000', ' ')

# # 片方しか試験を受けていない生徒を表示
# rt = df.groupby('名前').英語.count()
# result = rt[rt < 2].index
# print(result)

# # 部活の有無で英語の点数を比較
# df['部活2'] = df['部活'].isna()
# print(df.groupby('部活2')['英語'].mean())

# # クラス別の英語の点数を算出してグラフ化
# result_class = df.groupby('クラス')['英語'].mean()
# result_class.plot.bar()
# plt.show()

# # 表示
# print(df[:4])

names = ['名前', 'クラス', '部活', '実施月', '英語']
query_bot('Pandas英語の成績.xlsx', header=1, names=names)

