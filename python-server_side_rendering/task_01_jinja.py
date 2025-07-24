from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    Render the home page template.

    Returns:
        Rendered HTML template for the home page.
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    Render the about page template.

    Returns:
        Rendered HTML template for the about page.
    """
    return render_template('about.html')


@app.route('/contact')
def contact():
    """
    Render the contact page template.

    Returns:
        Rendered HTML template for the contact page.
    """
    return render_template('contact.html')


if __name__ == '__main__':
    """
    Run the Flask development server with debugging enabled on port 5000.
    """
    app.run(debug=True, port=5000)
