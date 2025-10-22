# 🚀 Deep Learning-Based Options Pricing Model

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12+-orange.svg)](https://tensorflow.org)
[![Keras](https://img.shields.io/badge/Keras-2.12+-red.svg)](https://keras.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)

> **Revolutionary Options Pricing using Advanced Deep Learning Techniques**  
> A sophisticated neural network model that outperforms traditional Black-Scholes pricing methods for European options on Asian Paints (ASIANPAINT) stock.

## 🌟 Key Highlights

- **🎯 High Accuracy**: Achieves superior performance compared to traditional pricing models
- **🧠 Advanced Architecture**: Multi-layer deep neural networks with LeakyReLU activation and BatchNormalization
- **📊 Real Market Data**: Trained on 4 years of actual Asian Paints options data (2017-2020)
- **⚡ Optimized Training**: Implements early stopping and learning rate scheduling
- **📈 Dual Models**: Separate specialized models for Call and Put options
- **🔬 Research-Based**: Implementation based on cutting-edge academic research

## 📊 Model Performance

| Model Type | MSE Score | Architecture | Training Data |
|------------|-----------|--------------|---------------|
| **Call Options** | 1,027.09 | 4-layer DNN (400 units) | 4 years ASIANPAINT data |
| **Put Options** | 1,028.73 | 5-layer DNN (400 units) | 4 years ASIANPAINT data |

## 🏗️ Architecture Overview

### Neural Network Design
```
Input Layer (5 features) → Dense(400) → LeakyReLU
    ↓
Hidden Layers (3-4 layers):
    Dense(400) → BatchNormalization → LeakyReLU
    ↓
Output Layer: Dense(1) → ReLU
```

### Input Features
- **t**: Time to expiration
- **strike_price**: Option strike price
- **underlying_value**: Current stock price
- **sigma**: Volatility
- **r**: Risk-free interest rate

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- TensorFlow 2.12+
- Jupyter Notebook

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/DL-Based-Option-Pricing-Model.git
   cd DL-Based-Option-Pricing-Model
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the notebook**
   ```bash
   jupyter notebook "Options_Pricing_using_Deep_Learning (1).ipynb"
   ```

## 📈 Results & Visualizations

### Model Performance Comparison
The deep learning models demonstrate significant improvements over traditional pricing methods:

- **Call Options MSE**: 1,027.09
- **Put Options MSE**: 1,028.73
- **Training Efficiency**: Early stopping prevents overfitting
- **Validation Accuracy**: Consistent performance across different market conditions

### Prediction vs Actual Prices
The models show excellent correlation between predicted and actual option prices, with clear visualization of model performance across different option indices.

## 🔬 Technical Implementation

### Data Preprocessing
- **Normalization**: MinMaxScaler for feature scaling
- **Train-Test Split**: 80-20 split with random state for reproducibility
- **Feature Engineering**: Optimized input features for maximum model performance

### Model Training
- **Optimizer**: Adam optimizer with adaptive learning rate
- **Loss Function**: Mean Squared Error (MSE)
- **Callbacks**: 
  - Early Stopping (patience=5)
  - Learning Rate Reduction (factor=0.2, patience=3)
- **Batch Size**: 128 for optimal training efficiency

### Advanced Techniques
- **LeakyReLU Activation**: Prevents dying ReLU problem
- **Batch Normalization**: Stabilizes training and improves convergence
- **Dropout**: Implicit regularization through early stopping

## 📚 Research Foundation

This implementation is based on the groundbreaking research:
> **"Option pricing with deep learning"** by A. Ke and A. Yang (2019)

The project demonstrates practical application of academic research in real-world financial markets.

## 🛠️ Project Structure

```
DL-Based-Option-Pricing-Model/
├── 📊 Options_Pricing_using_Deep_Learning (1).ipynb  # Main implementation
├── 📈 options_dataset.xlsx                           # Market data
├── 📋 requirements.txt                               # Dependencies
├── 📖 README.md                                      # This file
├── 🔧 .github/workflows/                             # CI/CD pipelines
├── 📁 docs/                                          # Documentation
└── 🧪 tests/                                         # Unit tests
```

## 🎯 Use Cases

- **Quantitative Finance**: Options pricing and risk management
- **Algorithmic Trading**: Real-time options valuation
- **Risk Management**: Portfolio hedging strategies
- **Academic Research**: Deep learning in finance applications
- **Financial Modeling**: Advanced pricing model development

## 🔮 Future Enhancements

- [ ] **Real-time API**: RESTful API for live pricing
- [ ] **Multi-Asset Support**: Extend to other underlying assets
- [ ] **American Options**: Support for early exercise
- [ ] **Ensemble Methods**: Combine multiple models for better accuracy
- [ ] **Web Dashboard**: Interactive visualization interface
- [ ] **Cloud Deployment**: Scalable cloud-based pricing service

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Harsh Verma**  
*Student ID: 2K22/MC/63*

- 🔗 [LinkedIn](https://linkedin.com/in/yourprofile)
- 📧 [Email](mailto:your.email@example.com)
- 🐙 [GitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Asian Paints Ltd. for providing market data
- TensorFlow and Keras teams for excellent deep learning frameworks
- The academic community for foundational research in financial ML
- Open source contributors who made this project possible

## 📊 Citation

If you use this project in your research or work, please cite:

```bibtex
@software{deep_learning_options_pricing,
  title={Deep Learning-Based Options Pricing Model},
  author={Harsh Verma},
  year={2024},
  url={https://github.com/yourusername/DL-Based-Option-Pricing-Model}
}
```

---

<div align="center">

**⭐ Star this repository if you found it helpful! ⭐**

*Built with ❤️ for the quantitative finance community*

</div>