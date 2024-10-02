from scripts.app import app  # Import the Flask app
from scripts.feature import start_daemon


def main():
    # Call the specific function from feature.py
    start_daemon()  # Call the function you want to run

    # Run the Flask app
    app.run(debug=True)  # You can set debug=False for production


if __name__ == "__main__":
    main()
