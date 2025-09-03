# 📧 Email Setup Guide for GDG Registration System

## 🚨 **IMPORTANT: You need to configure your Gmail before emails will work!**

### **Step 1: Edit the Config File**
Open `config.py` and replace the placeholder values:

```python
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'username': 'your-actual-email@gmail.com',  # ← PUT YOUR GMAIL HERE
    'password': 'your-16-digit-app-password',   # ← PUT YOUR APP PASSWORD HERE
    'from_email': 'your-actual-email@gmail.com' # ← PUT YOUR GMAIL HERE
}
```

### **Step 2: Enable 2-Factor Authentication on Gmail**
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Click "Security" → "2-Step Verification"
3. Turn it ON if not already enabled

### **Step 3: Generate App Password**
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Click "Security" → "App passwords"
3. Select "Mail" and "Other (Custom name)"
4. Name it "GDG Registration System"
5. Click "Generate"
6. **Copy the 16-digit password** (like: `abcd efgh ijkl mnop`)

### **Step 4: Update Config File**
Replace in `config.py`:
- `your-actual-email@gmail.com` → Your real Gmail address
- `your-16-digit-app-password` → The 16-digit app password you just generated

### **Step 5: Test the System**
1. Restart your Flask app
2. Register a new user
3. Check if email is received

## 🔍 **Troubleshooting:**

### **"Authentication failed" error:**
- Make sure you're using the **App Password**, not your regular Gmail password
- Ensure 2-Factor Authentication is enabled
- Check that the email address is correct

### **"Connection refused" error:**
- Check your internet connection
- Some networks block SMTP ports
- Try using a different network

### **Email not sending:**
- Check the console for error messages
- Verify all config values are correct
- Make sure the recipient email is valid

## 📱 **Alternative: Use Your Phone's Hotspot**
If your network blocks SMTP, try using your phone's mobile hotspot.

## 🆘 **Need Help?**
If you're still having issues, check:
1. Gmail account settings
2. Network restrictions
3. Console error messages

---

**Remember:** Never share your app password or commit it to version control! 