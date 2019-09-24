# TeachOpenCADD

#### A teaching platform for computer-aided drug design (CADD) using open source packages and data

Volkamer Lab 

*In Silico* Toxicology and Structural Bioinformatics <br>
Institute for Physiology <br>
Charitè - Universitätsmedizin Berlin <br>
[volkamerlab.org](https://physiologie-ccm.charite.de/en/research_at_the_institute/volkamer_lab/)

<img src="https://github.com/volkamerlab/TeachOpenCADD/blob/update-readme/README_figures/TeachOpenCADD_logo.svg" alt="TeachOpenCADD logo" width="200"/>

[![DOI](https://img.shields.io/badge/DOI-10.1186%2Fs13321--019--0351--x-blue.svg)](https://doi.org/10.1186/s13321-019-0351-x)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2600909.svg)](https://doi.org/10.5281/zenodo.2600909)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/volkamerlab/TeachOpenCADD/master)

<img src="https://github.com/volkamerlab/TeachOpenCADD/blob/update-readme/README_figures/TeachOpenCADD_logo.svg" alt="TeachOpenCADD logo" width="200"/>

## Table of contents  

* [Objective](#objective)
* [Topics](#topics)
* [Usage](#usage)
* [Contact](#contact)
* [Licence](#licence)
* [Citation](#citation)

## Aims of this teaching platform

(Back to [Table of contents](#table-of-contents).)

Open source programming packages for cheminformatics and structural bioinformatics are powerful tools to build modular, reproducible, and easy-to-share pipelines for computer-aided drug design (CADD). While documentation for tools is available, only few freely accessible examples teach underlying concepts focused on CADD usage such as the TDT initiative [1], addressing especially users new to the field.

Here, we present a CADD teaching platform developed from students for students, using open source packages such as the python tools RDKit [2], PyPDB [3], and PyMol [4]. For each topic, an interactive Jupyter Notebook [5] was developed, holding detailed theoretical background of the underlying topic and well-commented python code, freely available on GitHub. Illustrated at the example of EGFR kinase, we discuss how to acquire data from the public compound database ChEMBL [6], how to filter compounds for drug-likeness, and how to identify and remove unwanted substructures. Furthermore, we introduce measures for compound similarity, which are subsequently used to cluster compounds, i.e., for the selection of a divers compound set. We also employ machine learning approaches in order to build models for predicting novel active compounds. Lastly, structures are fetched from the public protein database PDB [7], used to generate ligand-based ensemble 3D pharmacophores and to conduct binding site comparison for off-target prediction. 

With this platform, we aim to introduce interested users to the ease and benefit of using open source cheminformatics tools. Topics will be continuously expanded and are open for contributions from the community. Beyond their teaching purpose, the notebooks can serve as starting point for users’ project-directed modifications and extensions. 


Literature:

[1] [S. Riniker et al., F1000Research, 2017, 6, 1136](https://f1000research.com/articles/6-1136/v1) 
[2] [G. Landrum, RDKit](http://www.rdkit.org)
[3] [W. Gilpin, Bioinformatics, 2016, 32, 156-60](https://academic.oup.com/bioinformatics/article/32/1/159/1743800) 
[4] [The PyMOL Molecular Graphics System, Version 1.8, Schrödinger, LLC](https://pymol.org)
[5] [T. Kluyver et al., IOS Press, 2016, 87-90.](http://ebooks.iospress.com/publication/42900)
[6] [A. Gaulton et al., Nucleic Acid Res., 2017, 40, D1100-7](https://academic.oup.com/nar/article/42/D1/D1083/1043509)
[7] [H. Berman et al., Nucleic Acid Res., 2000, 28, 235-42](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC102472/)


## Topics

(Back to [Table of contents](#table-of-contents).)

![Download repository](https://github.com/volkamerlab/TeachOpenCADD/blob/master/README_figures/TeachOpenCADD_topics.svg)

TeachOpenCADD offers teaching material on common tasks in computer-aided drug design. 
Currently, the following topics are available:

**Cheminformatics**

* Topic 1. Compound data acquisition: ChEMBL
* Topic 2. Molecular filtering: ADME and lead-likeness criteria
* Topic 3. Molecular filtering: unwanted substructures
* Topic 4. Ligand-based screening: compound similarity
* Topic 5. Compound clustering
* Topic 6. Maximum common substructures
* Topic 7. Ligand-based screening: machine learning
   
**Structural bioinformatics**

* Topic 8. Protein data acquisition: Protein Data Bank (PDB)
* Topic 9. Ligand-based pharmacophores
* Topic 10. Binding site similarity
* Topic 11. Structure-based CADD using online APIs/servers
  * 11a. Querying KLIFS & PubChem for potential kinase inhibitors
  * 11b. Docking the candidates against the target 
  * 11c. Visualizing the results and comparing against known data


The teaching material is offered in the form of 
* coding-based *Jupyter Notebooks* (topics 1-11) here on GitHub, so called *talktorials* (talk + tutorial), i.e. tutorials that can also be used in presentations, and
* GUI-based *KNIME workflows* (topics 1-8) on the [KNIME Hub](https://hub.knime.com/volkamerlab/space/TeachOpenCADD/TeachOpenCADD).

## Usage instructions

(Back to [Table of contents](#table-of-contents).)

You can use Binder to host the repository and all needed dependencies, or 
you can use our talktorials locally (download repository and install dependencies).


### Use Binder (for talktorials T1-T8)

Use binder to host the repository and all needed dependencies by following this link:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/volkamerlab/TeachOpenCADD/master)

The setup will take a few minutes.

### Install locally (for all talktorials)

#### Linux

1.  Get your local copy of the TeachOpenCADD repository (including the talktorials) by

    a. ... either downloading it as zip archive and unzipping it: 
    
    ![Download repository](https://github.com/volkamerlab/TeachOpenCADD/blob/master/README_figures/download_repo.png)
   
    b. ... or cloning it to your computer using the package `git`:

        ```bash
        git clone https://github.com/volkamerlab/TeachOpenCADD.git
        ```
        
2.  Use the Anaconda software for a clean package version management. 
   
    Install Anaconda2 or Anaconda3. In theory, it should not matter which Anaconda version you install. However, we only tested it for Anaconda2, so we cannot guarantee the same behaviour for Anaconda3.

    https://docs.anaconda.com/anaconda/install/

3.  Use the package management system conda to create an environment (called `teachopencadd`) for the talktorials. 
   
    We provide an environment file (yml file) containing all required packages.

    ```bash
    conda env create -f environment.yml
    ```

    Note: You can also create this environment manually. 
    Check ["Alternatively create conda environment manually"](#Alternatively-create-conda-environment-manually) for this.

4.  Activate the conda environment.
    
    ```bash
    conda activate teachopencadd
    ```
    
    Now you can work within the conda environment. 
    
5.  Link the conda environment to the Jupyter notebook.
    
    ```bash
    python -m ipykernel install --user --name teachopencadd
    
    # FYI, uninstall this link again with this command:
    #jupyter kernelspec uninstall teachopencadd
    ``` 

6.  Start the Jupyter notebook.

    ```bash
    jupyter notebook
    ```
    
7.  Change the Jupyter kernel to the conda environment via the menu:

    `Kernel > Change kernel > teachopencadd`
    
    ![Change Jupyter kernel](https://github.com/volkamerlab/TeachOpenCADD/blob/master/README_figures/jupyter_kernel_teachopencadd.png)
    
8.  Now you can get started with your first talktorial. Enjoy!



##### Alternatively create conda environment manually

**Note**: This is the alternative to creating the conda environment using the yml file as described in step 3 above. 

```bash
# Create and activate an environment called `teachopencadd`
conda create -n teachopencadd python=3.6
conda activate teachopencadd

# Install packages via conda
conda install jupyter  # Installs also ipykernel
conda install -c rdkit rdkit  # Installs also numpy and pandas
conda install -c samoturk pymol  # Installs also freeglut and glew
conda install -c conda-forge pmw  # Necessary for PyMol terminal window to pop up
conda install -c conda-forge scikit-learn  # Installs also scipy
conda install -c conda-forge seaborn  # Installs also matplotlib

# Install packages via pip (which is probably installed by default in your environment)
pip install chembl_webresource_client biopandas pypdb
```

#### Windows

Generally, the installation works the same under Linux and Windows without problems.

The only difference, we encountered, is the installation of PyMol:

* Download PyMol from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymol 
* Put it where Anaconda2 is installed (e.g. C:\Anaconda2)
* Open a command prompt as administrator (Windows > accessories > command prompt, "right-click" > open as administrator)
* Go to the Anaconda directory by typing the correct path on the prompt:

```bash
cd C:/Anaconda2
set path=%path%;C:\Anaconda2
pip install pymol‑2.3.0a0‑cp36‑cp36m‑win_amd64.whl
pip install pymol_launcher‑2.1‑cp36‑cp36m‑win_amd64.whl
# or whatever pymol_XXXX.whl you have downloaded
```

## Contact
(Back to [Table of contents](#table-of-contents).)

Please contact us if you have questions or suggestions!

* If you have questions regarding our Jupyter Notebooks, please open an issue on our GitHub repository: https://github.com/volkamerlab/teachopencadd/issues
* If you have questions regarding our KNIME workflows, please make a post on our KNIME Hub page in the "Discussion" section: https://hub.knime.com/volkamerlab/space/TeachOpenCADD/TeachOpenCADD
* If you have ideas for new topics, please fill out our questionnaire: [contribute.volkamerlab.org](contribute.volkamerlab.org)
* For all other requests, please send us an email: teachopencadd@charite.de

We are looking forward to hearing from you!


## License
(Back to [Table of contents](#table-of-contents).)

This work is licensed under the Attribution 4.0 International (CC BY 4.0).
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.


## Citation
(Back to [Table of contents](#table-of-contents).)

The authors of the TeachOpenCADD platform received public funding:
* Bundesministerium für Bildung und Forschung (Grant Number 031A262C) 
* Deutsche Forschungsgemeinschaft (Grant number VO 2353/1-1)
* HaVo-Stiftung, Ludwigshafen, Germany
* Stiftung Charité (Einstein BIH Visiting Fellow project)
* "SUPPORT für die Lehre" program (Förderung innovativer Lehrvorhaben) of the Freie Universität Berlin
* Open Access Publication Fund of Charité – Universitätsmedizin Berlin

If you make use of the TeachOpenCADD material in scientific publications, please cite our respective articles:
* [TeachOpenCADD Jupyter Notebooks: Talktorials 1-10](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x>`). 
* [TeachOpenCADD KNIME workflows](TBA)

It will help measure the impact of our research and future funding!

```
@article{TeachOpenCADD2019,
    author = {Sydow, Dominique and Morger, Andrea and Driller, Maximilian and Volkamer, Andrea},
    doi = {10.1186/s13321-019-0351-x},
    issn = {1758-2946},
    journal = {J. Cheminform.},
    number = {1},
    pages = {29},
    title = {{TeachOpenCADD: a teaching platform for computer-aided drug design using open source packages and data}},
    url = {https://doi.org/10.1186/s13321-019-0351-x},
    volume = {11},
    year = {2019}
}
```
