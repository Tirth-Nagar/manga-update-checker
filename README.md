# Manga Update Checker
This python script is designed to notify users when updates are available for their favorite manga titles. It utilizes the following tools and technologies:

Beautiful Soup for web scraping
Twilio for SMS communication
aiohttp for optimized requests and improved performance

## How to Use
Install the required libraries: pip install beautifulsoup4 twilio aiohttp
Set up a Twilio account and obtain your account SID, auth token, and phone number.
Update the account_sid, auth_token, and sender variables in the script with your Twilio account information.
Add your phone number as the receiver variable.
Create a firebase to store your user ingformation and preferred titles or create a manga_list variable with a list of the manga titles you want to receive updates for in database.py.
Run the script: main.py
The script will check for updates each time it is run and send you a text message whenever an update is available.

### Notes
The web scraping functionality relies on the specific HTML structure of the website being used. If the website updates its layout, the script may need to be modified to reflect the changes.
