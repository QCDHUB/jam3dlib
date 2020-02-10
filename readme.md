[![jamlogo](logos/jam.jpg)]

# JAM3DLIB

## List of Fits

|Reference|   tag    |   Data Included  |   Functions Extracted       |
|---------|----------|------------------|-----------------------------|
|arXiv... |JAM3D_2020|SIDIS, SIA, DY, pp|Sivers, transversity, Collins|


## Installation

### clone the repo

 ```git clone --recursive git@github.com:JeffersonLab/jam3dlib.git```

### prepare a jam python environment (python2)

- Download anaconda2 or anaconda3 into your system

- Create an environment

  ```conda create --name jam python=2.7```

- Activate the environment

  ```conda activate jam ###for conda 4.6 or later```

  or

  ```source activate jam ###for conda versions earlier than 4.6```

- Install subprocess32

  ```conda install subprocess32```

- Install all the dependencies

  ```pip install -r dependencies```


## Getting started

Source the setup

```source setup.bash```

We have provided two files in the repo with simple
examples to evaluate the TMD and CT3 PDFs/FFs

- example.py: bare-bones template python file

- example.ipynb: more detailed example jupyter notebook



## Authors

- Justin Cammarota

- Leonard Gamberg

- Zhong-Bo Kang

- Joshua A. Miller

- Daniel Pitonyak

- Alexei Prokudin

- Ted C. Rogers

- Nobuo Sato



## Institutions

![logo](logos/lvc.jpg)
![logo](logos/psu.png)
![logo](logos/odu.png)
![logo](logos/jlab.png)

...
