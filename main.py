from scraperModules import scraper
from notificationModules import notification

def main():
    booksList = ""
    updatedBooks = scraper.getUpdates()
    if len(updatedBooks) != 0:
        for book in updatedBooks:
            booksList = book + ", " + booksList
        message = "The following books have been updated today: " + booksList
        notification.sendSMS(message)
    else:
        notification.sendSMS("No books have been updated as of now.")

main()
