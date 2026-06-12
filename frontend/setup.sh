#!/bin/bash

echo "Setting up Zoning Research Tool Frontend..."

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "Installing Node.js dependencies..."
    npm install
else
    echo "Node modules already installed. Skipping npm install."
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your Mapbox token before running the application!"
fi

echo "✅ Frontend setup complete!"
echo ""
echo "To start the frontend development server:"
echo "  npm start"
