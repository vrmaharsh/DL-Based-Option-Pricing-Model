#!/bin/bash

# GitHub Repository Setup Script for DL-Based Options Pricing Model
# This script helps you set up and push your project to GitHub

echo "🚀 Setting up GitHub repository for DL-Based Options Pricing Model..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
fi

# Add all files
echo "📦 Adding files to Git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Deep Learning-Based Options Pricing Model

- Advanced neural network architecture for options pricing
- Separate models for Call and Put options
- Comprehensive documentation and API
- CI/CD pipeline with GitHub Actions
- Production-ready code structure
- Real market data from Asian Paints (2017-2020)
- High performance: MSE ~1,027 for both option types"

# Set up remote repository (you'll need to replace with your actual GitHub URL)
echo "🔗 Setting up remote repository..."
echo "Please replace 'yourusername' with your actual GitHub username:"
echo "git remote add origin https://github.com/yourusername/DL-Based-Option-Pricing-Model.git"

# Push to GitHub
echo "📤 Pushing to GitHub..."
echo "git push -u origin main"

echo ""
echo "✅ Setup complete! Next steps:"
echo "1. Create a new repository on GitHub named 'DL-Based-Option-Pricing-Model'"
echo "2. Replace 'yourusername' in the commands above with your GitHub username"
echo "3. Run the git remote add origin command"
echo "4. Run the git push command"
echo ""
echo "🎉 Your extraordinary project will be live on GitHub!"
