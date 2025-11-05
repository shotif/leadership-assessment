# Leadership Assesser

A Flask web application for evaluating leadership competencies according to the Croatian leadership model described in the functional specification. The app provides a secure dashboard, visualizations, and optional AI-powered insights via the Google Gemini API.

## Features
- Email/password authentication with Standard and Master roles.
- CRUD interface for leadership assessments with automatic score and category calculation.
- Dashboard with aggregated category summary.
- Visualization workspace featuring:
  - Adequacy/Potential matrix scatter plot.
  - Individual radar chart with behavioral descriptions and AI insight generation.
  - Side-by-side radar chart comparison for two individuals.
- Pluggable storage layer backed by JSON files (simulating cloud storage) with automatic seeding of demo users.

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Configure environment variables to customize seeded users and AI integration:
   - `LEADERSHIP_APP_DEFAULT_PASSWORD` – password for created demo accounts (default: `ChangeMe123!`).
   - `LEADERSHIP_APP_MASTER_EMAIL` – email for the seeded master account.
   - `LEADERSHIP_APP_STANDARD_EMAIL` – email for the seeded standard account.
   - `GOOGLE_GEMINI_API_KEY` – API key used to generate AI insights.
   - `GOOGLE_GEMINI_MODEL` – (optional) Gemini model name, defaults to `models/gemini-1.5-flash`.
3. Run the application:
   ```bash
   flask --app app.py run --debug
   ```
4. Navigate to `http://localhost:5000`, sign in with one of the seeded accounts, and begin working with assessments.

## Project Structure
```
app/
├── __init__.py
├── data/
├── domain.py
├── routes.py
├── services.py
├── static/
│   ├── styles.css
│   └── visualizations.js
└── templates/
    ├── assessment_form.html
    ├── base.html
    ├── dashboard.html
    ├── login.html
    └── visualizations.html
app.py
requirements.txt
```

## Notes
- All data is stored in JSON files under `app/data`. In production this module can be adapted to use Google Cloud Storage or another persistent store.
- The Google Gemini integration is optional. If the API key is not configured, the app displays a helpful message instead of generated insights.
