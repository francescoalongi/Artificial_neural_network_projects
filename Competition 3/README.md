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

The dataset were given with the following structure:

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
