"""
Visualization utilities for options pricing.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Optional, List, Dict, Any
import pandas as pd


def plot_predictions(y_true: np.ndarray, y_pred: np.ndarray, 
                    title: str = "Predictions vs Actual", 
                    sample_size: Optional[int] = None,
                    figsize: Tuple[int, int] = (12, 8)) -> plt.Figure:
    """
    Plot predictions vs actual values.
    
    Args:
        y_true: True values
        y_pred: Predicted values
        title: Plot title
        sample_size: Number of points to sample for plotting
        figsize: Figure size
        
    Returns:
        Matplotlib figure
    """
    if sample_size is not None and len(y_true) > sample_size:
        indices = np.random.choice(len(y_true), sample_size, replace=False)
        y_true_sample = y_true[indices]
        y_pred_sample = y_pred[indices]
    else:
        y_true_sample = y_true
        y_pred_sample = y_pred
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Scatter plot
    ax.scatter(y_true_sample, y_pred_sample, alpha=0.6, s=20)
    
    # Perfect prediction line
    min_val = min(y_true_sample.min(), y_pred_sample.min())
    max_val = max(y_true_sample.max(), y_pred_sample.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
    
    ax.set_xlabel('Actual Values')
    ax.set_ylabel('Predicted Values')
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return fig


def plot_training_history(history: Dict[str, List[float]], 
                         title: str = "Training History",
                         figsize: Tuple[int, int] = (12, 6)) -> plt.Figure:
    """
    Plot training history (loss curves).
    
    Args:
        history: Training history dictionary
        title: Plot title
        figsize: Figure size
        
    Returns:
        Matplotlib figure
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    
    # Loss plot
    ax1.plot(history['loss'], label='Training Loss')
    if 'val_loss' in history:
        ax1.plot(history['val_loss'], label='Validation Loss')
    ax1.set_title('Model Loss')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Learning rate plot (if available)
    if 'lr' in history:
        ax2.plot(history['lr'], label='Learning Rate')
        ax2.set_title('Learning Rate Schedule')
        ax2.set_xlabel('Epoch')
        ax2.set_ylabel('Learning Rate')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
    else:
        ax2.axis('off')
    
    plt.suptitle(title)
    plt.tight_layout()
    
    return fig


def plot_residuals(y_true: np.ndarray, y_pred: np.ndarray,
                  title: str = "Residuals Plot",
                  figsize: Tuple[int, int] = (12, 6)) -> plt.Figure:
    """
    Plot residuals (errors) analysis.
    
    Args:
        y_true: True values
        y_pred: Predicted values
        title: Plot title
        figsize: Figure size
        
    Returns:
        Matplotlib figure
    """
    residuals = y_true - y_pred
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    
    # Residuals scatter plot
    ax1.scatter(y_pred, residuals, alpha=0.6)
    ax1.axhline(y=0, color='r', linestyle='--')
    ax1.set_xlabel('Predicted Values')
    ax1.set_ylabel('Residuals')
    ax1.set_title('Residuals vs Predicted')
    ax1.grid(True, alpha=0.3)
    
    # Residuals histogram
    ax2.hist(residuals, bins=30, alpha=0.7, edgecolor='black')
    ax2.set_xlabel('Residuals')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Residuals Distribution')
    ax2.grid(True, alpha=0.3)
    
    plt.suptitle(title)
    plt.tight_layout()
    
    return fig


def plot_feature_importance(feature_names: List[str], 
                           importance_scores: np.ndarray,
                           title: str = "Feature Importance",
                           figsize: Tuple[int, int] = (10, 6)) -> plt.Figure:
    """
    Plot feature importance scores.
    
    Args:
        feature_names: List of feature names
        importance_scores: Importance scores for each feature
        title: Plot title
        figsize: Figure size
        
    Returns:
        Matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Sort features by importance
    sorted_indices = np.argsort(importance_scores)
    sorted_features = [feature_names[i] for i in sorted_indices]
    sorted_scores = importance_scores[sorted_indices]
    
    # Horizontal bar plot
    ax.barh(sorted_features, sorted_scores)
    ax.set_xlabel('Importance Score')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    
    return fig


def plot_price_distribution(prices: np.ndarray, 
                           title: str = "Option Price Distribution",
                           figsize: Tuple[int, int] = (10, 6)) -> plt.Figure:
    """
    Plot distribution of option prices.
    
    Args:
        prices: Array of option prices
        title: Plot title
        figsize: Figure size
        
    Returns:
        Matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.hist(prices, bins=50, alpha=0.7, edgecolor='black')
    ax.set_xlabel('Option Price')
    ax.set_ylabel('Frequency')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    
    # Add statistics
    mean_price = np.mean(prices)
    median_price = np.median(prices)
    ax.axvline(mean_price, color='r', linestyle='--', label=f'Mean: {mean_price:.2f}')
    ax.axvline(median_price, color='g', linestyle='--', label=f'Median: {median_price:.2f}')
    ax.legend()
    
    return fig


def create_comprehensive_report(y_true: np.ndarray, y_pred: np.ndarray,
                              feature_names: List[str],
                              importance_scores: Optional[np.ndarray] = None) -> plt.Figure:
    """
    Create a comprehensive visualization report.
    
    Args:
        y_true: True values
        y_pred: Predicted values
        feature_names: List of feature names
        importance_scores: Feature importance scores (optional)
        
    Returns:
        Matplotlib figure with subplots
    """
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Predictions vs Actual
    ax1 = plt.subplot(2, 3, 1)
    ax1.scatter(y_true, y_pred, alpha=0.6, s=20)
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    ax1.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2)
    ax1.set_xlabel('Actual')
    ax1.set_ylabel('Predicted')
    ax1.set_title('Predictions vs Actual')
    ax1.grid(True, alpha=0.3)
    
    # 2. Residuals
    ax2 = plt.subplot(2, 3, 2)
    residuals = y_true - y_pred
    ax2.scatter(y_pred, residuals, alpha=0.6)
    ax2.axhline(y=0, color='r', linestyle='--')
    ax2.set_xlabel('Predicted')
    ax2.set_ylabel('Residuals')
    ax2.set_title('Residuals Plot')
    ax2.grid(True, alpha=0.3)
    
    # 3. Residuals Distribution
    ax3 = plt.subplot(2, 3, 3)
    ax3.hist(residuals, bins=30, alpha=0.7, edgecolor='black')
    ax3.set_xlabel('Residuals')
    ax3.set_ylabel('Frequency')
    ax3.set_title('Residuals Distribution')
    ax3.grid(True, alpha=0.3)
    
    # 4. Price Distribution
    ax4 = plt.subplot(2, 3, 4)
    ax4.hist(y_true, bins=30, alpha=0.7, label='Actual', edgecolor='black')
    ax4.hist(y_pred, bins=30, alpha=0.7, label='Predicted', edgecolor='black')
    ax4.set_xlabel('Price')
    ax4.set_ylabel('Frequency')
    ax4.set_title('Price Distribution')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    # 5. Feature Importance (if available)
    ax5 = plt.subplot(2, 3, 5)
    if importance_scores is not None:
        sorted_indices = np.argsort(importance_scores)
        sorted_features = [feature_names[i] for i in sorted_indices]
        sorted_scores = importance_scores[sorted_indices]
        ax5.barh(sorted_features, sorted_scores)
        ax5.set_xlabel('Importance')
        ax5.set_title('Feature Importance')
    else:
        ax5.text(0.5, 0.5, 'Feature Importance\nNot Available', 
                ha='center', va='center', transform=ax5.transAxes)
        ax5.set_title('Feature Importance')
    ax5.grid(True, alpha=0.3)
    
    # 6. Performance Metrics
    ax6 = plt.subplot(2, 3, 6)
    from .evaluation import evaluate_model_performance
    metrics = evaluate_model_performance(y_true, y_pred)
    
    metric_names = ['MSE', 'RMSE', 'MAE', 'R²']
    metric_values = [metrics['mse'], metrics['rmse'], metrics['mae'], metrics['r2']]
    
    bars = ax6.bar(metric_names, metric_values)
    ax6.set_ylabel('Value')
    ax6.set_title('Performance Metrics')
    ax6.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, value in zip(bars, metric_values):
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2., height,
                f'{value:.3f}', ha='center', va='bottom')
    
    plt.tight_layout()
    return fig
