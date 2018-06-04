# Dancing Robot

This repository is for the DiscoveryLab Summer project

For project management, I recommend downloading [GitKraken](https://www.gitkraken.com/) (it supports all operating systems).

### Prerequisites

Python 3 and Conda (for Python 3) are the only externals requirement for this: https://www.anaconda.com/download/

### Installing

Once the repository is cloned, enter the repository:

```
cd DancingRobot
```

To open the Conda command prompt window, refer to this [Getting Started page](https://conda.io/docs/user-guide/getting-started.html).

Install the Conda environment via

```
conda env create -f environment.yml
```

Activate the environment via

```
source activate deeplearning-general
```

## Getting Started

After installing the environment, make sure the OpenCV works by running the video capture system:

```
python VideoCapture_HelloWorld.py
```

For Jupyter projects, run JupyterLab with the following command in the repository:

```
source activate deeplearning-general
jupyter lab
```


