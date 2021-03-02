[![made-with-python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)](https://www.python.org/)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?logo=Jupyter)](https://jupyter.org/try) 
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
# Artificial Neural Networks and Deep Learning Projects (A.A. 2019/2020)

**Authors**: Francesco **Alongi**, Gerlando **Re**.

This repository contains the projects for the Artificial Neural Networks and Deep Learning Course. For all these projects we used Tensorflow 2.1.0 (all requirements are listed in the ``requirements.txt`` file). </br>

### Project #1: Image Classification Network

The first project was an __Object Recognition__ challenge in which we had to build a CNN classifier. The dataset was composed of images representing 20 different types of objects (airplanes, bulbs...) also with an unbalance in the number of samples.

### Project #2: Image Segmentation Network

The second project had the purpose of getting acquainted with the __Image Segmentation__ problem, which consists in selecting the pixel space within the image in which a specific object "lies". For this network we did some literature research in order to study effective models to solve the problems (_U-net_ etc.). For this challenge we used a simpler version of the [Oxford IIIT-Pet dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/), where the recognition targets are some animals and the dataset also contains the _mask_ to be applied to the image in order to select the animal shape inside the image.

### Project #3: Visual Question Answering Network

The third and last challenge was a Visual Question Answering challenge, with the purpose of building a model that could intertwine both a CNN and an RNN. The challenge consisted of answering to some questions about a particular image, selecting the answer among 13 possible predefined answers. For this challenge a simpler version of the [Stanford CLEVR dataset](https://cs.stanford.edu/people/jcjohns/clevr/) was used. </br>
Also for this challenge we had to explore the literature in order to find a model that could adapt to our problem and could give us a good performance. Also the special side of the challenge was to mix a network for the feature extraction of the image with a recurrent neural network for text prediction.
