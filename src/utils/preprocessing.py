"""
Data preprocessing utilities for options pricing.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from typing import Tuple, Optional


def preprocess_options_data(data: pd.DataFrame, 
                          target_column: str = 'close',
                          feature_columns: Optional[list] = None,
                          test_size: float = 0.2,
                          random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, 
                                                          np.ndarray, np.ndarray, MinMaxScaler]:
    """
    Preprocess options data for model training.
    
    Args:
        data: DataFrame containing options data
        target_column: Name of the target column
        feature_columns: List of feature column names
        test_size: Proportion of data for testing
        random_state: Random state for reproducibility
        
    Returns:
        Tuple of (X_train, X_test, y_train, y_test, scaler)
    """
    if feature_columns is None:
        feature_columns = ['t', 'strike_price', 'underlying_value', 'sigma', 'r']
    
    # Extract features and target
    X = data[feature_columns].values
    y = data[target_column].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Normalize features
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def normalize_features(features: np.ndarray, scaler: MinMaxScaler) -> np.ndarray:
    """
    Normalize features using a fitted scaler.
    
    Args:
        features: Feature array to normalize
        scaler: Fitted MinMaxScaler
        
    Returns:
        Normalized features
    """
    return scaler.transform(features)


def denormalize_predictions(predictions: np.ndarray, scaler: MinMaxScaler) -> np.ndarray:
    """
    Denormalize predictions using a fitted scaler.
    
    Args:
        predictions: Normalized predictions
        scaler: Fitted MinMaxScaler
        
    Returns:
        Denormalized predictions
    """
    return scaler.inverse_transform(predictions)
