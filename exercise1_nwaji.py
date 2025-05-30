##RMB TO SAVE TO GITHUB REPO

# importing the requests library
import requests
import json

# defining the api-endpoint
API_URL = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

# data to be sent to api
data = {
        "UCID": "cen25",
        "first_name": "Chidiebube",
        "last_name": "Nwaji",
        "github_username": "chidiNwaji",
        "discord_username": "JoJoSiJuanito",
        "favorite_cartoon": "Wild Kratts",
        "favorite_language": "Java",
        "movie_or_game_or_book": "Saving Private Ryan"
        }

#header data
header = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# sending post request and saving response as response object
resp = requests.post(url=API_URL, data=json.dumps(data), headers=header)

# print response text and status code
print("Status Code:", resp.status_code)
print("Text:", resp.text)