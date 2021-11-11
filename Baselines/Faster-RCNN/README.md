# Species Detection Challenge - Baselines (Faster-RCNN)

1. The main code can be referred from this link: [```main.ipynb```](https://github.com/ICVGIP-Challenge/SpeciesDetection-21/blob/main/Baselines/Faster-RCNN/main.ipynb)
2. The changes (registering our dataset in COCO format) that we made in the above file is motivated by this [link](https://detectron2.readthedocs.io/en/latest/tutorials/datasets.html)
3. **Registering the dataset:** After installing all the dependencies, the main task is to register the dataset which is done by considering the ‘JSON’ files. After setting up the file paths, just run the ‘Creating dataset’ tab.
4. **Training:** In the ‘Training Procedure’ tab change the model ‘.yaml’ file to ‘COCO-Detection/faster_rcnn_R_50_C4_1x.yaml’
5. Other hyper-parameters are kept the same as the default.
6. **Evaluation:** This can be done by running the “Evaluate on validation set” tab.
7. **Visualisations:** Run “Check result of model on image” tab.

***NOTE: You can change the names of the tab according to your relevancy and update here too.***
