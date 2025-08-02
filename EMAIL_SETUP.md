# Email Setup Guide

## Setting up Gmail for Contact Form

To enable the contact form to send emails, you need to:

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a new app password for "Mail"
   - Copy the 16-character password

3. **Set Environment Variable**:
   ```bash
   export EMAIL_PASSWORD=your_16_character_app_password
   ```

4. **Start the server**:
   ```bash
   npm start
   ```

## Security Notes
- Never commit your email password to Git
- Use environment variables for sensitive data
- The app password is different from your regular Gmail password

## Testing
- Visit http://localhost:3000
- Go to the Contact page
- Fill out and submit the form
- Check your email for the message 