[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try) 
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
# Artificial Neural Networks and Deep Learning Projects (A.A. 2019/2020)

**Authors**: Francesco **Alongi**, Gerlando **Re**.

This repository contains the projects for the Artificial Neural Networks and Deep Learning Course. For all these projects we used Tensorflow 2.1.0 (all requirements are listed in the ``requirements.txt`` file). </br>

### Project #1: Image Classification Network

The first project was an __Object Recognition__ challenge in which we had to build a CNN classifier. The dataset was composed of images representing 20 different types of objects (airplanes, bulbs...) also with an unbalancement in number of samples.

### Project #2: Image Segmentation Network

The second project had the purpose of getting acquainted with the __Image Segmentation__ problem, which consists in selecting the pixel space within the image in which a specific object "lies". For this network we did some litterature research in order to study effective models to solve the problems (_U-net_ etc.). For this challenge we used a simpler version of the Oxford IIIT-Pet dataset [https://www.robots.ox.ac.uk/~vgg/data/pets/], where the recognition targets are some animals and the dataset also contains the _mask_ to be applied to the image in order to select the animal shape inside the image.

### Project #3: Visual Question Answering Network

The third and last challenge was a Visual Question Answering challenge, with the purpose of building a model that could intertwine both a CNN and an RNN. The challenge constisted of answering to some questions about a particular image, selecting the answer among 13 possible predefined answers. For this challenge a simpler version of the CLEVR dataset was used [https://cs.stanford.edu/people/jcjohns/clevr/]. </br>
Also for this challenge we had to explore the litterature in order to find a model that could adapt to our problem and could give us a good performance. Also the special side of the challenge was to mix a network for the feature extraction of the image with a recurrent neural network for text prediction.
