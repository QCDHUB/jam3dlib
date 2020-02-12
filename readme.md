![jamlogo](logos/jam.jpg)

# JAM3DLIB

## List of Fits

|Reference|   tag    |   Data Included  |   Functions Extracted       |
|---------|----------|------------------|-----------------------------|
|arXiv... |JAM3D_2020|SIDIS, SIA, DY, pp|Sivers, transversity, Collins|


## Installation

### clone the repo

 ```git clone --recursive git@github.com:JeffersonLab/jam3dlib.git```

 ```cd jam3dlib```

### prepare a jam python environment (python2)

- Download and install anaconda2 or anaconda3 into your system from https://www.anaconda.com/distribution/

- Create an environment

  ```conda create --name jam python=2.7```

- Activate the environment

  ```conda activate jam```

  for conda 4.6 or later

  OR

  ```source activate jam```

  for conda versions earlier than 4.6

- Install subprocess32

  ```conda install subprocess32```

- Install all the dependencies

  ```pip install -r dependencies```


## Getting started

Source the setup

```source setup.bash```

We have provided two files in the repo with simple
examples to evaluate the TMD and CT3 PDFs/FFs

- example.ipynb: detailed example jupyter notebook

```jupyter notebook example.ipynb```

- example.py: bare-bones template python file

```python example.py```



## Authors (Please contact Daniel, Alexei, or Nobuo with questions)

- Justin Cammarota

- Leonard Gamberg

- Zhong-Bo Kang

- Joshua A. Miller

- Daniel Pitonyak (pitonyak@lvc.edu)

- Alexei Prokudin (prokudin@jlab.org)

- Ted C. Rogers

- Nobuo Sato (nsato@jlab.org)



## Institutions

![l](logos/lvc.jpg)
![logo](logos/PSU_BKO_RGB_2C.png)
![logo](logos/odu.png)
![logo](logos/JLab_logo_white1.jpg)
![logo](logos/NSF_4-Color_bitmap_Logo.png)
![logo](logos/RGB_Color-Seal_Green-Mark_SC_Horizontal.png)
