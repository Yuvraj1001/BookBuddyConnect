import json
import logging
from flask import render_template, request, flash, redirect, url_for
from app import app
from data.resume_data import resume_data

@app.route('/')
def index():
    """Main portfolio page"""
    try:
        # Load blog posts
        with open('data/blog_posts.json', 'r') as f:
            blog_posts = json.load(f)
    except Exception as e:
        logging.error(f"Error loading blog posts: {e}")
        blog_posts = []
    
    return render_template('index.html', 
                         resume=resume_data, 
                         blog_posts=blog_posts)

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    try:
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not all([name, email, subject, message]):
            flash('All fields are required.', 'error')
            return redirect(url_for('index') + '#contact')
        
        # Log the contact form submission (in production, you'd send email or save to database)
        logging.info(f"Contact form submission - Name: {name}, Email: {email}, Subject: {subject}")
        logging.info(f"Message: {message}")
        
        flash('Thank you for your message! I will get back to you soon.', 'success')
        
    except Exception as e:
        logging.error(f"Error processing contact form: {e}")
        flash('An error occurred while sending your message. Please try again.', 'error')
    
    return redirect(url_for('index') + '#contact')

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html', resume=resume_data), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logging.error(f"Internal server error: {error}")
    return render_template('index.html', resume=resume_data), 500
