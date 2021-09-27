# Species Detection Challenge - Baselines (YOLOv5)

## Get started

1. First step is to convert the labels into YOLO format. Run the following script for this purpose:
```
**Baselines/YOLOv5:** python create_labels.py
```
2. Clone the [YOLOv5]() GitHub repository in the current folder itself.
3. Move _icvgip.yaml_ to ```data``` directory
```
**Baselines/YOLOv5:** mv icvgip.yaml data/
```
4. Open the file ```model/yolov5x.yaml``` in a text editor and change the value of nc to 20.
```
nc: 20
```
5. To start the training, run the following command:
```
**Baselines/YOLOv5:** python train.py --img 640 --cfg ./models/yolov5x.yaml --batch 16 --epochs 100 --data ./data/icvgip.yaml --weights yolov5x.pt --name icvgip --device 0
```

