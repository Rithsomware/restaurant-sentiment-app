# Restaurant Sentiment Analysis Platform

This project demonstrates a hackathon application where restaurant customers can place orders via a tablet. When an order is placed, the system:
- Captures an image of the table/customer using a webcam.
- Analyzes the customer’s facial expression for sentiment (e.g., "Happy", "Neutral", or "No face detected") using OpenCV’s Haar cascades.
- Logs the order details (table number, dish, order time, sentiment, and image path) into a local SQLite database.
- Prepares data that can later be exported and visualized (e.g., in Tableau).

## Features

- **Web-based Ordering Interface:** Customers select their table number and dish.
- **Camera Integration:** Captures images from a webcam at order time.
- **Sentiment Analysis:** Uses basic face and smile detection to assess customer satisfaction.
- **Robust Error Handling:** Edge-case protection if the camera or sentiment analysis fails.
- **Local Data Storage:** All order data is stored in an SQLite database for later analysis.

## File Structure
restaurant_sentiment_app/
├── app.py                   # Main Flask application and routes
├── camera.py                # Module for capturing images from the webcam
├── config.py                # Configuration settings (paths, camera index, etc.)
├── order.py                 # Order processing and SQLite database functions
├── sentiment.py             # Facial sentiment analysis (using Haar cascades)
├── requirements.txt         # Python dependencies
├── README.md                # Project overview and setup instructions
├── database/                # (Auto-created) Directory for the SQLite database
│   └── orders.db            # Orders database (created automatically on first run)
├── captured_images/         # (Auto-created) Directory for saved images
├── templates/               # HTML templates for the web interface
│   └── index.html           # Main ordering interface
└── static/
    └── css/
        └── style.css        # CSS styling for the interface


## Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd restaurant_sentiment_app
    ```

2. **Create a Virtual Environment and Install Dependencies:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate      # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    ```bash
    python app.py
    ```

    Open your browser and go to `http://127.0.0.1:5000/` to view the ordering interface.

4. **Usage:**

    - Enter a table number and select a dish.
    - Click **Place Order**.
    - The system will capture an image, analyze the facial sentiment, and log the order.
    - A confirmation message will display the detected sentiment.

## Notes

- Ensure that a working webcam is connected to your device.
- The sentiment analysis uses OpenCV’s Haar cascades (face and smile detection). For production use, consider a more robust model.
- Data stored in `database/orders.db` can be exported (e.g., to CSV) and visualized using Tableau.

## License

This project is licensed under the MIT License.
