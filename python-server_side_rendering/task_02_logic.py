"""
Flask Application - Task 2: Dynamic Template with Loops and Conditions

This application defines a route `/items` that loads a list of items from
a JSON file and renders them using a Jinja2 template. If the list is empty,
a fallback message is displayed.

Author: Your Name
Date: 2025-07
"""

from flask import Flask, render_template
import json
import os

# Initialize the Flask app
app = Flask(__name__)


@app.route('/items')
def show_items():
    """
    Route handler for '/items'.

    Reads a JSON file containing a list of items and passes it
    to a Jinja2 template (items.html) for dynamic rendering.
    
    Returns:
        Rendered HTML page with the list of items, or a message if empty.
    """
    items_file = 'items.json'
    
    try:
        with open(items_file, 'r') as f:
            data = json.load(f)
            items = data.get('items', [])  # Fallback to empty list
    except Exception as e:
        print(f"Error reading items file: {e}")
        items = []

    return render_template('items.html', items=items)


if __name__ == '__main__':
    # Run the app on host=0.0.0.0 for compatibility with sandbox environments
    app.run(debug=True, host='0.0.0.0', port=5000)
