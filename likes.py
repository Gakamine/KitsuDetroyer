import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ACCESS_TOKEN")
kitsu_id = os.getenv('KITSU_ID')

headers = {'Authorization':'Bearer '+token}
fetch_url = "https://kitsu.io/api/edge/post-likes?filter[userId]="+kitsu_id

def fetch_likes():    
    response = requests.get(fetch_url,headers=headers)
    return response.json()['data']

def delete_like(like_id):
    delete_url = "https://kitsu.io/api/edge/post-likes/"+like_id
    requests.delete(delete_url, headers=headers)
    print("Like "+like_id+" deleted")

likes = fetch_likes()
while likes != []:
    for like in likes:
        delete_like(like['id'])
    likes = fetch_likes()
