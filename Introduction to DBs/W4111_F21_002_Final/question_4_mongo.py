import mongodb_check
import pandas as pd


def question_4_example():

    # You may have to do this just to be safe.

    connect_url = "mongodb://localhost:27017/"
    mongodb_check.set_connect_url(connect_url)

    # Get the client
    client = mongodb_check.get_mongo_client()

    # This aggregation returns all of the characters that appeared in season 1, episode 1 and the scenes.
    # Requires the PyMongo package.
    # https://api.mongodb.com/python/current

    result = client['F21_Final']['got_episodes'].aggregate([
        {
            '$unwind': {
                'path': '$scenes',
                'includeArrayIndex': 'sceneNum'
            }
        }, {
            '$unwind': {
                'path': '$scenes.characters'
            }
        }, {
            '$project': {
                'seasonNum': 1,
                'episodeNum': 1,
                'sceneNum': {
                    '$sum': [
                        '$sceneNum', 1
                    ]
                },
                'characterName': '$scenes.characters.name'
            }
        }, {
            '$match': {
                'seasonNum': 1,
                'episodeNum': 1
            }
        }, {
            '$project': {
                '_id': 0
            }
        }
    ])

    result = list(result)
    result = pd.DataFrame(result)
    return result


def question_4_ratings():

    # You may have to do this just to be safe.
    connect_url = "mongodb://localhost:27017/"
    mongodb_check.set_connect_url(connect_url)

    # Get the client
    client = mongodb_check.get_mongo_client()

    result = client['F21_Final']['got_episodes'].aggregate([
        {
            '$project': {
                'seasonNum': 1, 
                'episodeNum': 1, 
                'episodeTitle': 1, 
                'episodeDate': '$episodeAirDate', 
                'episodeDescription': 1, 
                'link': {
                    '$substr': [
                        '$episodeLink', 7, 9
                    ]
                }
            }
        }, {
            '$lookup': {
                'from': 'title_ratings', 
                'localField': 'link', 
                'foreignField': 'tconst', 
                'as': 'joined_ratings_data'
            }
        }, {
            '$unwind': {
                'path': '$joined_ratings_data'
            }
        }, {
            '$project': {
                '_id': 0,
                'seasonNum': 1, 
                'episodeNum': 1, 
                'episodeDate': 1, 
                'episodeTitle': 1, 
                'episodeDescription': 1, 
                'tconst': '$joined_ratings_data.tconst', 
                'averageRating': '$joined_ratings_data.averageRating', 
                'numVotes': '$joined_ratings_data.numVotes'
            }
        }
    ])

    result = list(result)
    result = pd.DataFrame(result)
    return result

