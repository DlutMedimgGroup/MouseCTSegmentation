# MouseCTSegmentation

## Introduction
This repository is used for segmenting torso organs from mouse micro-CT images.

## Installation

### 3D-CAFFE

Please follow the [instructions](http://caffe.berkeleyvision.org/install_apt.html) to install 3D-CAFFE.

> Notes: Don't forget to build Pycaffe interfaces.

```
make pycaffe && make install # after modify the config file of CAFFE
```

### Python dependencies

The code is developed using python 2.7. Python dependencies are required as follow.

1. SimpleITK

   `pip install SimpleITK`

2. NumPy

   `pip install numpy`

3. H5Py

   `pip install h5py`

## Data preparation

1. CAFFE reads the h5 file to train the network. You need to convert origin formats (e.g. .nii/.nii.gz/.mhd, etc.) to h5 files. We provide a python script`cov_format.py` to convert the format of the files.

2. You need to create a file name list of the dataset named `data.list`. It should look like this:

   ```
   ./id1.h5
   ./id2.h5
   ./id3.h5
   ...
   ```

   

## Usage

1. Put the dataset in the folder.
2. Modify the `data.list` path in the file `train.prototxt`.
3. Train the model.

```
cd MouseCTSegmentation
sh train.sh
```
>Notes: You can specify the numbers of GPU runs in the file train.sh.

4. Segment the images using the model. We also provide pre-trained models in the folder `model`. You can modify the variable `caffe_model` in the file `seg.py` to use them.
```
python seg.py
```




## Contact

Please contact hanascend@foxmail.com if you have any questions.