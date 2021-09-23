# Species Detection Challenge
Keeping track of animal's movement patterns, habitat utilisation, population demographics, snaring and poaching incidents, breakouts, helps to allocate land management resources, plan restoration efforts and ultimately protect them. An important task of Wild Life Monitoring is detecting the individual species.
In this challenge, you are given a task to classify the given image into one of the 20 categories. <br />

<i>Note: The model will be evaluated on a test set that is not publically available.</i>


## Directory structure
<ul>
  <li><b>Baselines:</b> Contains code and the model
    <ul>
      <li>YOLOv5</li>
      <li>Faster RCNN</li>
    </ul>
  </li>
  <li><b>Dataset:</b> Contains the dataset
    <ul>
      <li>train_images</li>
      <li>val_images</li>
      <li>train_labels</li>
      <li>val_labels</li>
    </ul>
  </li>
</ul>

## Dataset Description
The dataset consists of 11,141 train samples and 1,586 validation samples.  The label distribution in a particular set is essentially non-uniform. A category wise frequency distribution is shown in the chart below:


![distribution](https://user-images.githubusercontent.com/89697711/134514955-0deffe21-7703-4af0-ad60-29b5cc0d0371.png)

<!--![train-set-distribution](https://user-images.githubusercontent.com/89697711/134506331-e51d80bc-1f0e-4c50-bdf9-586269c9c096.png)

![val-set-distribution](https://user-images.githubusercontent.com/89697711/134506335-831bd227-ffbd-4efd-94d9-2ff4ada57786.png)

Train Set Distribution
![Training_Dataset](https://user-images.githubusercontent.com/89697711/134462094-3b0db5ae-516e-486e-b918-51c33125d76d.png)

Validation Set Distribution
![Validation](https://user-images.githubusercontent.com/89697711/134462112-ad4dd01f-6858-4045-963c-88fad8eecfa9.png)
!-->

The structure will primarily contain the details about the feature set, labels, dataset format, etc...

## Get Started
This section will describe how to clone the dataset and run the baseline model shared.

## References
References will go here.
