import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def init_database():
    #initialize the database
    cred = credentials.Certificate("databaseModules\manga-updates-533fd-firebase-adminsdk-lo3b6-419cc41a75.json")
    firebase_admin.initialize_app(cred)

def retrieve_data():
    get_updates_for = []
    #Reading from the database
    db = firestore.client()
    doc = db.collection(u'Users').document(u'Tirth') 
    if doc.get().exists:
        books = doc.get().to_dict()["Books"]
        for book in books:
            get_updates_for.append(book)
    return get_updates_for

def add_data():
    #Writing to the database
    db = firestore.client()
    doc = db.collection(u'Users').document(u'Tirth') 
    if doc.get().exists:
        books = doc.get().to_dict()["Books"]
        books.append(input("Enter the name of the book: "))
        doc.update({"Books": books})
    else:
        print("No such document!")

def delete_data():
    #Deleting from the database
    db = firestore.client()
    doc = db.collection(u'Users').document(u'Tirth') 
    if doc.get().exists:
        books = doc.get().to_dict()["Books"]
        books.remove(input("Enter the name of the book: "))
        doc.update({"Books": books})
    else:
        print("No such document!")