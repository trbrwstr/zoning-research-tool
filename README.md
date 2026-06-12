# Zoning Research Tool

An AI-powered zoning and permit research tool for real estate developers, architects, and contractors. Get comprehensive zoning summaries, setback requirements, and permit processes in seconds.

## Features

- **Instant Zoning Analysis**: Enter any US address to get comprehensive zoning information
- **AI-Powered Interpretation**: GPT-4 interprets complex zoning codes into actionable insights
- **Municipal Data Scraping**: Automatically scrapes county assessor sites and municipal portals
- **Interactive Maps**: Mapbox visualization of property boundaries and locations
- **Comprehensive Reports**: Setbacks, height restrictions, lot coverage, parking requirements, and more
- **Flexible Pricing**: Pay per lookup or monthly subscription

## Tech Stack

### Backend
- **Python 3.9+**
- **FastAPI**: Modern, fast web framework
- **SQLAlchemy**: Database ORM
- **OpenAI GPT-4**: AI-powered code interpretation
- **BeautifulSoup4 & Selenium**: Web scraping
- **Geopy**: Geocoding services
- **Mapbox**: Mapping and visualization

### Frontend
- **React 18**
- **TailwindCSS**: Styling
- **Mapbox GL**: Interactive maps
- **Lucide React**: Icons
- **Axios**: HTTP client

## Installation

### Prerequisites
- Python 3.9 or higher
- Node.js 16 or higher
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure:
```bash
cp .env.example .env
```

5. Edit `.env` and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
MAPBOX_ACCESS_TOKEN=your_mapbox_token
```

6. Initialize the database:
```bash
python -c "from app.models.database import engine, Base; Base.metadata.create_all(bind=engine)"
```

7. Start the backend server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
API documentation: `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Copy the example environment file and configure:
```bash
cp .env.example .env
```

4. Edit `.env` and add your Mapbox token:
```
REACT_APP_MAPBOX_TOKEN=your_mapbox_token
REACT_APP_API_URL=http://localhost:8000
```

5. Start the frontend development server:
```bash
npm start
```

The application will be available at `http://localhost:3000`

## Usage

### Web Interface

1. Open your browser to `http://localhost:3000`
2. Enter a property address in the search field
3. Click "Research" to initiate the zoning lookup
4. View the comprehensive zoning analysis including:
   - Zoning code and description
   - Setback requirements
   - Height restrictions
   - Lot coverage limits
   - Parking requirements
   - Permitted uses
   - Potential issues
   - AI-powered recommendations

### API Usage

The API provides RESTful endpoints for programmatic access:

#### Zoning Lookup
```bash
POST /api/zoning/lookup
Content-Type: application/json

{
  "address": "123 Main St, San Francisco, CA",
  "municipality": "San Francisco",
  "state": "CA"
}
```

#### Get Lookup Result
```bash
GET /api/zoning/lookup/{lookup_id}
```

#### Pricing Information
```bash
GET /api/pricing/info
```

See full API documentation at `http://localhost:8000/docs`

## API Reference

### Endpoints

#### Zoning
- `POST /api/zoning/lookup` - Create a new zoning lookup
- `GET /api/zoning/lookup/{id}` - Get lookup results
- `GET /api/zoning/history` - Get lookup history

#### Users
- `POST /api/users/register` - Register a new user
- `GET /api/users/me` - Get current user info

#### Subscriptions
- `POST /api/subscriptions/create` - Create subscription
- `GET /api/subscriptions/user/{user_id}` - Get user subscription

#### Pricing
- `GET /api/pricing/info` - Get pricing information

## Configuration

### Environment Variables

#### Backend (.env)
- `OPENAI_API_KEY` - OpenAI API key for GPT-4
- `MAPBOX_ACCESS_TOKEN` - Mapbox access token
- `DATABASE_URL` - Database connection string
- `PRICE_PER_LOOKUP` - Price per lookup (default: 9.99)
- `MONTHLY_SUBSCRIPTION_PRICE` - Monthly subscription price (default: 99.00)

#### Frontend (.env)
- `REACT_APP_MAPBOX_TOKEN` - Mapbox access token
- `REACT_APP_API_URL` - Backend API URL

## Architecture

### Backend Structure
```
backend/
├── app/
│   ├── api/           # API endpoints
│   ├── core/          # Core configuration
│   ├── models/        # Database models
│   ├── services/      # Business logic
│   │   ├── geocoding.py
│   │   ├── scraping.py
│   │   ├── ai_interpretation.py
│   │   └── mapbox_service.py
│   └── utils/         # Utility functions
├── requirements.txt
└── .env.example
```

### Frontend Structure
```
frontend/
├── src/
│   ├── components/    # React components
│   │   ├── ZoningLookupForm.js
│   │   ├── ZoningResults.js
│   │   ├── MapView.js
│   │   └── PricingModal.js
│   ├── App.js
│   └── index.js
├── package.json
└── .env.example
```

## Data Sources

The tool integrates with various municipal data sources:

- **County Assessor Websites**: Property records and parcel data
- **Municipal GIS APIs**: Zoning boundaries and codes
- **Zoning Portals**: Official zoning ordinances and regulations
- **Building Department Sites**: Permit processes and requirements

Note: Each municipality has different data systems. The scraping modules are designed to be customizable per jurisdiction.

## Development

### Adding New Municipalities

To add support for a new municipality:

1. Update `app/services/scraping.py` with municipality-specific selectors
2. Add GIS API endpoints if available
3. Test with sample addresses
4. Add error handling for municipality-specific issues

### Customizing AI Prompts

Edit the prompts in `app/services/ai_interpretation.py` to customize the AI interpretation for specific use cases or jurisdictions.

## Pricing

- **Per Lookup**: $9.99 per property
- **Monthly Subscription**: $99/month (100 lookups included)

Pricing can be customized via environment variables.

## Limitations

- Data availability varies by municipality
- Some counties may require API access keys
- Real-time data accuracy depends on municipal source systems
- Always verify zoning information with official sources before making decisions

## Troubleshooting

### Geocoding Failures
- Ensure the address is properly formatted
- Check internet connectivity
- Verify geocoding API key if using a premium service

### Scraping Issues
- Municipal websites may change structure
- Some sites may block automated requests
- Consider using official APIs when available

### AI Interpretation Errors
- Check OpenAI API key is valid
- Verify API credits are available
- Review prompt for specific jurisdiction requirements

## License

Proprietary - All rights reserved

## Support

For support, contact the development team or open an issue in the project repository.
