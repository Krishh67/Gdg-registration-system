# Email Configuration Template for GDG Registration System
# Copy this file to 'config.py' and fill in your actual credentials

EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'username': 'your-email@gmail.com',  # Replace with your Gmail address
    'password': 'your-app-password',     # Replace with your Gmail App Password
    'from_email': 'your-email@gmail.com' # Replace with your Gmail address
}

# Event Details
EVENT_CONFIG = {
    'name': 'GDG TechTalk Seminar',
    'date': 'December 15, 2024',
    'time': '2:00 PM - 5:00 PM',
    'venue': 'GDG Innovation Center'
}

# Instructions:
# 1. Copy this file to 'config.py'
# 2. Replace 'your-email@gmail.com' with your actual Gmail
# 3. Replace 'your-app-password' with your 16-digit Gmail App Password
# 4. Customize event details as needed
# 5. Never commit config.py to version control! 