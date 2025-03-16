# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from order import init_db, log_order
from camera import capture_image
from sentiment import analyze_sentiment

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session and flash messages

# Initialize the database on startup
init_db()

# Simulated menu items
MENU_ITEMS = [
    {"id": 1, "name": "Margherita Pizza", "price": 600},
    {"id": 2, "name": "Cheeseburger", "price": 400},
    {"id": 3, "name": "Caesar Salad", "price": 450},
    {"id": 4, "name": "Pasta Carbonara", "price": 500}
]

@app.route('/')
def hero():
    return render_template('hero.html')

@app.route('/home')
def index():
    """
    Renders the main ordering interface.
    """
    return render_template('index.html', menu=MENU_ITEMS)

@app.route('/order', methods=['POST'])
def order():
    """
    Processes an order: captures the image, performs sentiment analysis,
    logs the order, and displays the result.
    """
    table_number = request.form.get('table_number')
    dish_id = request.form.get('dish')
    dish = next((item['name'] for item in MENU_ITEMS if str(item['id']) == dish_id), "Unknown Dish")
    
    # Check if a table number was provided (edge-case handling)
    if not table_number:
        flash("Table number is required.", "error")
        return redirect(url_for('index'))
    
    # Attempt to capture an image from the webcam
    try:
        image_path, frame = capture_image()
    except Exception as e:
        flash(f"Error capturing image: {str(e)}", "error")
        image_path = ""
        sentiment = "Error"
    else:
        # Attempt sentiment analysis on the captured frame
        try:
            sentiment = analyze_sentiment(frame)
        except Exception as e:
            sentiment = "Analysis Error"
    
    # Log the order details in the database
    log_order(table_number, dish, sentiment, image_path)
    
    flash(f"Order for {dish} received! Sentiment detected: {sentiment}", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
