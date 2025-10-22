"""
Main entry point for the Options Pricing Deep Learning application.
"""

import argparse
import sys
import os
from pathlib import Path

# Add src to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.options_pricer import OptionsPricer
from utils.evaluation import evaluate_model_performance
from utils.visualization import plot_predictions, plot_training_history


def main():
    """Main function for command-line interface."""
    parser = argparse.ArgumentParser(
        description="Deep Learning-Based Options Pricing Model"
    )
    
    parser.add_argument(
        '--mode',
        choices=['train', 'predict', 'evaluate'],
        default='predict',
        help='Mode to run the application'
    )
    
    parser.add_argument(
        '--call-model',
        type=str,
        help='Path to call options model file'
    )
    
    parser.add_argument(
        '--put-model',
        type=str,
        help='Path to put options model file'
    )
    
    parser.add_argument(
        '--call-scaler',
        type=str,
        help='Path to call options scaler file'
    )
    
    parser.add_argument(
        '--put-scaler',
        type=str,
        help='Path to put options scaler file'
    )
    
    parser.add_argument(
        '--time-to-expiry',
        type=float,
        help='Time to expiration in years'
    )
    
    parser.add_argument(
        '--strike-price',
        type=float,
        help='Strike price of the option'
    )
    
    parser.add_argument(
        '--underlying-price',
        type=float,
        help='Current underlying asset price'
    )
    
    parser.add_argument(
        '--volatility',
        type=float,
        help='Annualized volatility (0.0 to 1.0)'
    )
    
    parser.add_argument(
        '--risk-free-rate',
        type=float,
        help='Risk-free interest rate (0.0 to 1.0)'
    )
    
    parser.add_argument(
        '--option-type',
        choices=['call', 'put'],
        help='Type of option to price'
    )
    
    args = parser.parse_args()
    
    if args.mode == 'predict':
        predict_mode(args)
    elif args.mode == 'train':
        train_mode(args)
    elif args.mode == 'evaluate':
        evaluate_mode(args)


def predict_mode(args):
    """Handle prediction mode."""
    if not all([args.call_model, args.put_model, args.call_scaler, args.put_scaler]):
        print("Error: All model and scaler paths are required for prediction mode.")
        return
    
    if not all([args.time_to_expiry, args.strike_price, args.underlying_price, 
                args.volatility, args.risk_free_rate, args.option_type]):
        print("Error: All option parameters are required for prediction.")
        return
    
    try:
        # Initialize pricer
        pricer = OptionsPricer()
        pricer.load_models(
            args.call_model, args.put_model,
            args.call_scaler, args.put_scaler
        )
        
        # Make prediction
        if args.option_type == 'call':
            price = pricer.price_call(
                args.time_to_expiry, args.strike_price,
                args.underlying_price, args.volatility, args.risk_free_rate
            )
        else:
            price = pricer.price_put(
                args.time_to_expiry, args.strike_price,
                args.underlying_price, args.volatility, args.risk_free_rate
            )
        
        print(f"Predicted {args.option_type} option price: ${price:.2f}")
        
    except Exception as e:
        print(f"Error during prediction: {e}")


def train_mode(args):
    """Handle training mode."""
    print("Training mode not implemented in this version.")
    print("Please use the Jupyter notebook for model training.")


def evaluate_mode(args):
    """Handle evaluation mode."""
    print("Evaluation mode not implemented in this version.")
    print("Please use the Jupyter notebook for model evaluation.")


if __name__ == "__main__":
    main()
