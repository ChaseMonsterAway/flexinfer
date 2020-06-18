# Flexinfer
A flexible Python front-end inference SDK.

## Features
- Flexible
  
  Flexinfer is has a Python front-end, which makes it easy to build a computer vision product prototype.

- Efficient
  
  Most of time consuming part of Flexinfer is powered by C++ or CUDA, so Flexinfer is also efficient. If you are really hungry for efficiency and don't mind the trouble of C++, you can refer to [Cheetahinfer](https://github.com/Media-Smart/cheetahinfer).

## License
This project is released under [Apache 2.0 license](https://github.com/Media-Smart/flexinfer/blob/master/LICENSE).

## Installation
### Requirements

- Linux
- Python 3.6 or higher
- TensorRT 7.0.0.11 or higher
- PyTorch 1.2.0 or higher
- CUDA 9.0 or higher
- volksdep

We have tested the following versions of OS and softwares:

- OS: Ubuntu 16.04.6 LTS
- Python 3.6.9
- TensorRT 7.0.0.11
- PyTorch 1.2.0
- CUDA: 10.2

### Install flexinfer

1. Install volksdep following the [official instructions](https://github.com/Media-Smart/volksdep)

2. If your platform is x86 or x64, you can create a conda virtual environment and activate it.

```shell
conda create -n flexinfer python=3.6.9 -y
conda activate flexinfer
```

3. Clone the flexinfer repository.

```shell
git clone https://github.com/Media-Smart/flexinfer
cd flexinfer
```

4. Install requirements.

```shell
pip install -r requirements.txt
```

## Usage
Here is an example of deploying a classifier, you can run the following statement to classify an image.
```shell
python examples/classifier.py image_file
```
All sample files are in examples directory.

## Contact
