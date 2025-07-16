# Portfolio Website

## Overview
This is a personal portfolio website for Yuvraj, a Computer Science student and software developer. The website is built using Flask (Python web framework) and features a modern, responsive design with sections for about, skills, projects, blog posts, and contact information.

## User Preferences
Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default templating engine)
- **CSS Framework**: TailwindCSS (loaded via CDN)
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter family)
- **JavaScript**: Vanilla JavaScript for basic interactions
- **Responsive Design**: Mobile-first approach using TailwindCSS utilities

The frontend follows a traditional server-side rendered approach where HTML templates are rendered on the server and sent to the client. The design uses a modern dark theme with blue accent colors.

### Backend Architecture
- **Framework**: Flask (Python micro web framework)
- **Structure**: Simple MVC-like pattern with separated routes
- **Session Management**: Flask sessions with configurable secret key
- **Error Handling**: Custom 404 error handler
- **Logging**: Python's built-in logging module for debugging and monitoring

The backend is minimal and lightweight, suitable for a portfolio site that primarily serves static content with basic form handling.

## Key Components

### 1. Application Structure
- `app.py`: Main Flask application factory and configuration
- `main.py`: Entry point for running the application
- `routes.py`: Route handlers for all endpoints
- `templates/`: HTML templates using Jinja2
- `static/`: CSS, JavaScript, and other static assets
- `data/`: JSON and Python files containing portfolio data

### 2. Data Management
- **Resume Data**: Stored in `data/resume_data.py` as a Python dictionary
- **Blog Posts**: Stored in `data/blog_posts.json` as JSON
- **No Database**: Uses file-based data storage for simplicity

### 3. Frontend Components
- **Navigation**: Fixed header with smooth scrolling navigation
- **Hero Section**: Introduction with call-to-action buttons
- **About Section**: Personal information and journey
- **Skills Section**: Technical and soft skills with visual indicators
- **Projects Section**: Portfolio projects with details and links
- **Blog Section**: Recent blog posts with metadata
- **Contact Section**: Contact form for visitor inquiries

### 4. Responsive Design
- Mobile-first responsive design using TailwindCSS
- Collapsible mobile navigation menu
- Flexible grid layouts that adapt to different screen sizes
- Touch-friendly interface elements

## Data Flow

### 1. Page Rendering
1. User requests the homepage (`/`)
2. Flask loads resume data from `data/resume_data.py`
3. Flask loads blog posts from `data/blog_posts.json`
4. Template is rendered with combined data
5. HTML response is sent to the client

### 2. Contact Form Submission
1. User submits contact form via POST to `/contact`
2. Flask validates form data (basic validation)
3. Contact information is logged to console
4. Flash message is set for user feedback
5. User is redirected back to the contact section

### 3. Static Asset Serving
- CSS, JavaScript, and images are served directly by Flask
- External dependencies (TailwindCSS, Font Awesome) loaded via CDN

## External Dependencies

### 1. Frontend Dependencies (CDN)
- **TailwindCSS**: Utility-first CSS framework for styling
- **Font Awesome**: Icon library for UI elements
- **Google Fonts**: Web fonts (Inter family)

### 2. Python Dependencies
- **Flask**: Web framework
- **Werkzeug**: WSGI utilities (ProxyFix middleware)

### 3. Runtime Dependencies
- Python 3.x environment
- Web server capability (development server included)

## Deployment Strategy

### 1. Development Environment
- Flask development server on port 5000
- Debug mode enabled for development
- Environment variables for configuration (SESSION_SECRET)

### 2. Production Considerations
- ProxyFix middleware configured for reverse proxy deployment
- Session secret should be set via environment variable
- Logging configured for debugging (should be adjusted for production)
- Static files served by Flask (consider CDN or dedicated static server for production)

### 3. Configuration
- Environment-based configuration using `os.environ`
- Debug mode and secret key configurable
- Host and port settings ready for deployment platforms

## Notable Features

### 1. Contact Form Handling
- Basic form validation
- Flash messaging for user feedback
- Logging of contact submissions (placeholder for email integration)

### 2. Error Handling
- Custom 404 error page handling
- Exception logging throughout the application

### 3. SEO and Accessibility
- Semantic HTML structure
- Responsive meta tags
- Smooth scrolling navigation
- Accessible color contrast (dark theme)

### 4. Performance Considerations
- Minimal server-side processing
- CDN-hosted external dependencies
- Lightweight static asset structure

The architecture is designed for simplicity and ease of maintenance, making it suitable for a personal portfolio website that doesn't require complex database operations or user authentication systems.