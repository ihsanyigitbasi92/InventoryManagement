
"""
README file for the Stock Tracking System project.
"""

# Stock Tracking System

This is a stock tracking system for an electronics store, built with Flask and SQLAlchemy.

## Features

- Inventory Management
- Product Management
- Supplier Management
- Sales Management
- User Management
- Notifications
- Dashboard
- Data Export/Import

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/stock_tracking_system.git
   ```
2. Navigate to the project directory:
   ```
   cd stock_tracking_system
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Set up the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```
2. Run the application:
   ```
   python run.py
   ```
3. Open your browser and go to `http://localhost:5000`.

## Configuration

Edit the `config.py` file to configure the application settings, such as the database URI and mail server settings.

## License

This project is licensed under the MIT License.
