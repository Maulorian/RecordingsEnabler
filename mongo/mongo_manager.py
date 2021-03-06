import os
import dotenv
import pymongo
dotenv.load_dotenv()
RECORDING_ENABLER_DATABASE = 'RecordingEnabler'
CONNECTION_STRING = f"mongodb+srv://adp:{os.getenv('MONGO_PASSWORD')}@yeda.lan6r.gcp.mongodb.net/?ssl=true" \
                    f"&ssl_cert_reqs=CERT_NONE "
INDEX = 'match_id'


def get_recording_enabler_database():
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client[RECORDING_ENABLER_DATABASE]
    return db


def get_recorded_games_collection():
    recoding_enabler_database = get_recording_enabler_database()
    return recoding_enabler_database.matches


def create_index():
    collection = get_recorded_games_collection()
    collection.create_index(INDEX, unique=True)
