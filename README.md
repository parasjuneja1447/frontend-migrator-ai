# AI Frontend Migrator 🚀

An intelligent web scraping and component analysis tool that uses AI to extract and convert website sections into reusable UI components.

## Overview

The AI Frontend Migrator is a FastAPI-based service that automates the process of analyzing web pages and converting their sections into structured UI components using Google's Gemini AI. Perfect for frontend developers looking to migrate or refactor existing websites into component-based architectures.

## Features

✨ **Web Page Analysis** - Extracts HTML from live websites  
🤖 **AI-Powered Component Detection** - Uses Gemini AI to intelligently identify and categorize UI components  
🔄 **Duplicate Removal** - Automatically deduplicates extracted components  
📸 **Screenshots** - Captures screenshots of analyzed pages  
⚡ **Fast & Async** - Built with FastAPI for high performance

## Tech Stack

- **Backend**: FastAPI
- **AI/ML**: Google Gemini 2.5 Flash API
- **Web Scraping**: Playwright
- **Language**: Python
- **Package Management**: npm/pip

## Project Structure

```
ai-frontend-migrator/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── agents/
│   │   ├── reader.py          # Web page reader using Playwright
│   │   ├── parser.py          # HTML parser
│   │   └── analyzer.py        # AI-powered component analyzer
│   ├── services/
│   │   ├── gemini_service.py  # Google Gemini API integration
│   │   └── openai_service.py  # OpenAI API integration (optional)
│   └── utils/
│       ├── removeDuplicates.py # Utility to remove duplicate components
│       └── is_noise.py         # Utility for noise detection
├── package.json               # Node.js dependencies
├── .env                       # Environment variables
└── README.md                  # This file
```

## Prerequisites

- Python 3.8+
- Node.js 14+
- Google Gemini API Key
- Chromium/Chrome browser (for Playwright)

## Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd ai-frontend-migrator
```

2. **Install Python dependencies**

```bash
pip install fastapi uvicorn playwright google-genai python-dotenv
```

3. **Install Node dependencies**

```bash
npm install
```

4. **Install Playwright browsers**

```bash
playwright install chromium
```

## Configuration

1. **Create a `.env` file** in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here  # Optional
```

2. **Obtain API Keys**:
   - [Google Gemini API](https://ai.google.dev/)
   - [OpenAI API](https://platform.openai.com/) (optional)

## Usage

### Start the Server

```bash
uvicorn app.main:app --reload
```

The server will start on `http://127.0.0.1:8000`

### API Endpoints

#### Home

```
GET /
```

Returns a simple welcome message.

**Response:**

```json
{
  "message": "AI Migration Agent Running 🚀"
}
```

#### Analyze Page

```
GET /analyze?url=https://example.com
```

Analyzes a website and extracts UI components.

**Parameters:**

- `url` (required): The URL of the website to analyze

**Response:**

```json
{
  "sections": [...],
  "components": [
    {
      "component": "Hero",
      "props": {
        "title": "Welcome to our site"
      }
    },
    ...
  ]
}
```

### Example

```bash
curl "http://127.0.0.1:8000/analyze?url=https://example.com"
```

## How It Works

1. **Reader** - Fetches the website using Playwright and captures HTML
2. **Parser** - Extracts structured sections from the HTML
3. **Analyzer** - Uses Gemini AI to convert sections into component definitions
4. **Deduplication** - Removes duplicate components from results
5. **Response** - Returns JSON with extracted components and their properties

## Key Modules

### `app/agents/reader.py`

Uses Playwright to navigate to URLs, capture page content, and take screenshots.

### `app/agents/analyzer.py`

Sends website sections to Gemini AI and parses the response into component objects.

### `app/services/gemini_service.py`

Handles communication with the Google Gemini API.

### `app/utils/removeDuplicates.py`

Deduplicates extracted components to avoid redundant results.

## Development

### Running Tests

```bash
npm test
```

### Code Structure

- All agent logic is modular and can be imported independently
- Services are abstracted for easy API swapping
- Utility functions are separated for reusability

## Troubleshooting

**Issue: Playwright browser not found**

```bash
playwright install chromium
```

**Issue: API key errors**

- Ensure `.env` file is properly configured
- Verify API keys are valid and active

**Issue: Timeout on large pages**

- Increase the `timeout` parameter in `reader.py`
- Consider analyzing specific pages or sections

## Future Enhancements

- Support for multiple AI providers (OpenAI, Claude)
- Component generation in various frameworks (React, Vue, Angular)
- Batch URL processing
- Custom component templates
- Web UI dashboard

## License

ISC

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

---

**Built with ❤️ using FastAPI and Google Gemini AI**
