# Image Segmentation Project

This project purpose was to solve an Image Segmentation problem with the [Oxford IIT-Pet dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/). The problem is to select the pixels 
in which a given subject lies within the image, in this way the model selects a labeled area inside of it. An example is given in the picture below.

![segmentation-example](https://www.robots.ox.ac.uk/~vgg/data/pets/pet_annotations.jpg)

## Dataset Structure

The dataset at our disposal had the following structure:

* __Image size__: variable.
* __Color space__: RGB/Grayscale.
* __File format__: JPG.
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

