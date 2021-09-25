# Species Detection Challenge 2021
## Problem Description
The wildlife conservation organizations and governments across the globe have dedicated resources and developed policies to ensure continued biodiversity on our planet. Population monitoring is critical to wildlife conservation. The advancements in the last decade in the computer vision field have shown scope in assisting the conservation efforts as we are able to collect large datasets from camera traps. The aim of this task is to detect species in camera trap images and develop robust systems that can generalize well to different species and across different geographical locations.

![audio-visual-challenge](https://ci4.googleusercontent.com/proxy/pz5n4yxA_iyZw2JaoSJA5ux6cK6k2u6tYPQuE42YHHx_KAzLBgQL-oVBBisTk9Dbk3r1Ln-pAjUy97WJFV6paxwW2MckmqvBin7Tjy5Io7p-I2pXiGL6E8FIj7aQyhBpXwngqHhpVTnFCTtcaLhQ4eBucqznyf8icn-t28kIWWi9e2FD-NTEOgZSdFdhuzLkVHtylMoeob-c8XoAC67Z=s0-d-e1-ft#https://docs.google.com/drawings/d/e/2PACX-1vQjQYbKg6dZZ5o1Q4U1Ty-FiXGgzXf2sUc_l4IoXHSO7BfUmQXiggbO-6h_4jTeI4EvTvXYOnSoxhpY/pub?w=962&h=540)


## Directory structure
- **Baselines:** Contains code and the model
   - YOLOv5
   - Faster-RCNN
- **Dataset:** Contains the dataset
   - train_images
   - val_images
   - train_labels
   - val_labels

## Dataset Statistics
The dataset consists of 11,141 train samples and 1,586 validation samples. The label distribution in a particular set is essentially non-uniform. A category wise frequency distribution is shown in the chart below:


![distribution](https://user-images.githubusercontent.com/89697711/134514955-0deffe21-7703-4af0-ad60-29b5cc0d0371.png)

<!--![train-set-distribution](https://user-images.githubusercontent.com/89697711/134506331-e51d80bc-1f0e-4c50-bdf9-586269c9c096.png)

![val-set-distribution](https://user-images.githubusercontent.com/89697711/134506335-831bd227-ffbd-4efd-94d9-2ff4ada57786.png)

Train Set Distribution
![Training_Dataset](https://user-images.githubusercontent.com/89697711/134462094-3b0db5ae-516e-486e-b918-51c33125d76d.png)

Validation Set Distribution
![Validation](https://user-images.githubusercontent.com/89697711/134462112-ad4dd01f-6858-4045-963c-88fad8eecfa9.png)
!-->

*Note: The model will be evaluated on a test set that is not publically available.*

## Evaluation Metric
***ClassAverage mAP will be used as the evaluation metric. Each retrieval example will produce an average precision (AP) score. Averageing AP for all the query from a particular class will give the mAP for that class. ClassAverage mAP is then obtained by averaging mAP for all the class. ClassAverage Map can be calculated for both audio to video and video to audio retrieval. The final score will be the average of both of them.***

```math
Final mAP = 0.5*(audio2video) + 0.5*(video2audio)
```

## Getting Started
### Downloading the dataset
1. Complete dataset can be downloaded from this [link](https://drive.google.com/drive/folders/1C5c8K0ZkPhzz-RX1qkPgkGejAssSA72v). 
2. Keep the downloaded files in the [```Dataset```](/Datasets) directory as mentioned above.

### Running the baselines
Go to the [```Baselines/YOLOv5```](/Baselines/YOLOv5) or [```Baselines/Faster-RCNN```](/Baselines/Faster-RCNN) sub-directories to get a detailed description to run the respective baseline model.

## Submission
Submit a ***txt*** file with each row specifying the class label index of the ***retrieval results sorted in decreasing order of similarity.***
