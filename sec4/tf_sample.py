import tensorflow as tf    #TensorFlowのインポート
from tensorflow.examples.tutorials.mnist import input_data    #データの取得
import time    #時間を測る

# データの取得
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# モデルの定義
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 後からロードする正解データ（画像とラベル）の格納変数
y_ = tf.placeholder(tf.float32, [None, 10])

# 交差エントロピーの定義
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# 訓練方法の定義
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 学習の準備
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

start_time = time.perf_counter()

# 学習
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_:batch_ys})

# 時間を測る
execution_time = time.perf_counter() - start_time
print(execution_time, "秒") 

# 学習済みモデルの保存
saver = tf.train.Saver()
saver.save(sess, "./model/tf_model")

# テスト
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))

# テスト結果をみてみる
y_label, z_label = sess.run((tf.argmax(y,1), tf.argmax(y_,1)), feed_dict = {x: mnist.test.images, y_:mnist.test.labels})

count = [[0 for i in range(10)] for j in range(10)]
for i, j in zip(y_label, z_label):
    count[i][j] += 1
print("正解", end = "")
for i in range(10):
    print("   [{0}]".format(i), end="")
print()
for i in range(10):
    print("予測[{0}]".format(i), end="")
    for j in range(10):
        print("{0:6d}".format(count[i][j]), end="")
    print()

# 正解率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("正解率", sess.run(accuracy, feed_dict={x: mnist.test.images, y_:mnist.test.labels})*100 , "%")