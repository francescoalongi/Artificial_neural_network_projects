# Image Segmentation Project

This project purpose was to solve an Image Segmentation problem with the [Oxford IIT-Pet dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/). The problem is to select the pixels 
in which a given subject lies within the image, in this way the model selects a labeled area inside of it. An example is given in the picture below.

![segmentation-example](https://www.robots.ox.ac.uk/~vgg/data/pets/pet_annotations.jpg)

## Dataset Structure

The dataset at our disposal had the following structure:

* __Image size__: 256x256 pixels.
* __Color space__: RGB.
* __File format__: tif.
* __Number of classes__: 2.
  * _'background'_ : 0.
  * _'building'_ : 1 (corresponding to the value 255 in the stored masks).
* __Number of training images__: 7647.
* __Number of testing images__: 1234.

```
.
└── Classification_Dataset
    ├── train
    │   ├── images
    |   |   ├── img_0.tif
    |   |   ⋮
    |   |   └── img_x.tif
    │   └── masks
    |       ├── mask_0.tif
    |       ⋮
    |       └── maks_x.tif
    └── test
        ├── test_image_0.tif
        ⋮
        └── test_image_z.tif
```
