import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ACCESS_TOKEN")
kitsu_id = os.getenv('KITSU_ID')

headers = {'Authorization':'Bearer '+token}
query = """query {
  findProfileById(id: """+kitsu_id+""") {
    posts(last: 10) {
      nodes {
        id
      }
    }
  }
}
"""


def fetch_posts():    
    response = requests.post("https://kitsu.io/api/graphql",json={"query": query},headers=headers)
    return response.json()['data']['findProfileById']['posts']['nodes']

def delete_post(post_id):
    delete_url = "https://kitsu.io/api/edge/posts/"+post_id
    requests.delete(delete_url, headers=headers)
    print("https://kitsu.io/posts/"+post_id+" deleted")

posts = fetch_posts()
while posts != []:
    for post in posts:
        delete_post(post['id'])
    posts = fetch_posts()
