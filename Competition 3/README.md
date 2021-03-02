# Visual Question Answering competition 
In this competition, we were asked to solve a VQA problem using a reducted version of the [CLEVR dataset](https://cs.stanford.edu/people/jcjohns/clevr/). 

## Dataset structure
This reducted version of the CLEVR dataset was composed as follows:
* Images:
  * Image size: 320x480 pixels
  * Color space: RGBA
  * File Format: .png
  * Number of training images: 69642
  * Number of test images: 2754
* Questions:
  * Two types of questions: "exist" or "count"
  * Number of training questions: 259492
  * Number of test questions: 3000
* Answers (13 possible answer):
  * '0': 0
  * '1': 1
  * '10': 2
  * '2': 3
  * '3': 4
  * '4': 5
  * '5': 6
  * '6': 7
  * '7': 8
  * '8': 9
  * '9': 10
  * 'no': 11
  * 'yes': 12

The dataset was given with the following structure:

```
.
└── dataset_vqa
    ├── train
    │   ├── CLEVR_train_x.png
    ⋮    ...
    │   └── CLEVR_train_y.png
    ├── test
    │   ├── CLEVR_val_x.png
    ⋮    ...
    │   └── CLEVR_val_y.png
    ├── train_data.json
    └── test_data.json
```
where the `train_data.json` and `test_data.json` are composed of dictionaries with the following structure:

```
{
 'question': ...,
 'image_filename': ..., 
 'answer': ...
}
```

## Notebooks description
* `ValSplit.ipynb`: this notebook has been used to create a `valid_data.json` with some random images chosen from the train folder. It has been decided to take from the initial training set 90% of the images and kept them for the actual dataset used for training the model, the remaining 10% have been used for the validation set;
* `FeaturesExtractor.ipynb`: this notebook was built mainly for computational efficiency. In order to speed up the training process, we decided to statically extract the features of the images before the actual training phase of the main model. The model used for extracting the features is a VGG19, which have been used without performing any fine-tuning;
* `VQA_model.ipynb`: this notebook contain the core of the competition solution.

## Model Description
For the final solution we decided to extract features from every image in the dataset using a pre-trained VGG19 network and using global average pooling in order to obtain a feature vector with length equal to 512. Then we created a custom data generator that for every entry in the dataset (training, validation or testing) returns a batch of list composed of the tokenized question, the feature vector corresponding to the image and the target (if not in testing mode). The tokenized question was fed to a RNN with two LSTMs Bidirectional layers. The output of the RNN and the feature vector (coming out from the generator) go through two separate dense layers, successively merged using a Concatenate layer. Then a fully connected network does the classification over the 13 classes.

<img src="https://user-images.githubusercontent.com/19633559/109685522-a1c56d00-7b81-11eb-89d1-c184b846cc96.jpg" width=600>


