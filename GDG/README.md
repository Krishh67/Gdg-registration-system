# GDG - Google Developers Club

A crazy animated landing page and event registration portal built with Python Flask.

## Features

- 🎨 **Crazy Animated Landing Page**: Particle network, floating GDG letters, CRT effects, and colorful blobs
- 📝 **Event Registration Portal**: Form with validation for Name, Email, and Phone
- 💾 **Data Storage**: JSON file-based storage (no database required)
- ✅ **Form Validation**: Server-side validation with error handling
- 🗑️ **Manage Registrations**: Delete individual or clear all registrations
- 📊 **Export Data**: Download registrations as JSON or CSV
- 🎯 **No JavaScript Dependencies**: Pure Python backend with minimal inline JS

## Setup

1. **Install Python** (3.8 or higher)
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Navigate to the project directory**:
   ```bash
   cd GDG
   ```

2. **Run the Flask app**:
   ```bash
   python app.py
   ```

3. **Open your browser** and go to:
   ```
   http://localhost:8000
   ```

## Project Structure

```
GDG/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── registrations.json     # Data storage (created automatically)
├── static/
│   └── css/
│       ├── styles.css     # Landing page styles
│       └── register.css   # Registration page styles
└── templates/
    ├── index1.html        # Landing page template
    └── register.html      # Registration page template
```

## API Endpoints

- `GET /` - Landing page
- `GET /register` - Registration page
- `POST /api/register` - Submit registration
- `GET /api/registrations` - Get all registrations
- `DELETE /api/registrations/<id>` - Delete specific registration
- `DELETE /api/registrations/clear` - Clear all registrations
- `GET /export/json` - Export as JSON
- `GET /export/csv` - Export as CSV

## Data Storage

Registrations are stored in `registrations.json` with the following structure:
```json
{
  "id": "id-20241203225200",
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1 555 123 4567",
  "created_at": "2024-12-03T22:52:00"
}
```

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Minimal JavaScript
- **Storage**: JSON file
- **Styling**: Custom CSS with animations and responsive design

## Browser Support

- Chrome/Edge (recommended)
- Firefox
- Safari
- Mobile browsers

---

Built with ❤️ for GDG (Google Developers Club) 