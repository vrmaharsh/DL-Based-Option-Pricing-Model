"""
Custom exceptions for the Options Pricing Deep Learning project.
"""


class OptionsPricingError(Exception):
    """Base exception for options pricing errors."""
    pass


class ModelNotLoadedError(OptionsPricingError):
    """Raised when trying to use models that haven't been loaded."""
    pass


class InvalidInputError(OptionsPricingError):
    """Raised when input parameters are invalid."""
    pass


class DataProcessingError(OptionsPricingError):
    """Raised when data processing fails."""
    pass


class ModelTrainingError(OptionsPricingError):
    """Raised when model training fails."""
    pass


class PredictionError(OptionsPricingError):
    """Raised when prediction fails."""
    pass
