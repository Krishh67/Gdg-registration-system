# Email Configuration Template for GDG Registration System
# Copy this file to 'config.py' and fill in your actual credentials

import os

EMAIL_CONFIG = {
    'smtp_server': os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
    'smtp_port': int(os.getenv('SMTP_PORT', 587)),
    'username': os.getenv('EMAIL_USER'),
    'password': os.getenv('EMAIL_PASS'),
    'from_email': os.getenv('FROM_EMAIL')
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
