# 🚀 Deployment Guide

This guide provides comprehensive instructions for deploying the Deep Learning-Based Options Pricing Model in various environments.

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for version control)
- GitHub account (for repository access)

## 🏠 Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/DL-Based-Option-Pricing-Model.git
cd DL-Based-Option-Pricing-Model
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
# Run Jupyter notebook
jupyter notebook "Options_Pricing_using_Deep_Learning (1).ipynb"

# Or use command-line interface
python src/main.py --help
```

## 🐳 Docker Deployment

### 1. Create Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

### 2. Build and Run
```bash
# Build Docker image
docker build -t dl-options-pricing .

# Run container
docker run -p 8888:8888 dl-options-pricing
```

## ☁️ Cloud Deployment

### AWS EC2 Deployment

1. **Launch EC2 Instance**
   - Choose Ubuntu 20.04 LTS
   - Select t3.medium or larger
   - Configure security groups (port 22, 8888)

2. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip git
   pip3 install -r requirements.txt
   ```

3. **Deploy Application**
   ```bash
   git clone https://github.com/yourusername/DL-Based-Option-Pricing-Model.git
   cd DL-Based-Option-Pricing-Model
   jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
   ```

### Google Cloud Platform

1. **Create VM Instance**
   ```bash
   gcloud compute instances create dl-options-pricing \
     --image-family=ubuntu-2004-lts \
     --image-project=ubuntu-os-cloud \
     --machine-type=e2-medium
   ```

2. **Deploy Application**
   ```bash
   gcloud compute ssh dl-options-pricing
   # Follow same steps as AWS
   ```

### Azure Deployment

1. **Create Virtual Machine**
   ```bash
   az vm create \
     --resource-group myResourceGroup \
     --name dl-options-pricing \
     --image UbuntuLTS \
     --size Standard_B2s
   ```

2. **Deploy Application**
   ```bash
   az vm run-command invoke \
     --resource-group myResourceGroup \
     --name dl-options-pricing \
     --command-id RunShellScript \
     --scripts "git clone https://github.com/yourusername/DL-Based-Option-Pricing-Model.git"
   ```

## 🌐 Web API Deployment

### Flask API Deployment

1. **Create API Server**
   ```python
   # api_server.py
   from flask import Flask, request, jsonify
   from src.models.options_pricer import OptionsPricer
   
   app = Flask(__name__)
   pricer = OptionsPricer()
   
   @app.route('/price', methods=['POST'])
   def price_option():
       data = request.json
       # Implementation here
       return jsonify({'price': price})
   
   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

2. **Deploy with Gunicorn**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 api_server:app
   ```

### FastAPI Deployment

1. **Create FastAPI Server**
   ```python
   # fastapi_server.py
   from fastapi import FastAPI
   from pydantic import BaseModel
   from src.models.options_pricer import OptionsPricer
   
   app = FastAPI()
   pricer = OptionsPricer()
   
   class OptionRequest(BaseModel):
       type: str
       time_to_expiry: float
       strike_price: float
       underlying_price: float
       volatility: float
       risk_free_rate: float
   
   @app.post("/price")
   async def price_option(request: OptionRequest):
       # Implementation here
       return {"price": price}
   ```

2. **Deploy with Uvicorn**
   ```bash
   pip install uvicorn
   uvicorn fastapi_server:app --host 0.0.0.0 --port 8000
   ```

## 🔧 Environment Configuration

### Environment Variables
Create a `.env` file:
```env
# Model paths
CALL_MODEL_PATH=models/call_model.h5
PUT_MODEL_PATH=models/put_model.h5
CALL_SCALER_PATH=models/call_scaler.pkl
PUT_SCALER_PATH=models/put_scaler.pkl

# API configuration
API_HOST=0.0.0.0
API_PORT=5000
DEBUG=False

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

### Configuration Management
```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CALL_MODEL_PATH = os.getenv('CALL_MODEL_PATH', 'models/call_model.h5')
    PUT_MODEL_PATH = os.getenv('PUT_MODEL_PATH', 'models/put_model.h5')
    API_HOST = os.getenv('API_HOST', '0.0.0.0')
    API_PORT = int(os.getenv('API_PORT', 5000))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
```

## 📊 Monitoring and Logging

### Application Logging
```python
# logging_config.py
import logging
import os

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/app.log'),
            logging.StreamHandler()
        ]
    )
```

### Performance Monitoring
```python
# monitoring.py
import time
import psutil
import logging

def monitor_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        end_memory = psutil.Process().memory_info().rss
        
        logging.info(f"Function {func.__name__} executed in {end_time - start_time:.2f}s")
        logging.info(f"Memory usage: {(end_memory - start_memory) / 1024 / 1024:.2f} MB")
        
        return result
    return wrapper
```

## 🔒 Security Considerations

### API Security
- Use HTTPS in production
- Implement API key authentication
- Add rate limiting
- Validate all inputs
- Use environment variables for secrets

### Model Security
- Store models securely
- Implement model versioning
- Add model validation
- Monitor for model drift

## 📈 Scaling Considerations

### Horizontal Scaling
- Use load balancers
- Implement stateless design
- Use container orchestration (Kubernetes)
- Implement caching (Redis)

### Vertical Scaling
- Monitor resource usage
- Optimize model inference
- Use GPU acceleration
- Implement model quantization

## 🚨 Troubleshooting

### Common Issues

1. **Model Loading Errors**
   - Check file paths
   - Verify model format
   - Check dependencies

2. **Memory Issues**
   - Increase memory allocation
   - Use model quantization
   - Implement batch processing

3. **Performance Issues**
   - Profile the application
   - Optimize model inference
   - Use caching

### Debug Mode
```python
# Enable debug mode
import logging
logging.basicConfig(level=logging.DEBUG)

# Or set environment variable
export DEBUG=True
```

## 📚 Additional Resources

- [TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [AWS Deployment Guide](https://aws.amazon.com/getting-started/)
- [Google Cloud Deployment](https://cloud.google.com/deployment-manager)

---

*This deployment guide provides comprehensive instructions for deploying your Options Pricing Model in various environments.*
