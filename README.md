This repository contains code to analyze HCR confocal microscopy data. 

#### Enivronment setup

1. Create a new environment
```
conda create -n mfish python=3.8
conda activate mfish
```


2. Install libraries
```
pip install scikit-image jupyterlab seaborn pandas numpy matplotlib scikit-learn scipy toml
pip install plotly
pip install cellpose
pip install napari[all]
pip install -e .
```

#### Contact

Polina Kosillo