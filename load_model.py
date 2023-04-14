import tensorflow as tf

checkpoint_path = "C:\\Users\\wangy\\Downloads\\scannet200_val.ckpt"

graph = tf.Graph()
with graph.as_default():
    session = tf.session()
    saver =