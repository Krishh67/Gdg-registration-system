from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
import json
import csv
import os
from datetime import datetime
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Import configuration
try:
    from config import EMAIL_CONFIG, EVENT_CONFIG
except ImportError:
    # Fallback configuration if config.py doesn't exist
    
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

# Data storage file
DATA_FILE = 'registrations.json'

def load_registrations():
    """Load registrations from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_registrations(registrations):
    """Save registrations to JSON file"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(registrations, f, indent=2, ensure_ascii=False)

def validate_name(name):
    """Validate name field"""
    if not name or len(name.strip()) < 2:
        return "Please enter at least 2 characters."
    if not re.match(r"^[-'a-zA-Z\s]+$", name.strip()):
        return "Only letters, spaces, hyphens, and apostrophes allowed."
    return ""

def validate_email(email):
    """Validate email field"""
    if not email:
        return "Email is required."
    if not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]{2,}$", email, re.IGNORECASE):
        return "Please enter a valid email address."
    return ""

def validate_phone(phone):
    """Validate phone field"""
    if not phone:
        return "Phone is required."
    digits = re.sub(r'[^0-9+]', '', phone)
    if len(digits) < 7:
        return "Please enter a valid phone number."
    return ""

def validate_course(course):
    """Validate course field"""
    if not course:
        return "Course is required."
    valid_courses = ['btech-aids', 'btech-ce', 'mba-tech']
    if course not in valid_courses:
        return "Please select a valid course."
    return ""

def validate_year(year):
    """Validate year field"""
    if not year:
        return "Year is required."
    valid_years = ['1', '2', '3', '4', '5']
    if year not in valid_years:
        return "Please select a valid year."
    return ""

def send_registration_email(registration_data):
    """Send confirmation email to registered user"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['from_email']
        msg['To'] = registration_data['email']
        msg['Subject'] = f"{EVENT_CONFIG['name']} Registration Confirmed - {registration_data['id']}"
        
        # Email body
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                <div style="text-align: center; margin-bottom: 30px;">
                    <h1 style="color: #4285f4; margin-bottom: 10px;">🎉 Registration Confirmed!</h1>
                    <h2 style="color: #34a853; margin-bottom: 20px;">{EVENT_CONFIG['name']}</h2>
                </div>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                    <h3 style="color: #333; margin-top: 0;">Event Details</h3>
                    <p><strong>📅 Date:</strong> {EVENT_CONFIG['date']}</p>
                    <p><strong>⏰ Time:</strong> {EVENT_CONFIG['time']}</p>
                    <p><strong>📍 Venue:</strong> {EVENT_CONFIG['venue']}</p>
                    <p><strong>🎫 Registration ID:</strong> {registration_data['id']}</p>
                </div>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                    <h3 style="color: #333; margin-top: 0;">Your Information</h3>
                    <p><strong>Name:</strong> {registration_data['name']}</p>
                    <p><strong>Email:</strong> {registration_data['email']}</p>
                    <p><strong>Phone:</strong> {registration_data['phone']}</p>
                    <p><strong>Course:</strong> {registration_data['course']}</p>
                    <p><strong>Year:</strong> {registration_data['year']}</p>
                </div>
                
                <div style="background: #e8f5e8; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                    <h3 style="color: #2e7d32; margin-top: 0;">What's Next?</h3>
                    <ol style="margin: 0; padding-left: 20px;">
                        <li>Save this email for your records</li>
                        <li>Add the event to your calendar</li>
                        <li>Join our WhatsApp Community: <a href="https://chat.whatsapp.com/L4DqRpnUTGIAvWKG7h6DHc" style="color: #4285f4;">Click here</a></li>
                    </ol>
                </div>
                
                <div style="text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd;">
                    <p style="color: #666; margin: 0;">Questions? Contact us at <a href="mailto:events@gdg.com" style="color: #4285f4;">events@gdg.com</a></p>
                    <p style="color: #666; margin: 5px 0 0 0;">© 2024 Google Developers Club. All rights reserved.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        # Connect to SMTP server and send email
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['username'], EMAIL_CONFIG['password'])
        text = msg.as_string()
        server.sendmail(EMAIL_CONFIG['from_email'], registration_data['email'], text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False

@app.route('/')
def landing():
    """Landing page"""
    return render_template('indexx.html')

@app.route('/events')
def events():
    """Events selection page"""
    return render_template('events.html')

@app.route('/register/<event_type>')
def register_event(event_type):
    """Event registration page"""
    if event_type == 'seminar':
        return render_template('register_event.html')
    else:
        return redirect(url_for('events'))

@app.route('/thank-you')
def thank_you():
    """Thank you page after registration"""
    return render_template('thank_you.html', registration_id="GDG-2024-001")

@app.route('/admin')
def admin():
    """Admin panel to view all registrations"""
    registrations = load_registrations()
    
    # Calculate today's registrations
    from datetime import datetime, date
    today = date.today()
    today_count = 0
    
    for reg in registrations:
        try:
            reg_date = datetime.fromisoformat(reg['created_at']).date()
            if reg_date == today:
                today_count += 1
        except:
            pass
    
    return render_template('admin.html', registrations=registrations, today_count=today_count)

@app.route('/api/register', methods=['POST'])
def register():
    """Handle registration form submission"""
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        
        # Validation
        name_error = validate_name(name)
        email_error = validate_email(email)
        phone_error = validate_phone(phone)
        course_error = validate_course(data.get('course', ''))
        year_error = validate_year(data.get('year', ''))
        
        if name_error or email_error or phone_error or course_error or year_error:
            return jsonify({
                'success': False,
                'errors': {
                    'name': name_error,
                    'email': email_error,
                    'phone': phone_error,
                    'course': course_error,
                    'year': year_error
                }
            }), 400
        
        # Check for duplicate email
        registrations = load_registrations()
        if any(r['email'].lower() == email.lower() for r in registrations):
            return jsonify({
                'success': False,
                'message': 'Email already registered.'
            }), 400
        
        # Create registration record
        registration = {
            'id': f"id-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'name': name,
            'email': email,
            'phone': phone,
            'course': data.get('course', ''),
            'year': data.get('year', ''),
            'interests': data.get('interests', []),
            'notes': data.get('notes', ''),
            'created_at': datetime.now().isoformat()
        }
        
        registrations.insert(0, registration)
        save_registrations(registrations)
        
        # Send confirmation email
        email_sent = send_registration_email(registration)
        
        return jsonify({
            'success': True,
            'message': 'Registered successfully!' + (' Email sent!' if email_sent else ' Email could not be sent.'),
            'registration': registration
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Server error: {str(e)}'
        }), 500

@app.route('/api/registrations')
def get_registrations():
    """Get all registrations"""
    return jsonify(load_registrations())

@app.route('/api/registrations/<registration_id>', methods=['DELETE'])
def delete_registration(registration_id):
    """Delete a registration"""
    registrations = load_registrations()
    registrations = [r for r in registrations if r['id'] != registration_id]
    save_registrations(registrations)
    return jsonify({'success': True, 'message': 'Registration deleted.'})

@app.route('/api/registrations/clear', methods=['DELETE'])
def clear_registrations():
    """Clear all registrations"""
    save_registrations([])
    return jsonify({'success': True, 'message': 'All registrations cleared.'})

@app.route('/export/json')
def export_json():
    """Export registrations as JSON"""
    registrations = load_registrations()
    return jsonify(registrations)

@app.route('/export/csv')
def export_csv():
    """Export registrations as CSV"""
    registrations = load_registrations()
    
    # Create CSV content
    output = []
    output.append(['Name', 'Email', 'Phone', 'Course', 'Year', 'Interests', 'Notes', 'Created At'])
    
    for reg in registrations:
        interests_str = ', '.join(reg.get('interests', [])) if reg.get('interests') else ''
        output.append([
            reg['name'],
            reg['email'],
            reg['phone'],
            reg.get('course', ''),
            reg.get('year', ''),
            interests_str,
            reg.get('notes', ''),
            reg['created_at']
        ])
    
    # Create CSV string
    csv_content = '\n'.join([','.join([f'"{cell}"' for cell in row]) for row in output])
    
    return csv_content, 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename=gdg-registrations.csv'
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000) 
