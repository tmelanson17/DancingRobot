# Dancing Robot

This repository is for the DiscoveryLab Summer project

For project management, I recommend downloading [GitKraken](https://www.gitkraken.com/) (it supports all operating systems).

### Prerequisites

Python 3 and Conda (for Python 3) are the only externals requirement for this: https://www.anaconda.com/download/

### Installing

Open the Anaconda Prompt window (refer to this [Getting Started page](https://conda.io/docs/user-guide/getting-started.html)).

In the Anaconda Prompt window, type

```
cd [/path/to/DancingRobot]
```

Install the Conda environment via

```
conda env create -f environment.yml
```

For Windows, activate the environment via

```
activate deeplearning
```

For Linux / OS X, activate the environment via

```
source activate deeplearning
```


## Getting Started

After installing the environment, make sure the OpenCV works by running the video capture system:

```
python VideoCapture_HelloWorld.py
```

For Jupyter projects, **activate the environment first**, THEN run JupyterLab with the following command in the repository:

```
jupyter lab
```


