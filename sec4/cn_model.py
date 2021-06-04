import tensorflow as tf

def dl(x):

        # サイズ変更　整形
	x_img = tf.reshape(x,[-1,28,28,1])  

	# 畳み込み層1
	W_conv1 = tf.Variable(tf.truncated_normal([5,5,1,32], stddev=0.1))     
	conv1 = tf.nn.conv2d(x_img, W_conv1, strides=[1,1,1,1], padding='SAME')
	b_conv1 = tf.Variable(tf.constant(0.1, shape=[32]))
	h_conv1 = tf.nn.relu(conv1+b_conv1)              

	#プーリング層1
	h_pool1 = tf.nn.max_pool(h_conv1, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

	#畳み込み層2
	W_conv2 = tf.Variable(tf.truncated_normal([5,5,32,64], stddev=0.1))
	conv2 = tf.nn.conv2d(h_pool1, W_conv2, strides=[1,1,1,1], padding='SAME')
	b_conv2 = tf.Variable(tf.constant(0.1, shape=[64]))
	h_conv2 = tf.nn.relu(conv2+b_conv2)

	#プーリング層2
	h_pool2 = tf.nn.max_pool(h_conv2, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

	#畳み込まれているものをフラットな形に変換
	h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])

	#全結合層
	w_fc1 = tf.Variable(tf.truncated_normal([7*7*64, 1024], stddev=0.1))
	b_fc1 = tf.Variable(tf.constant(0.1, shape=[1024]))
	h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)

        # ドロップアウト率
	keep_prob = tf.placeholder(tf.float32)  
	out_drop = tf.nn.dropout(h_fc1, keep_prob) 

	#出力層
	W_fc2 = tf.Variable(tf.truncated_normal([1024, 10], stddev=0.1))
	b_fc2 = tf.Variable(tf.constant(0.1, shape=[10]))
	out = tf.nn.softmax(tf.matmul(h_fc1, W_fc2) + b_fc2)
	return out, keep_prob