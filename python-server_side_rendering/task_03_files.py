from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_data(filepath):
    """
    Reads product data from a JSON file.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        list: A list of product dictionaries.
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []


def read_csv_data(filepath):
    """
    Reads product data from a CSV file.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        list: A list of product dictionaries.
    """
    products = []
    try:
        with open(filepath, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    products.append({
                        'id': int(row['id']),
                        'name': row['name'],
                        'category': row['category'],
                        'price': float(row['price'])
                    })
                except (ValueError, KeyError):
                    continue
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return products


@app.route('/products')
def products():
    """
    Route to display products from JSON or CSV data source.
    Supports filtering by product ID using query parameters.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products = []

    # Determine the data source
    if source == 'json':
        products = read_json_data('products.json')
    elif source == 'csv':
        products = read_csv_data('products.csv')
    else:
        error = "Wrong source"

    # Filter by ID if provided
    if product_id and not error:
        try:
            product_id = int(product_id)
            product = next(
                (p for p in products if p['id'] == product_id), None)
            if product:
                products = [product]
            else:
                error = "Product not found"
                products = []
        except ValueError:
            error = "Invalid ID format. ID must be an integer."
            products = []

    return render_template('product_display.html', products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
