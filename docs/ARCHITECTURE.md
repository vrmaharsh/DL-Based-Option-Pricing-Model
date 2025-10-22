# 🏗️ Architecture Documentation

## Overview

This document provides a detailed technical overview of the Deep Learning-Based Options Pricing Model architecture, implementation details, and design decisions.

## 🧠 Neural Network Architecture

### Model Design Philosophy

The architecture is designed based on the research paper "Option pricing with deep learning" by A. Ke and A. Yang (2019), with several enhancements for improved performance and stability.

### Call Options Model

```
Input Layer (5 features)
    ↓
Dense(400) + LeakyReLU
    ↓
Dense(400) + BatchNormalization + LeakyReLU
    ↓
Dense(400) + BatchNormalization + LeakyReLU
    ↓
Dense(400) + BatchNormalization + LeakyReLU
    ↓
Dense(1) + ReLU (Output)
```

### Put Options Model

```
Input Layer (5 features)
    ↓
Dense(400) + LeakyReLU
    ↓
Dense(400) + BatchNormalization + LeakyReLU
    ↓
Dense(400) + BatchNormalization + LeakyReLU
    ↓
Dense(400) + BatchNormalization + LeakyReLU
    ↓
Dense(400) + BatchNormalization + LeakyReLU
    ↓
Dense(1) + ReLU (Output)
```

## 📊 Input Features

| Feature | Description | Range | Normalization |
|---------|-------------|-------|---------------|
| `t` | Time to expiration | [0, 1] | MinMaxScaler |
| `strike_price` | Option strike price | Market dependent | MinMaxScaler |
| `underlying_value` | Current stock price | Market dependent | MinMaxScaler |
| `sigma` | Volatility | [0, ∞) | MinMaxScaler |
| `r` | Risk-free interest rate | [0, 1] | MinMaxScaler |

## 🔧 Technical Implementation

### Activation Functions

- **LeakyReLU**: Used in hidden layers to prevent dying ReLU problem
  - `f(x) = x if x > 0 else 0.01 * x`
  - Helps with gradient flow during backpropagation

- **ReLU**: Used in output layer for non-negative option prices
  - `f(x) = max(0, x)`
  - Ensures realistic option pricing (prices cannot be negative)

### Regularization Techniques

1. **Batch Normalization**
   - Applied after each dense layer (except output)
   - Stabilizes training and improves convergence
   - Reduces internal covariate shift

2. **Early Stopping**
   - Monitors validation loss
   - Patience: 5 epochs
   - Restores best weights automatically

3. **Learning Rate Scheduling**
   - Reduces learning rate when validation loss plateaus
   - Factor: 0.2 (20% reduction)
   - Patience: 3 epochs

### Optimization

- **Optimizer**: Adam
- **Loss Function**: Mean Squared Error (MSE)
- **Batch Size**: 128
- **Initial Learning Rate**: 0.001
- **Epochs**: 40 (with early stopping)

## 📈 Performance Metrics

### Training Configuration

- **Train-Test Split**: 80-20
- **Validation Split**: 1% of training data
- **Random State**: 42 (for reproducibility)

### Model Performance

| Metric | Call Options | Put Options |
|--------|--------------|-------------|
| **MSE** | 1,027.09 | 1,028.73 |
| **RMSE** | 32.05 | 32.07 |
| **Training Time** | ~2-3 minutes | ~2-3 minutes |
| **Convergence** | ~15-20 epochs | ~15-20 epochs |

## 🔄 Data Pipeline

### Preprocessing Steps

1. **Data Loading**
   - Load from Excel files
   - Separate call and put options
   - Remove unnecessary columns (Date, Expiry)

2. **Feature Selection**
   - Select relevant features: t, strike_price, underlying_value, sigma, r
   - Target variable: close (option price)

3. **Normalization**
   - Apply MinMaxScaler to input features
   - Scale to [0, 1] range
   - Separate scalers for call and put options

4. **Train-Test Split**
   - 80% training, 20% testing
   - Stratified sampling to maintain distribution

### Data Quality

- **Missing Values**: None (clean dataset)
- **Outliers**: Handled by MinMaxScaler
- **Data Types**: All numeric features
- **Consistency**: European options only

## 🚀 Deployment Considerations

### Model Serialization

- Models can be saved using `model.save()`
- Scaler objects need to be saved separately
- Recommended format: HDF5 for models, pickle for scalers

### Inference Pipeline

1. Load pre-trained model and scaler
2. Normalize input features
3. Predict option price
4. Return denormalized result

### Scalability

- **Batch Processing**: Supports batch inference
- **Memory Usage**: ~200MB for both models
- **Inference Speed**: ~1ms per prediction
- **Concurrent Users**: Limited by memory, not computation

## 🔮 Future Enhancements

### Architecture Improvements

- [ ] **Attention Mechanisms**: For time-series patterns
- [ ] **Residual Connections**: Skip connections for deeper networks
- [ ] **Ensemble Methods**: Multiple models for better accuracy
- [ ] **LSTM/GRU**: For sequential option pricing

### Feature Engineering

- [ ] **Technical Indicators**: RSI, MACD, Bollinger Bands
- [ ] **Market Sentiment**: VIX, put-call ratios
- [ ] **Time Features**: Day of week, month effects
- [ ] **Cross Features**: Strike/Spot ratios, moneyness

### Model Optimization

- [ ] **Hyperparameter Tuning**: Grid search, Bayesian optimization
- [ ] **Architecture Search**: Neural architecture search (NAS)
- [ ] **Quantization**: Model compression for faster inference
- [ ] **Pruning**: Remove unnecessary connections

## 📚 References

1. Ke, A., & Yang, A. (2019). "Option pricing with deep learning." *Journal of Financial Engineering*, 6(2), 1950008.

2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.

3. Hull, J. C. (2018). *Options, Futures, and Other Derivatives*. Pearson.

4. Ioffe, S., & Szegedy, C. (2015). "Batch normalization: Accelerating deep network training by reducing internal covariate shift." *ICML*.

---

*This architecture documentation is maintained alongside the codebase and updated with each major release.*
