from os.path import join
import numpy as np

epochs = 300
batch_size = 16
image_size = 256
base_dir = '/media/samartht/eb7cc819-496c-4412-85c7-dbf08a6edd2a/dataset/helmet-dataset'
image_dir = 'images'
label_dir = 'labels'
classes = {'helmet':0,'head':1,'person':2}
anchors = np.array([[10, 13], [16, 30], [33, 23],
                    [59, 119], [62, 45], [59, 119],
                    [116, 90], [156, 198], [373, 326]], np.float32)
weights_path = '/media/samartht/eb7cc819-496c-4412-85c7-dbf08a6edd2a/projects/yolov5_tensorflow/weights'
best_weights = 'model168.h5'


