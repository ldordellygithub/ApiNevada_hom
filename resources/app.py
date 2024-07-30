import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getMyInfo')

def getMyInfo():
    
    value = {
        "name": "Jennifer ",
        "lastname": "Berrio",
         "age": 35,
        "height": 1.62,
        "weight": 75,
        
        "socialMedia": [
            {"facebook": "https://www.facebook.com/luis.garcia.7"},
            {"instagram": "https://www.instagram.com/luis.garcia.7"},
            {"twitter": "https://www.twitter.com/luis.garcia.7"},
            {"youtube": "https://www.youtube.com/luis.garcia.7"}
        ],
       
    
        "City_yenny": [ 
            {"address": "calle 123 # 15-01"},
            {"ciudad": "Pereira "},
            {"departamento": "Risalralda"},
            {"pais": "Colombia"}
        ],
        
        
         "name02": "Luis ",
        "lastname02": "Dordelly ",
        
         "age_02": 35,
        "height_02": 1.62,
        "weight_02": 75,
        
        "socialMedia_02": [
            {"facebook_02": "https://www.facebook.com/luis.garcia.7"},
            {"instagram_02": "https://www.instagram.com/luis.garcia.7"},
            {"twitter_02": "https://www.twitter.com/luis.garcia.7"},
            {"youtube_02": "https://www.youtube.com/luis.garcia.7"}
        ],
        
        
        "City_luis": [ 
            {"address_01": "calle 123 # 15-01"},
            {"ciudad_01": "Pereira "},
            {"departamento_01": "Risalralda"},
            {"pais_01": "Colombia"}
        ],
        
        
        
        


    }
    

    return jsonify(value)

if __name__ == "__main__":
    app.run(debug=True)
    