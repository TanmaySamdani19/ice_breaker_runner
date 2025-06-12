# IceBreaker Pro 🤝

**Professional Networking Made Easy with AI-Powered Insights**

IceBreaker Pro is a cutting-edge web application that revolutionizes professional networking by generating personalized outreach emails based on LinkedIn profile analysis. Using advanced AI and web scraping technologies, it creates meaningful connections through data-driven insights.

![IceBreaker Pro](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-Latest-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange)

## ✨ Features

- **🔍 Intelligent Profile Analysis**: Automatically discovers and analyzes LinkedIn profiles using AI agents
- **📧 Personalized Email Generation**: Creates customized outreach emails with multiple tone and length options
- **🎨 Modern UI**: Beautiful, responsive interface with glassmorphism design and smooth animations
- **⚡ Real-time Processing**: Fast profile lookup and email generation
- **📋 One-Click Copy**: Easy email copying to clipboard functionality
- **🎯 Purpose-Driven**: Tailored emails for networking, job inquiries, collaboration, and introductions

## 🚀 Demo

Enter any professional's name, and IceBreaker Pro will:
1. Find their LinkedIn profile using AI-powered search
2. Extract key insights and professional highlights
3. Generate personalized outreach emails based on your preferences
4. Provide ready-to-send content with proper formatting

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework for Python
- **LangChain**: AI orchestration and prompt engineering
- **OpenAI GPT-4**: Language model for content generation
- **Pydantic**: Data validation and parsing
- **Requests**: HTTP library for API calls

### Frontend
- **HTML5/CSS3**: Modern responsive design
- **JavaScript (ES6+)**: Interactive functionality
- **Font Awesome**: Icon library
- **Google Fonts**: Typography (Inter font family)

### APIs & Services
- **Scrapin.io**: LinkedIn profile data extraction
- **Tavily Search**: Web search capabilities for profile discovery
- **OpenAI API**: AI-powered text generation

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package manager)
- API keys for the following services:
  - OpenAI API key
  - Scrapin.io API key
  - Tavily API key

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/icebreaker-pro.git
   cd icebreaker-pro
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SCRAPIN_API_KEY=your_scrapin_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   
   Navigate to `http://localhost:5000`

## 🔧 Configuration

### Email Generation Options

The application supports various customization options:

- **Length Options**:
  - Short & Concise (3-4 sentences)
  - Medium Length (2-3 paragraphs)
  - Detailed & Comprehensive (multiple paragraphs)

- **Tone Options**:
  - Professional (formal business language)
  - Friendly & Warm (approachable yet professional)
  - Casual & Relaxed (conversational style)

- **Purpose Options**:
  - Professional Networking
  - Job Opportunity Inquiry
  - Collaboration Proposal
  - Introduction & Connection

## 📁 Project Structure

```
icebreaker-pro/
├── app.py                     # Main Flask application
├── ice_breaker.py            # Core profile analysis logic
├── email_generator.py        # Email generation functionality
├── output_parsers.py         # Pydantic models for data validation
├── agents/
│   └── linkedin_lookup_agents.py  # AI agent for profile discovery
├── third_parties/
│   └── linkedin.py          # LinkedIn profile scraping
├── tools/
│   └── tools.py             # Utility tools for web search
├── templates/
│   └── index.html           # Main webpage template
├── static/                  # Static assets (if any)
├── .env                     # Environment variables (create this)
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔑 API Keys Setup

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account or sign in
3. Navigate to API Keys section
4. Create a new API key
5. Add to your `.env` file

### Scrapin.io API Key
1. Visit [Scrapin.io](https://scrapin.io/)
2. Sign up for an account
3. Get your API key from the dashboard
4. Add to your `.env` file

### Tavily API Key
1. Visit [Tavily](https://tavily.com/)
2. Create an account
3. Obtain your API key
4. Add to your `.env` file

## 🎯 Usage Examples

### Basic Usage
1. Enter a professional's name in the search field
2. Click "Analyze Profile"
3. Review the generated insights and facts
4. Customize email preferences (length, tone, purpose)
5. Click "Generate Email"
6. Copy the personalized email to your clipboard

### Advanced Features
- **Regenerate Email**: Click "Regenerate" to create alternative versions
- **Multiple Purposes**: Switch between networking, job inquiries, and collaboration
- **Tone Adjustment**: Adapt the communication style to your relationship

## 🔧 Development

### Running in Development Mode
```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python app.py
```

### Testing Components
Individual components can be tested:

```bash
# Test email generator
python email_generator.py

# Test ice breaker functionality
python ice_breaker.py

# Test LinkedIn scraping
python third_parties/linkedin.py
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guidelines for Python code
- Add comments for complex functionality
- Update documentation for new features
- Test your changes thoroughly

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛡️ Privacy & Ethics

IceBreaker Pro is designed with privacy and ethical considerations in mind:

- **Data Usage**: Profile data is processed temporarily and not stored permanently
- **Respectful Outreach**: Generated emails encourage genuine, professional communication
- **API Compliance**: All integrations follow respective API terms of service
- **User Responsibility**: Users are responsible for ethical use of generated content

## 🚨 Troubleshooting

### Common Issues

**Issue**: API Key errors
- **Solution**: Verify all API keys are correctly set in the `.env` file

**Issue**: Profile not found
- **Solution**: Try using the full name or check spelling

**Issue**: Email generation fails
- **Solution**: Ensure OpenAI API key has sufficient credits

**Issue**: Slow response times
- **Solution**: Check internet connection and API service status

### Error Messages
- `TAVILY_API_KEY not found`: Add Tavily API key to `.env` file
- `SCRAPIN_API_KEY not found`: Add Scrapin.io API key to `.env` file
- `Network response was not ok`: Check API service availability

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/icebreaker-pro/issues) page
2. Create a new issue with detailed information
3. Contact the development team

## 🔮 Future Enhancements

- [ ] Support for multiple social platforms (Twitter, GitHub)
- [ ] Email template library
- [ ] CRM integration capabilities
- [ ] Advanced analytics and tracking
- [ ] Mobile application
- [ ] Team collaboration features
- [ ] Custom AI model training

## 📊 Performance

- **Profile Analysis**: ~3-5 seconds
- **Email Generation**: ~2-3 seconds
- **Concurrent Users**: Supports multiple simultaneous requests
- **Uptime**: 99.9% availability target

## 🏆 Acknowledgments

- OpenAI for providing powerful language models
- LangChain community for excellent AI orchestration tools
- Flask team for the robust web framework
- All contributors and beta testers

---

**Made with ❤️ for better professional networking**

*IceBreaker Pro - Breaking the ice, one personalized email at a time.*