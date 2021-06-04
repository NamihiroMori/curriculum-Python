import numpy as np    #画像処理にNumpy配列を扱えるようにするため
from PIL import Image    #画像処理ライブラリ(Pillow)
import sys
import joblib  

#自作のデータを読み込み
image = Image.open("ファイル名")
img_gray = image.convert("L")
img_resize = img_gray.resize((28, 28),Image.LANCZOS)
data = np.array(img_resize)

#自作の画像データを表示させる
for xs in data:
    for x in xs:
        sys.stdout.write('%03d ' % x)
    sys.stdout.write('\n')

#予測
data = [np.array(img_resize).ravel()]
clf = joblib.load("sample2.pkl")
predict = clf.predict(data)
print("予測", int(predict))