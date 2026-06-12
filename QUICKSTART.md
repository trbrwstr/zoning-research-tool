# Quick Start Guide

Get the Zoning Research Tool up and running in minutes.

## Prerequisites

- Python 3.9+
- Node.js 16+
- OpenAI API key
- Mapbox access token

## Setup (5 minutes)

### 1. Clone and Navigate
```bash
cd zoning-research-tool
```

### 2. Backend Setup
```bash
cd backend
./setup.sh
# Edit backend/.env and add your API keys
```

### 3. Frontend Setup
```bash
cd ../frontend
./setup.sh
# Edit frontend/.env and add your Mapbox token
```

### 4. Run Application

**Option A: Run both servers separately**
```bash
# Terminal 1 - Backend
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Frontend
cd frontend
npm start
```

**Option B: Run with combined script**
```bash
cd zoning-research-tool
./start-dev.sh
```

### 5. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## First Use

1. Open http://localhost:3000 in your browser
2. Enter a US address (e.g., "123 Main St, San Francisco, CA")
3. Click "Research"
4. Wait for the analysis to complete
5. View comprehensive zoning information including:
   - Zoning code and description
   - Setback requirements
   - Height restrictions
   - Lot coverage
   - Permitted uses
   - AI-powered recommendations

## Required API Keys

### OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Add to `backend/.env` as `OPENAI_API_KEY=sk-...`

### Mapbox Access Token
1. Go to https://account.mapbox.com/
2. Create an account and get your access token
3. Add to both `backend/.env` and `frontend/.env` as `MAPBOX_ACCESS_TOKEN=pk...`

## Troubleshooting

### Backend won't start
- Ensure Python 3.9+ is installed
- Check that virtual environment is activated
- Verify all dependencies are installed: `pip install -r requirements.txt`

### Frontend won't start
- Ensure Node.js 16+ is installed
- Delete `node_modules` and run `npm install` again
- Check that `.env` file exists in frontend directory

### Geocoding fails
- Verify address format
- Check internet connection
- Ensure geocoding service is accessible

### Scraping errors
- Some municipalities may block automated requests
- Consider using official APIs when available
- Check that the municipality has online zoning data

### AI interpretation fails
- Verify OpenAI API key is valid
- Check API credits are available
- Review OpenAI service status

## Next Steps

- Customize scraping for specific municipalities
- Adjust AI prompts for your use case
- Set up production deployment
- Integrate payment processing (Stripe)
- Add user authentication

## Support

For detailed documentation, see [README.md](README.md)
