# config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Path for the SQLite database
DATABASE_URI = os.path.join(BASE_DIR, 'database', 'orders.db')

# Default camera index (adjust if needed)
CAMERA_INDEX = 0

# Note: The Haar cascade files are accessed via OpenCV's built-in data paths.
