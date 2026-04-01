# Diego Tomas Dominguez - Portfolio Website

A modern, responsive portfolio website built with Django that showcases my skills, projects, education, and contact information.

## 🚀 Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Smooth Animations**: Scroll-reveal animations and smooth transitions
- **Hamburger Navigation**: Mobile-friendly navigation menu
- **Dynamic Content**: Content managed through Django admin panel
- **Contact Form**: Functional contact form with AJAX submission
- **Modern UI**: Dark theme with clean, professional design
- **Skill Progress Bars**: Visual representation of technical skills
- **Project Showcase**: Display of personal and academic projects

## 🛠️ Tech Stack

### Backend
- **Python 3.x**
- **Django 4.x** - Web framework
- **SQLite** - Database (development)

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS variables
- **JavaScript (ES6+)** - Interactive features
- **Google Fonts** - Typography (Playfair Display & Outfit)

### Development Tools
- **VS Code** - Code editor
- **Git** - Version control

## 📁 Project Structure

```
midterm project dom/
├── tom_project/
│   ├── diego_app/
│   │   ├── migrations/          # Database migrations
│   │   ├── templates/
│   │   │   └── portfolio.html   # Main portfolio template
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── style.css    # Main stylesheet
│   │   │   ├── js/
│   │   │   │   └── script.js    # JavaScript functionality
│   │   │   └── images/
│   │   │       └── profile.jpg  # Profile picture
│   │   ├── admin.py             # Django admin configuration
│   │   ├── models.py            # Database models
│   │   ├── views.py             # View functions
│   │   ├── urls.py              # URL routing
│   │   └── tests.py             # Unit tests
│   └── tom_project/             # Django project settings
├── manage.py                    # Django management script
├── db.sqlite3                   # SQLite database
└── requirements.txt             # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "midterm project dom"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

**Requirements**
   ```
      asgiref==3.11.1
      Django==6.0.3
      pillow==12.1.1
      sqlparse==0.5.5
      tzdata==2025.3

   ```

7. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📝 Usage

### Managing Content

1. **Access Admin Panel**: Go to `/admin` and login with superuser credentials
2. **Add Content**: Use the admin interface to manage:
   - Skills and proficiency levels
   - Projects with descriptions and tags
   - Education records
   - Contact information
   - Home section content

### Customizing

1. **Styles**: Edit `static/css/style.css` for visual changes
2. **Scripts**: Modify `static/js/script.js` for JavaScript functionality
3. **Templates**: Update `templates/portfolio.html` for layout changes
4. **Models**: Modify `models.py` to add new data fields

## 🎨 Design Features

### Responsive Breakpoints
- **Desktop**: > 900px width
- **Tablet**: 560px - 900px width  
- **Mobile**: < 560px width

### Color Scheme
- **Primary**: Dark blue (#0f1c2e)
- **Accent**: Blue (#5b8af5)
- **Text**: White (#f7f6f3)
- **Background**: Various shades of blue-gray

### Animations
- **Scroll Reveal**: Elements fade in and slide up when scrolling
- **Hover Effects**: Interactive feedback on buttons and cards
- **Smooth Transitions**: 0.2-0.65s transitions throughout

## 🔧 Configuration

### Django Settings
Key settings in `tom_project/settings.py`:
- DEBUG mode for development
- Static files configuration
- Media files for uploads
- CSRF and security settings

### Database Models
- **Skill**: Name, description, proficiency level
- **Project**: Name, description, tags, URLs
- **Education**: Level, institution, status, dates
- **ContactInfo**: Type, label, value, URL
- **HomeSection**: Profile image, name, bio

## 🐛 Troubleshooting

### Common Issues

1. **Hamburger menu not working**
   - Ensure browser width is < 900px
   - Check browser console for JavaScript errors
   - Verify CSS classes match between HTML and JS

2. **Images not displaying**
   - Check static files configuration
   - Verify image paths in templates
   - Run `python manage.py collectstatic` for production

3. **Admin panel not accessible**
   - Create superuser: `python manage.py createsuperuser`
   - Check URLs configuration
   - Verify admin.py registrations

4. **Styles not loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_URL settings
   - Verify CSS file paths

## 📱 Mobile Features

- **Hamburger Menu**: Collapsible navigation for small screens
- **Touch-Friendly**: Large tap targets and proper spacing
- **Responsive Grid**: Adaptive layouts for different screen sizes
- **Optimized Images**: Proper scaling and performance

## 🚀 Deployment

### Production Setup
1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Set up production database (PostgreSQL recommended)
4. Configure static files serving
5. Set up domain and SSL
6. Use Gunicorn or similar WSGI server

### Environment Variables
Consider using `.env` file for:
- `SECRET_KEY`
- `DEBUG` setting
- Database credentials
- Email settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Diego Tomas Dominguez**
- Student Developer
- Negros Oriental State University
- Email: [myladtomdominguez@gmail.com]

## 🙏 Acknowledgments

- Django Documentation and Community
- Google Fonts for typography
- Stack Overflow community support
- Open source libraries and tools

---
