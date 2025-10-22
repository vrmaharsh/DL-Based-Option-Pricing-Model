"""
Model evaluation utilities for options pricing.
"""

import numpy as np
from typing import Dict, Tuple
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def evaluate_model_performance(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """
    Evaluate model performance using various metrics.
    
    Args:
        y_true: True values
        y_pred: Predicted values
        
    Returns:
        Dictionary containing performance metrics
    """
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    # Calculate percentage errors
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    return {
        'mse': mse,
        'rmse': rmse,
        'mae': mae,
        'r2': r2,
        'mape': mape
    }


def calculate_prediction_accuracy(y_true: np.ndarray, y_pred: np.ndarray, 
                                tolerance: float = 0.05) -> float:
    """
    Calculate prediction accuracy within a tolerance.
    
    Args:
        y_true: True values
        y_pred: Predicted values
        tolerance: Tolerance for accuracy (default 5%)
        
    Returns:
        Accuracy percentage
    """
    errors = np.abs((y_true - y_pred) / y_true)
    accurate_predictions = np.sum(errors <= tolerance)
    accuracy = (accurate_predictions / len(y_true)) * 100
    
    return accuracy


def compare_with_black_scholes(y_true: np.ndarray, y_pred_dl: np.ndarray, 
                             y_pred_bs: np.ndarray) -> Dict[str, float]:
    """
    Compare deep learning model with Black-Scholes model.
    
    Args:
        y_true: True option prices
        y_pred_dl: Deep learning predictions
        y_pred_bs: Black-Scholes predictions
        
    Returns:
        Dictionary containing comparison metrics
    """
    dl_metrics = evaluate_model_performance(y_true, y_pred_dl)
    bs_metrics = evaluate_model_performance(y_true, y_pred_bs)
    
    # Calculate improvement
    mse_improvement = ((bs_metrics['mse'] - dl_metrics['mse']) / bs_metrics['mse']) * 100
    rmse_improvement = ((bs_metrics['rmse'] - dl_metrics['rmse']) / bs_metrics['rmse']) * 100
    
    return {
        'dl_mse': dl_metrics['mse'],
        'bs_mse': bs_metrics['mse'],
        'mse_improvement': mse_improvement,
        'dl_rmse': dl_metrics['rmse'],
        'bs_rmse': bs_metrics['rmse'],
        'rmse_improvement': rmse_improvement,
        'dl_r2': dl_metrics['r2'],
        'bs_r2': bs_metrics['r2']
    }


def calculate_value_at_risk(predictions: np.ndarray, confidence_level: float = 0.95) -> float:
    """
    Calculate Value at Risk (VaR) for predictions.
    
    Args:
        predictions: Array of predictions
        confidence_level: Confidence level for VaR calculation
        
    Returns:
        VaR value
    """
    return np.percentile(predictions, (1 - confidence_level) * 100)


def calculate_expected_shortfall(predictions: np.ndarray, confidence_level: float = 0.95) -> float:
    """
    Calculate Expected Shortfall (ES) for predictions.
    
    Args:
        predictions: Array of predictions
        confidence_level: Confidence level for ES calculation
        
    Returns:
        ES value
    """
    var = calculate_value_at_risk(predictions, confidence_level)
    return np.mean(predictions[predictions <= var])
