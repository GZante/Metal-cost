# Metal Price Forecasting using LSTM

This repository contains code for forecasting metal prices using a Bidirectional Long Short-Term Memory (LSTM) neural network. Additionally, it includes a Tkinter-based GUI application for visualizing metal values and calculating the total metal value based on user input.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)



## Introduction

This project aims to forecast the prices of various metals using historical price data. The forecasting model is built using a Bidirectional LSTM neural network, which is well-suited for time series prediction tasks. The repository also includes a Tkinter-based GUI application that allows calculating price of a metal based on its content in a waste or mineral. Prices can be found in the attached excel file. Price are varying, and highly dependent on the metal form and purity. 

## Features

- **Metal Price Forecasting**: Forecast the prices of various metals using historical price data.
- **Bidirectional LSTM Model**: Utilize a Bidirectional LSTM neural network for accurate forecasting.
- **Tkinter GUI**: A user-friendly GUI application for visualizing metal values and calculating the total metal value.
- **Data Visualization**: Plot the original and forecasted metal prices for better analysis.

The Long Short-Term Memory (LSTM) model included in this repository is designed to forecast the prices of various metals for which historical price data is available on Yahoo Finance. The method, while not perfect and potentially inaccurate, provides a robust starting point for metal price forecasting. The hyperparameters, such as the learning rate, have been optimized, and the architecture of the neural network has been carefully designed. Tests have been conducted with both a single layer and a few layers to keep the model simple yet effective.

The code provides Mean Absolute Percentage Error (MAPE) and accuracy metrics for each metal, allowing users to evaluate the model's performance. Additionally, a plot is generated that includes historical, training, and test values, providing a visual representation of the model's forecasting capabilities.

Table 1 below is summarizing the train and test accuracy and MAPE for each metal:
Table 1. Train and test MAPE and accuracy for different metals
| Metal      | Train MAPE | Train Accuracy | Test MAPE  | Test Accuracy |
|------------|------------|----------------|------------|---------------|
| Gold       | 0.0098     | 0.9902         | 0.0084     | 0.9916        |
| Silver     | 0.0297     | 0.9703         | 0.0180     | 0.9820        |
| Platinum   | 0.0162     | 0.9838         | 0.0188     | 0.9812        |
| Palladium  | 0.0328     | 0.9672         | 0.0224     | 0.9776        |
| Aluminum   | 0.0088     | 0.9912         | 0.0106     | 0.9894        |
| Copper     | 0.0123     | 0.9877         | 0.0116     | 0.9884        |


The figure below shows the data obtained for gold, including the historical, training, and test values. This visual representation helps in understanding the model's performance and accuracy.


![image](https://github.com/user-attachments/assets/d96b49b6-3027-4382-b019-3f7936383522)

Figure 1. Actual gold price with train and test forecasts obtained with the LSTM 

The GUI is a tool to help calculate the metal value one can foun in metallic waste, knowing the metal content in 1 kg of waste materials. It allows selecting various metals from a periodic table, as can be seen from Figure 2. A random value is given to each metal. It is based on the excel file provided. This file contain metal values (which are highly dependent on metal form, purity and change over time). The reference websites provided can help to actualize this value.

![image](https://github.com/user-attachments/assets/c3a09959-c954-41e0-8ab6-dc84bbb7aa36)

Figure 2. Screenshot of the GUI to calculate metal value


