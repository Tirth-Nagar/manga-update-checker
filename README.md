# Manga Update Checker
This python script is designed to notify users when updates are available for their favorite manga titles. It utilizes the following tools and technologies:

1. Beautiful Soup for web scraping
2. Twilio for SMS communication
3. aiohttp for optimized requests and improved performance

## How to Use
1. Install the required libraries: pip install beautifulsoup4 twilio aiohttp
2. Set up a Twilio account and obtain your account SID, auth token, and phone number.
3. Update the account_sid, auth_token, and sender variables in the script with your Twilio account information.
4. Add your phone number as the receiver variable.
-=5. Create a firebase to store your user ingformation and preferred titles or create a manga_list variable with a list of the manga titles you want to receive updates for -in database.py.
6. Run the script: main.py
7. The script will check for updates each time it is run and send you a text message whenever an update is available.

### Notes
The web scraping functionality relies on the specific HTML structure of the website being used. If the website updates its layout, the script may need to be modified to reflect the changes.
