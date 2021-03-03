# Image Classification Project

This first challenge was an image classification task. In an image classification task the model is provided with an image and it must be able to tell which class the object in the image corresponds to. An example is shown below. </br> </br>
![airplane](https://user-images.githubusercontent.com/19633559/109784924-dbdb5100-7c0b-11eb-9422-94303fe4c14e.jpg)</br>
**Class:** airplane


## Dataset Structure

The dataset at our disposal had the following structure:

* __Image size__: variable.
* __Color space__: RGB/Grayscale.
* __File format__: .jpg
* __Number of classes__: 20 ("owl","lightbulb","sword"...)
* __Number of training images__: 1554.
* __Number of testing images__: 500.

```
.
└── Classification_Dataset
    ├── train
    │   ├── airplanes
    |   |   ├── img_0.jpg
    |   |   ⋮
    |   |   └── img_x.jpg
    ⋮    ⋮
    │   └── wine-bottle
    |       ├── img_0.jpg
    |       ⋮
    |       └── img_y.jpg
    └── test
        ├── test_image_0.jpg
        ⋮
        └── test_image_z.jpg
```

The number of pictures related to each class' folder is different, leading to an unbalancing of the training samples.

## Notebooks/scripts description
* `DatasplitJsonCreate.py` and `ValidationCreation.py` are two auxiliary scripts which define some function useful to create the validation dataset out of the provided training set;
* `CNN_model.ipynb` is the notebook containing the core of the challenge, it creates the validation dataset, it builds and trains the CNN model and generates the predictions.

## Model description
The neural network used is a custom CNN which is implemented using the learning rate scheduler in order to let the loss decrease faster at the beginning and then let it slow down. The structure is the commonly used one for classification task, with some convolutional layers at the beginning in order to extract meaningful features from the images and then a fully connected part used for classification.
