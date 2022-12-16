# RadiomicsContourEffect
 Study of contour effects on radiomic prostate cancer studies

## Description
The goal of this work is to study the effects of contour variability on prostate cancer radiomics. These changes can be noise addition or using other user-defined volumes such as the PTV or GTV. 

## Getting Started
### Dependencies
This work was developed in Python. Features are intended to be the ones extracted with 3DSlicer, Radiomics extension. Pandas is used to open and format the features dataset. The Machine-learning pipeline is built using Sklearn and Seaborn is used for visualization.
### Installing
- Clone the repository to your PC (green button or on GitHub Desktop press Ctrl+Shift+O)
- Assuming you already have python installed, create a virtual environment in a folder of your choice: In a command line, cd to that folder and type `python -m venv radiomics_venv`
- In the same folder, type: `radiomics_venv\Scripts\activate` (Windows)
- Them cd to the folder where you cloned the repository and install all dependencies typing: `pip install -r requirements.txt`
### Running
The main.py file contains the main script. It will read a file named features.csv. This file contains example features extracted from a private dataset of 43 patients. You will be using a different dataset, so make sure the extracted features are in the same format. It will also save the results in a file named analysis.csv. The plot_roc.py file will plot scatterplots (number of PCA components vs ROC Value for each class). You can also find the developed Classifier and a MulticlassROCDisplay utility class in the tools.py file. Change whatever you need to adjust to your dataset and needs.


