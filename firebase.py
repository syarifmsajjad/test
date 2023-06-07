import pyrebase
config = {
"apiKey": "AIzaSyAzEVLC6I_zwN2cWyTFOc5vpRbgOqLza4U",
"authDomain": "eas1.aces.telkomsel.firebase.io",
"databaseURL": "https://eas1.aces.telkomsel.firebase.io",
"storageBucket": "eas1.aces.telkomsel.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
print(db.get())
