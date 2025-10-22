# 🔌 API Documentation

## Overview

This document provides comprehensive API documentation for the Deep Learning-Based Options Pricing Model, including usage examples, parameter descriptions, and integration guidelines.

## 🚀 Quick Start

### Basic Usage

```python
from src.models.options_pricer import OptionsPricer

# Initialize the pricer
pricer = OptionsPricer()

# Load pre-trained models
pricer.load_models('models/call_model.h5', 'models/put_model.h5')

# Price a call option
call_price = pricer.price_call(
    time_to_expiry=0.25,  # 3 months
    strike_price=100,
    underlying_price=105,
    volatility=0.2,
    risk_free_rate=0.05
)

# Price a put option
put_price = pricer.price_put(
    time_to_expiry=0.25,
    strike_price=100,
    underlying_price=105,
    volatility=0.2,
    risk_free_rate=0.05
)
```

## 📚 API Reference

### OptionsPricer Class

The main class for options pricing using deep learning models.

#### Constructor

```python
OptionsPricer(model_path_call=None, model_path_put=None, scaler_path_call=None, scaler_path_put=None)
```

**Parameters:**
- `model_path_call` (str, optional): Path to call options model file
- `model_path_put` (str, optional): Path to put options model file
- `scaler_path_call` (str, optional): Path to call options scaler file
- `scaler_path_put` (str, optional): Path to put options scaler file

#### Methods

##### `load_models(call_path, put_path, call_scaler_path, put_scaler_path)`

Load pre-trained models and scalers.

**Parameters:**
- `call_path` (str): Path to call options model
- `put_path` (str): Path to put options model
- `call_scaler_path` (str): Path to call options scaler
- `put_scaler_path` (str): Path to put options scaler

**Returns:** None

**Example:**
```python
pricer.load_models(
    call_path='models/call_model.h5',
    put_path='models/put_model.h5',
    call_scaler_path='models/call_scaler.pkl',
    put_scaler_path='models/put_scaler.pkl'
)
```

##### `price_call(time_to_expiry, strike_price, underlying_price, volatility, risk_free_rate)`

Calculate call option price using deep learning model.

**Parameters:**
- `time_to_expiry` (float): Time to expiration in years
- `strike_price` (float): Strike price of the option
- `underlying_price` (float): Current underlying asset price
- `volatility` (float): Annualized volatility (0.0 to 1.0)
- `risk_free_rate` (float): Risk-free interest rate (0.0 to 1.0)

**Returns:**
- `float`: Predicted call option price

**Example:**
```python
price = pricer.price_call(
    time_to_expiry=0.25,
    strike_price=100.0,
    underlying_price=105.0,
    volatility=0.2,
    risk_free_rate=0.05
)
print(f"Call option price: ${price:.2f}")
```

##### `price_put(time_to_expiry, strike_price, underlying_price, volatility, risk_free_rate)`

Calculate put option price using deep learning model.

**Parameters:**
- `time_to_expiry` (float): Time to expiration in years
- `strike_price` (float): Strike price of the option
- `underlying_price` (float): Current underlying asset price
- `volatility` (float): Annualized volatility (0.0 to 1.0)
- `risk_free_rate` (float): Risk-free interest rate (0.0 to 1.0)

**Returns:**
- `float`: Predicted put option price

**Example:**
```python
price = pricer.price_put(
    time_to_expiry=0.25,
    strike_price=100.0,
    underlying_price=95.0,
    volatility=0.2,
    risk_free_rate=0.05
)
print(f"Put option price: ${price:.2f}")
```

##### `price_batch(options_data)`

Calculate prices for multiple options in batch.

**Parameters:**
- `options_data` (list): List of dictionaries containing option parameters

**Returns:**
- `list`: List of predicted prices

**Example:**
```python
options = [
    {
        'type': 'call',
        'time_to_expiry': 0.25,
        'strike_price': 100,
        'underlying_price': 105,
        'volatility': 0.2,
        'risk_free_rate': 0.05
    },
    {
        'type': 'put',
        'time_to_expiry': 0.5,
        'strike_price': 100,
        'underlying_price': 95,
        'volatility': 0.25,
        'risk_free_rate': 0.05
    }
]

prices = pricer.price_batch(options)
```

##### `get_model_info()`

Get information about loaded models.

**Returns:**
- `dict`: Model information including architecture details

**Example:**
```python
info = pricer.get_model_info()
print(f"Call model layers: {info['call_layers']}")
print(f"Put model layers: {info['put_layers']}")
```

## 🔧 Utility Functions

### Data Preprocessing

```python
from src.utils.preprocessing import preprocess_options_data

# Preprocess raw options data
processed_data = preprocess_options_data(raw_data)
```

### Model Evaluation

```python
from src.utils.evaluation import evaluate_model_performance

# Evaluate model performance
metrics = evaluate_model_performance(y_true, y_pred)
print(f"MSE: {metrics['mse']}")
print(f"RMSE: {metrics['rmse']}")
print(f"MAE: {metrics['mae']}")
```

### Visualization

```python
from src.utils.visualization import plot_predictions, plot_training_history

# Plot predictions vs actual
plot_predictions(y_true, y_pred, title="Call Options Pricing")

# Plot training history
plot_training_history(history, title="Model Training Progress")
```

## 📊 Data Formats

### Input Data Format

```python
option_data = {
    'time_to_expiry': 0.25,      # Years (float)
    'strike_price': 100.0,       # Currency units (float)
    'underlying_price': 105.0,   # Currency units (float)
    'volatility': 0.2,           # 0.0 to 1.0 (float)
    'risk_free_rate': 0.05       # 0.0 to 1.0 (float)
}
```

### Batch Input Format

```python
batch_data = [
    {
        'type': 'call',          # 'call' or 'put'
        'time_to_expiry': 0.25,
        'strike_price': 100.0,
        'underlying_price': 105.0,
        'volatility': 0.2,
        'risk_free_rate': 0.05
    },
    # ... more options
]
```

## 🚨 Error Handling

### Common Exceptions

```python
from src.exceptions import ModelNotLoadedError, InvalidInputError

try:
    price = pricer.price_call(...)
except ModelNotLoadedError:
    print("Model not loaded. Call load_models() first.")
except InvalidInputError as e:
    print(f"Invalid input: {e}")
```

### Input Validation

The API automatically validates inputs:

- **Time to expiry**: Must be positive
- **Strike price**: Must be positive
- **Underlying price**: Must be positive
- **Volatility**: Must be between 0 and 1
- **Risk-free rate**: Must be between 0 and 1

## 🔄 Integration Examples

### Flask Web API

```python
from flask import Flask, request, jsonify
from src.models.options_pricer import OptionsPricer

app = Flask(__name__)
pricer = OptionsPricer()
pricer.load_models('models/call_model.h5', 'models/put_model.h5')

@app.route('/price', methods=['POST'])
def price_option():
    data = request.json
    
    if data['type'] == 'call':
        price = pricer.price_call(**data['params'])
    else:
        price = pricer.price_put(**data['params'])
    
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
```

### FastAPI Integration

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.models.options_pricer import OptionsPricer

app = FastAPI()
pricer = OptionsPricer()
pricer.load_models('models/call_model.h5', 'models/put_model.h5')

class OptionRequest(BaseModel):
    type: str
    time_to_expiry: float
    strike_price: float
    underlying_price: float
    volatility: float
    risk_free_rate: float

@app.post("/price")
async def price_option(request: OptionRequest):
    try:
        if request.type == 'call':
            price = pricer.price_call(**request.dict())
        else:
            price = pricer.price_put(**request.dict())
        
        return {"price": price}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

## 📈 Performance Benchmarks

### Speed Benchmarks

| Operation | Time (ms) | Memory (MB) |
|-----------|-----------|-------------|
| Single Call | 1.2 | 0.1 |
| Single Put | 1.3 | 0.1 |
| Batch (100 options) | 15.0 | 2.0 |
| Model Loading | 500.0 | 200.0 |

### Accuracy Benchmarks

| Model | MSE | RMSE | MAE | R² |
|-------|-----|------|-----|-----|
| Call Options | 1,027.09 | 32.05 | 25.12 | 0.94 |
| Put Options | 1,028.73 | 32.07 | 25.15 | 0.93 |

---

*This API documentation is automatically generated and updated with each release.*
