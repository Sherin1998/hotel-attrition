# hotel-attrition 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Tools Used](#bug---feature-request)
 


## Demo

Link: https://customerhotel.herokuapp.com/




## Overview
This is a streamlit app for prediction of customer arrival in a hotel

## Motivation
To get correct prediction of whether a customer will check in a hotel based on input parameters.This allows them to expand promotional offers and improve facilities and rectify the issues where they lack
## Installation
The Code is written in Python 3.7. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── app.py
├── Procfile
├── README.md
├── app.py
├──setup.sh
├── Task2.ipynb
├── svmmodel.pkl
├── scaler.pkl
├── requirements.txt
```

## Tools Used
Pycharm,JupyterNotebook,Github,Heroku,streamlit



Train Data link :https://drive.google.com/drive/folders/1Xk-3vOBCfPdttnrRKxNNuwVNgWd9nUFE

Test data link :https://drive.google.com/drive/folders/1Xk-3vOBCfPdttnrRKxNNuwVNgWd9nUFE



##New Evnvironment Creation

conda create -n hotelattrition python=3.7

activate hotelattrition 

##Dependencies creation

cd file location

pip freeze>requiremnets.txt






