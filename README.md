# Yolov5-Tensorflow
Train-Yolo-V5 using Tensorflow
[YOLOv5](https://github.com/ultralytics/yolov5) implementation using TensorFlow 2

#### Train
* Run `python generate.py` for generating anchors
* Change anchors and path in `utils\config.py`
* Run `python train.py` for training

#### Test
* Run `python test.py`

#### Dataset structure
    ├── Dataset folder 
        ├── IMAGES
            ├── 1111.jpg
            ├── 2222.jpg
        ├── LABELS
            ├── 1111.xml
            ├── 2222.xml
        ├── train.txt

make sure to copy the XML in Images folder as well. 
#### Note 
* xml file should be in PascalVOC format
* for making `train.txt`, see `VOC2012/ImageSets/Main/train.txt` 

#### Reference
* https://github.com/ultralytics/yolov5
* https://github.com/wizyoung/YOLOv3_TensorFlow
