# Image Segmentation Project

This project purpose was to solve an Image Segmentation problem with some satellite images picturing buildings and roads. The problem is to select the pixels 
in which a given subject lies within the image, in this way the model selects a labeled area inside of it. An example is given in the picture below.

![inbox_3311561_229e83d6163165828b175edc5f1a2b5e_71](https://user-images.githubusercontent.com/19633559/109698049-3e423c00-7b8f-11eb-93db-9247db32562a.png)
![inbox_3311561_14527a461492c2a3711f4c6993e372ea_71_mask](https://user-images.githubusercontent.com/19633559/109698060-413d2c80-7b8f-11eb-82a5-10b33c7a2ed7.png)

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
## Notebook Description
``ValSetCreation.ipynb``: This notebook is used in order to build the JSON file that is used in order to extract the validation set from the training data. 
``U-Net-style-model.ipynb``: This is the main notebook, where we implemented a U-Net-like structure for the model.

## Model Description
We built a U-Net like structure, using _skipping connections_ implemented through ``Concatenate`` layers keeping the data augmentation low. The U-Net-like structure has been explored in various settings: the number of filters, the depth of the network and the number of ``Conv2D`` layers in each macro-layer of the U-Net have been perturbed various times before obtaining a validation loss around 0.24 with a IoU (_Intersection over Union_) metric of about 76%. On Kaggle we scored a 0.54 accuracy, pretty consistent with the  results on the validation IoU. A possible improvement is to use a Jaccard loss for the training.




