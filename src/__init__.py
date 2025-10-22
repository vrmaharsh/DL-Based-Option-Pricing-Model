"""
Deep Learning-Based Options Pricing Model

A sophisticated neural network model for pricing European options using deep learning techniques.
Based on research by A. Ke and A. Yang (2019).

Author: Harsh Verma
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Harsh Verma"
__email__ = "your.email@example.com"

from .models.options_pricer import OptionsPricer
from .utils.preprocessing import preprocess_options_data
from .utils.evaluation import evaluate_model_performance
from .utils.visualization import plot_predictions, plot_training_history

__all__ = [
    "OptionsPricer",
    "preprocess_options_data", 
    "evaluate_model_performance",
    "plot_predictions",
    "plot_training_history"
]
