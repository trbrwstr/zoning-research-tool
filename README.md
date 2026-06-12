# Zoning Research Tool

A client-ready zoning research and permit intelligence product built for real estate, architecture, construction, and land-use teams that need faster answers before committing time, money, or staff to a property decision.

This project demonstrates the kind of practical, AI-assisted web application I build for freelance clients on Fiverr and Upwork: focused workflows, clean interfaces, API integrations, automation, and deployable full-stack foundations.

## What This Product Does

The Zoning Research Tool helps turn a property address into an organized zoning research package. Instead of manually searching assessor sites, zoning maps, municipal code pages, and permit portals, the application is designed to collect and summarize the information a stakeholder needs to begin evaluating a site.

Typical outputs include:

- Zoning district and description
- Setback requirements
- Height limits
- Lot coverage rules
- Parking requirements
- Permitted and conditional uses
- Parcel and location context
- Permit process guidance
- Potential development issues
- Plain-English AI summaries for faster review

> Important: zoning and permit decisions should always be verified with the applicable municipality, licensed design professionals, and legal counsel before purchase, design, financing, or construction decisions are made.

## Who It Helps

This type of system is useful for:

- Real estate investors screening parcels
- Developers comparing acquisition opportunities
- Architects preparing early feasibility notes
- Contractors answering client questions
- Permit expediters organizing jurisdiction-specific requirements
- Brokers and consultants who want a faster first-pass research workflow
- Local businesses that need custom internal research automation

## Freelance Services Available

I can adapt this project into a paid client solution or use it as a starting point for related automation tools.

### Custom Web Applications

- Full-stack business dashboards
- Client portals
- Internal admin tools
- Search and reporting workflows
- Form-heavy operational systems
- Lightweight SaaS MVPs

### AI-Assisted Research Tools

- Document summarization
- Municipal or regulatory research assistants
- Property and zoning research workflows
- Lead qualification tools
- Structured report generation
- Retrieval-augmented knowledge tools

### Automation and Data Collection

- Public website data extraction where permitted
- API integrations
- Spreadsheet-to-dashboard workflows
- Report generation pipelines
- Notification and monitoring systems
- Data cleanup and transformation tools

### Product and MVP Support

- Scope planning
- Feature prioritization
- UX flow design
- Technical architecture
- Prototype development
- Deployment preparation
- Security and maintainability review

## Why Work With Me

I build practical software that is meant to be used, not just demonstrated. My approach is simple:

1. Clarify the business goal.
2. Reduce the idea to the smallest useful version.
3. Build a clean and maintainable implementation.
4. Test the core workflow.
5. Leave room for iteration, automation, and scale.

For freelance clients, that means clear communication, realistic tradeoffs, and software that solves the immediate problem without unnecessary complexity.

## Example Client Use Cases

This codebase can be adapted for projects such as:

- A real estate feasibility lookup tool for a local market
- A permit checklist generator for contractors
- A zoning summary dashboard for architects
- A municipal code research assistant
- A parcel intake and due-diligence workflow
- A paid lookup portal for consultants
- An internal research tool for acquisition teams

## Product Capabilities

- Address-based research workflow
- AI-powered interpretation of complex zoning text
- Municipal data scraping and integration architecture
- Interactive map support through Mapbox
- REST API endpoints for programmatic access
- Pricing-ready structure for per-lookup or subscription models
- Frontend and backend separation for easier deployment and scaling
- Configurable data sources for different jurisdictions

## Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- OpenAI API integration
- BeautifulSoup and Selenium for data collection workflows
- Geocoding services
- Mapbox integration

### Frontend

- React
- TailwindCSS
- Mapbox GL
- Axios
- Lucide React icons

## How a Client Project Usually Works

### 1. Discovery

We define the target users, workflow, required data sources, budget, and success criteria.

### 2. Prototype

I build the smallest version that proves the workflow: input, processing, output, and basic user experience.

### 3. Integration

We connect APIs, databases, maps, AI models, payment systems, dashboards, or third-party services as needed.

### 4. Review and Hardening

I clean up edge cases, improve error handling, review sensitive data exposure, and prepare the app for real use.

### 5. Handoff or Ongoing Support

You can receive the code, documentation, deployment guidance, and optional follow-up iterations.

## Customization Options

Depending on the client need, this project can be customized with:

- Jurisdiction-specific zoning logic
- Branded report templates
- PDF exports
- User accounts and saved searches
- Payment integration
- Admin dashboards
- CRM or spreadsheet exports
- Email delivery
- More detailed source citations
- Human review workflows
- Role-based access control

## Quality and Security Priorities

For client work, I prioritize:

- Clear, readable code
- Minimal dependencies where possible
- Input validation
- Least-privilege API key handling
- Environment-based configuration
- Separation of frontend and backend concerns
- Practical error messages
- Maintainable project structure
- Honest documentation about limitations

## Local Development Preview

This repository includes a full-stack application structure with a Python backend and React frontend.

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API documentation is available locally at:

```text
http://localhost:8000/docs
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm start
```

The web application is available locally at:

```text
http://localhost:3000
```

## Required Configuration

Typical environment variables include:

```text
OPENAI_API_KEY=your_openai_api_key
MAPBOX_ACCESS_TOKEN=your_mapbox_token
DATABASE_URL=your_database_url
REACT_APP_MAPBOX_TOKEN=your_mapbox_token
REACT_APP_API_URL=http://localhost:8000
```

Client deployments can be configured for the preferred hosting provider, database, domain, payment provider, and API vendors.

## Data Source Notice

Municipal data systems vary widely. Some jurisdictions offer reliable GIS APIs; others rely on PDFs, HTML pages, portals, or manual confirmation. Any production deployment should be tailored to the specific jurisdictions and data sources that matter to the client.

Where official APIs are available, they are preferred over scraping. Where scraping is used, it should respect site terms, robots policies, rate limits, and applicable law.

## Accuracy Disclaimer

This software is intended to support preliminary research and workflow automation. It is not a substitute for official municipal determinations, professional legal advice, licensed architectural review, engineering review, surveying, title review, or permitting authority decisions.

Users should independently verify all zoning, parcel, building, and permit information with official sources before relying on it for financial, legal, construction, or development decisions.

## Contact and Availability

I am available for freelance projects through Fiverr and Upwork, including custom software builds, automation tools, MVP development, AI-assisted workflows, and practical internal business applications.

If you are reviewing this repository as a potential client, please reach out with:

- A short description of the workflow you want to improve
- The users who will rely on it
- The data sources or systems involved
- Your desired timeline
- Any examples, spreadsheets, screenshots, or current manual process notes

## Legal

Copyright © 2026. All rights reserved.

All source code, documentation, designs, workflows, concepts, product names, and related materials in this repository are proprietary unless a separate written agreement states otherwise. No part of this repository may be copied, reproduced, distributed, sublicensed, sold, transferred, modified, published, displayed, or used to create derivative works without prior written permission from the rights holder.

Unauthorized use, reproduction, distribution, or commercial exploitation of this repository or any portion of its contents is strictly prohibited. Access to this repository does not grant any license, ownership interest, intellectual property right, or permission to use the materials for any purpose except review as expressly authorized by the rights holder.

All trademarks, service marks, third-party APIs, platform names, and external services referenced in this repository remain the property of their respective owners.
