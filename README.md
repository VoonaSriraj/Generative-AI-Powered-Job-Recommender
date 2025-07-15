# AI Job Recommender

A comprehensive AI-powered job recommendation system that analyzes resumes and provides personalized job suggestions from LinkedIn and Naukri platforms. The application uses advanced language models to extract insights from resumes and identify skill gaps while providing career roadmaps.

## Features

- **Resume Analysis**: Extract and analyze text from PDF resumes
- **Skill Gap Analysis**: Identify missing skills and certifications for better job opportunities
- **Career Roadmap**: Generate personalized career development suggestions
- **Job Recommendations**: Fetch relevant job listings from LinkedIn and Naukri
- **Interactive Web Interface**: User-friendly Streamlit-based interface
- **MCP Server Integration**: Model Context Protocol server for external integrations

## Project Structure

```
job-recommender/
├── app.py                 # Main Streamlit application
├── mcp_server.py          # MCP server implementation
├── requirements.txt       # Python dependencies
├── src/
│   ├── __init__.py
│   ├── helper.py         # PDF processing and AI utilities
│   └── job_api.py        # Job scraping APIs
└── README.md
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-job-recommender.git
   cd ai-job-recommender
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   APIFY_API_KEY=your_apify_api_key_here
   ```

## API Keys Required

- **Groq API Key**: For AI-powered resume analysis and text generation
- **Apify API Key**: For web scraping job listings from LinkedIn and Naukri

## Usage

### Running the Streamlit Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### Using the MCP Server

```bash
python mcp_server.py
```

The MCP server will run on `http://0.0.0.0:8501`

### Application Workflow

1. **Upload Resume**: Upload a PDF resume through the web interface
2. **Resume Analysis**: The system extracts text and generates:
   - Resume summary highlighting skills, education, and experience
   - Skill gap analysis identifying missing competencies
   - Future roadmap with learning recommendations
3. **Job Recommendations**: Click "Get Job Recommendations" to:
   - Extract relevant job keywords from resume
   - Fetch matching jobs from LinkedIn and Naukri
   - Display results with direct links to job postings

## Technical Implementation

### Core Components

**Resume Processing (`src/helper.py`)**
- PDF text extraction using PyMuPDF
- Integration with Groq's LLaMA model for text analysis
- Configurable token limits for different analysis types

**Job Scraping (`src/job_api.py`)**
- LinkedIn job scraping using Apify's LinkedIn Jobs Scraper
- Naukri job scraping using Apify's Naukri Jobs Scraper
- Configurable search parameters (location, number of results)

**Web Interface (`app.py`)**
- Streamlit-based responsive design
- Real-time progress indicators
- Formatted output with custom styling

**MCP Server (`mcp_server.py`)**
- FastMCP implementation for external integrations
- Async job fetching tools
- HTTP transport protocol

### AI Model Integration

The application uses Groq's LLaMA 3.1 8B model for:
- Resume summarization
- Skill gap identification
- Career roadmap generation
- Job keyword extraction

## Dependencies

- **streamlit**: Web application framework
- **pymupdf**: PDF text extraction
- **langchain-groq**: Groq API integration
- **langchain**: LLM framework utilities
- **apify-client**: Web scraping client
- **python-dotenv**: Environment variable management
- **groq**: Direct Groq API client

## Configuration

### Job Search Parameters

- **Default Location**: India (configurable)
- **Default Results**: 60 jobs per platform
- **Supported Platforms**: LinkedIn, Naukri

### AI Model Settings

- **Model**: llama-3.1-8b-instant
- **Temperature**: 0.5
- **Max Tokens**: Configurable per analysis type

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please create an issue in the GitHub repository.

## Future Enhancements

- Support for additional job platforms
- Enhanced resume parsing for multiple formats
- Machine learning-based job matching
- User authentication and job tracking
- Integration with calendar applications for interview scheduling
- Advanced analytics and reporting features
