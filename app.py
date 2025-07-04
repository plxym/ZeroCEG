from flask import Flask, render_template, request, jsonify
import os
import json
from utils.pdf_parser import extract_text
import requests

app = Flask(__name__)

# Store PDF content in memory for quick access
pdf_content_cache = {}

def load_pdf_content():
    """Load all PDF files and cache their content"""
    pdf_dir = 'pdfs'
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
        print(f"Created {pdf_dir} directory. Please add your PDF files here.")
        return
    
    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            try:
                filepath = os.path.join(pdf_dir, filename)
                event_id = filename.replace('.pdf', '').replace('_', '-')
                pdf_content_cache[event_id] = extract_text(filepath)
                print(f"Loaded content for {event_id}")
            except Exception as e:
                print(f"Error loading {filename}: {e}")

# Events configuration - automatically populated from PDF files
def get_events():
    events = []
    pdf_dir = 'pdfs'
    
    if os.path.exists(pdf_dir):
        for filename in os.listdir(pdf_dir):
            if filename.endswith('.pdf'):
                event_id = filename.replace('.pdf', '').replace('_', '-')
                title = filename.replace('.pdf', '').replace('_', ' ').title()
                events.append({
                    'id': event_id,
                    'title': title,
                    'description': f'Get help with {title} event guidelines and requirements',
                    'filename': filename
                })
    
    # Add some default events if no PDFs found
    if not events:
        events = [
            {
                'id': 'dragster-design',
                'title': 'Dragster Design',
                'description': 'Design and build a CO2-powered dragster that travels the fastest and farthest',
                'filename': 'dragster_design.pdf'
            },
            {
                'id': 'video-game-design',
                'title': 'Video Game Design',
                'description': 'Create an original video game that demonstrates programming and design skills',
                'filename': 'video_game_design.pdf'
            },
            {
                'id': 'architectural-design',
                'title': 'Architectural Design',
                'description': 'Design a structure that meets specific architectural requirements',
                'filename': 'architectural_design.pdf'
            }
        ]
    
    return events

@app.route('/')
def index():
    events = get_events()
    return render_template('index.html', events=events)

@app.route('/event/<event_id>')
def event_page(event_id):
    events = get_events()
    event = next((e for e in events if e['id'] == event_id), None)
    
    if not event:
        return render_template('error.html', message="Event not found"), 404
    
    # Get PDF content for this event
    guide_text = pdf_content_cache.get(event_id, "")
    
    return render_template('event.html', 
                         title=event['title'],
                         event_id=event_id,
                         guide_text=guide_text)

@app.route('/chat')
def standalone_chat():
    """Standalone chat page that works without PDFs"""
    return render_template('standalone-chat.html')

@app.route('/cors-help')
def cors_help():
    """CORS setup help page"""
    return render_template('cors-helper.html')

@app.route('/api/events')
def api_events():
    events = get_events()
    return jsonify({'events': events})

# Add CORS headers to all responses
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', message="Page not found"), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html', message="Server error occurred"), 500

from flask import Flask, request, jsonify
import requests


import logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/api/chat", methods=["POST"])
def proxy_to_puter():
    try:
        data = request.get_json()
        app.logger.debug(f"Sending to Puter API: {data}")

        puter_response = requests.post(
            "https://js.puter.com/v2/",
            headers={"Content-Type": "application/json"},
            json=data,
            timeout=30
        )

        app.logger.debug(f"Puter API responded with status {puter_response.status_code}")
        app.logger.debug(f"Response content: {puter_response.text}")

        try:
            return jsonify(puter_response.json()), puter_response.status_code
        except ValueError:
            return jsonify({
                "error": "Puter API returned non-JSON.",
                "status": puter_response.status_code,
                "raw_response": puter_response.text
            }), 500

    except Exception as e:
        app.logger.error(f"Error contacting Puter API: {str(e)}")
        return jsonify({ "error": str(e) }), 500

0
    
if __name__ == '__main__':
    print("Starting TSA Helper...")
    print("Loading PDF content...")
    load_pdf_content()
    print(f"Loaded {len(pdf_content_cache)} event guides")
    print("\n" + "="*50)
    print("IMPORTANT: CORS Setup Required!")
    print("Visit http://localhost:5000/cors-help for setup instructions")
    print("="*50 + "\n")
    print("Starting Flask server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
