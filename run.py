#!/usr/bin/env python3
"""
TSA Helper - Run Script
Simple script to start the TSA Helper application
"""

import os
import sys

def check_requirements():
    """Check if required packages are installed"""
    try:
        import flask
        print("✓ Flask is installed")
    except ImportError:
        print("✗ Flask is not installed. Run: pip install Flask")
        return False
    
    try:
        import requests
        print("✓ Requests is installed")
    except ImportError:
        print("✗ Requests is not installed. Run: pip install requests")
        return False
    
    try:
        import fitz
        print("✓ PyMuPDF is installed")
    except ImportError:
        print("✗ PyMuPDF is not installed. Run: pip install PyMuPDF")
        print("  (This is needed for PDF processing)")
        return False
    
    return True

def create_directories():
    """Create necessary directories"""
    directories = ['pdfs', 'static', 'templates', 'utils']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✓ Created {directory}/ directory")
        else:
            print(f"✓ {directory}/ directory exists")

def main():
    print("=" * 50)
    print("TSA Helper - Starting Application")
    print("=" * 50)
    
    # Check requirements
    print("\n1. Checking requirements...")
    if not check_requirements():
        print("\nPlease install missing requirements and try again.")
        print("Run: pip install -r requirements.txt")
        sys.exit(1)
    
    # Create directories
    print("\n2. Setting up directories...")
    create_directories()
    
    # Check for PDF files
    print("\n3. Checking for PDF files...")
    pdf_dir = 'pdfs'
    pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')] if os.path.exists(pdf_dir) else []
    
    if pdf_files:
        print(f"✓ Found {len(pdf_files)} PDF files:")
        for pdf in pdf_files:
            print(f"  - {pdf}")
    else:
        print("! No PDF files found in pdfs/ directory")
        print("  You can still use the application, but add PDF files for full functionality")
    
    # Start the application
    print("\n4. Starting Flask application...")
    print("-" * 30)
    print("Application will be available at:")
    print("http://localhost:5000")
    print("http://127.0.0.1:5000")
    print("-" * 30)
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Import and run the app
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
