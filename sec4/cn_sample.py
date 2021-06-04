import tensorflow as tf    # TensorFlowのインポート
from tensorflow.examples.tutorials.mnist import input_data # データの取得
import time    # 時間を測る
import cn_model     # モデルを構築したプログラムを利用するためにインポート

# データの読み込み
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])   
y_ = tf.placeholder(tf.float32, [None, 10])   
y,keep_prob = cn_model.dl(x)

#誤差関数（クロスエントロピー）
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

# 訓練方法の定義
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# テスト
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))

# 正解率
ac = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 学習の準備
init = tf.global_variables_initializer()  # データの初期化
sess = tf.Session()       # セッション(tensorflowの計算)を開始する
sess.run(init)   # セッションを実行する(initを実行する)

# 学習時間測るため
start_time = time.perf_counter()

# 学習
for _ in range(1000):
    bs, b_y = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: bs, y_:b_y, keep_prob: 0.5})
    if _ % 200 == 0:
        accuracy = sess.run(ac, feed_dict={x: bs, y_:b_y, keep_prob: 0.5})
        print("ステップ{0:5d}, 正解率{1:6.2f}%" .format(_, accuracy*100))

# 学習時間測るため
execution_time = time.perf_counter() - start_time
print(execution_time, "秒")

# 学習済みモデルの保存
saver = tf.train.Saver()
saver.save(sess, "./model/cn_model")

# 正解率
accuracy = sess.run(ac, feed_dict={x: mnist.test.images, y_:mnist.test.labels, keep_prob: 1.0})
print("正解率", accuracy*100 , "%")