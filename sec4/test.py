from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import time

X, y = fetch_openml('mnist_784',version=1, return_X_y=True)

TRAIN_SIZE = 60000
TEST_SIZE = 10000

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=TRAIN_SIZE, test_size=TEST_SIZE)
print("訓練用データ:", X_train.shape)
print("テスト用データ:", X_test.shape)

start_time = time.perf_counter()
clf = joblib.load("sample2.pkl")    #モデルの読み込み

execution_time = time.perf_counter() - start_time
print(execution_time, "秒") 

predict = clf.predict(X_test)

print("正解率", accuracy_score(y_test, predict)*100 , "%")