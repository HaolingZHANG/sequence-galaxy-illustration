# Visual claims of the paper "Toward a formal cartography of protein function"

## Preparation 

You may clone this code repository (using the following command line) or 
just [download](https://codeload.github.com/HaolingZHANG/sequence-galaxy-illustration/zip/refs/heads/main) 
this code repository with the ZIP format.

```shell
git clone https://github.com/HaolingZHANG/sequence-galaxy-illustration.git
```

To complete the data generation and visualization, 
please install the following dependencies using 
[conda](https://www.anaconda.com/docs/getting-started/miniconda/install/overview).
```shell
conda create -n cartography python=3.10 -y
conda activate cartography
conda install numpy==1.26.4 scikit-learn==1.7.2 shapely matplotlib -c conda-forge -y
```

## Working procedure

For the sequence count statistics related to the protein sequence universe discussed in the manuscript, 
please run [number.py](https://github.com/HaolingZHANG/sequence-galaxy-illustration/blob/main/code/number.py). 

For the constructed figures, run 
[figure_1.py](https://github.com/HaolingZHANG/sequence-galaxy-illustration/blob/main/figure_1.py) 
through 
[figure_6.py](https://github.com/HaolingZHANG/sequence-galaxy-illustration/blob/main/figure_6.py). 

Figure 3 was constructed using Microsoft PowerPoint; see 
[figure_3.py](https://github.com/HaolingZHANG/sequence-galaxy-illustration/blob/main/figure_3.py)
for details.

The 3D structural elements in Figure 6a were generated from a pseudo-PDB file rendered in 
[PyMOL Software](https://www.pymol.org/). 
The procedure for generating this file is described in 
[structure.py](https://github.com/HaolingZHANG/sequence-galaxy-illustration/blob/main/code/structure.py). 
The rendered output from this Python script was used as input for styling within PyMOL Software. 
Final image composition was completed in 
[Adobe Illustrator](https://www.adobe.com/products/illustrator.html).

The table data are presented without additional processing; 
they are provided as-is.

# Citation

If you think the corresponding paper of this repository helps or being used in your research, 
please consider refer this work.

