# Deep Learning-Based Options Pricing Model

A sophisticated neural network model for pricing European options using deep learning techniques.

## Overview

This project implements a deep learning approach to options pricing, specifically for Asian Paints (ASIANPAINT) options data from 2017-2020. The model uses advanced neural network architectures to achieve high accuracy in pricing both Call and Put options.

## Files

- **`Options_Pricing_using_Deep_Learning (1).ipynb`** - Main Jupyter notebook containing the complete implementation
- **`options_dataset.xlsx`** - Dataset containing Asian Paints options data (2017-2020)

## Key Features

- **Dual Models**: Separate neural networks for Call and Put options
- **Advanced Architecture**: Multi-layer DNN with LeakyReLU activation and BatchNormalization
- **High Performance**: MSE scores of ~1,027 for both option types
- **Real Market Data**: 4 years of actual Asian Paints options data
- **Research-Based**: Implementation based on academic research (Ke & Yang, 2019)

## Model Performance

| Model Type | MSE Score | Architecture |
|------------|-----------|--------------|
| Call Options | 1,027.09 | 4-layer DNN (400 units) |
| Put Options | 1,028.73 | 5-layer DNN (400 units) |

## Usage

1. Open the Jupyter notebook
2. Install required dependencies (TensorFlow, Keras, pandas, numpy, scikit-learn, matplotlib)
3. Run all cells to train and evaluate the models

## Author

Harsh Verma (2K22/MC/63)

## License

MIT License