from sklearn.datasets import fetch_openml    #データの取得
from sklearn.model_selection import train_test_split    #データを分割
from sklearn.linear_model import LogisticRegression     #学習
from sklearn.metrics import classification_report   #レポート
from sklearn.metrics import accuracy_score  #正解率
from sklearn.metrics import confusion_matrix  # 混合行列
import joblib    #学習済みモデル保存
import time    #時間を測る

#データの取得
X, y = fetch_openml('mnist_784',version=1, return_X_y=True)

#データの数調整
TRAIN_SIZE = 60000
TEST_SIZE = 10000

#データの分割
X_train, X_test, y_train, y_test = train_test_split( X, y, train_size=TRAIN_SIZE, test_size=TEST_SIZE)
print("訓練用データ:", X_train.shape)
print("テスト用データ:", X_test.shape)

start_time = time.perf_counter()

#学習
clf = LogisticRegression().fit(X_train, y_train)

#時間を測る
execution_time = time.perf_counter() - start_time
print(execution_time, "秒") 

#学習済みモデル保存
joblib.dump(clf, "sample2.pkl",compress=True)

#テスト
predict = clf.predict(X_test)

#レポート
print(classification_report(y_test, predict))

#正解率
print("正解率", accuracy_score(y_test, predict)*100 , "%")

# 混合行列の表示
print(confusion_matrix(y_test, predict))