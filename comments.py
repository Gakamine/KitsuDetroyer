import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ACCESS_TOKEN")
kitsu_id = os.getenv('KITSU_ID')

headers = {'Authorization':'Bearer '+token}
query = """query {
  findProfileById(id: """+kitsu_id+""") {
    comments(first: 10) {
      nodes {
        id
      }
    }
  }
}
"""


def fetch_comments():    
    response = requests.post("https://kitsu.io/api/graphql",json={"query": query},headers=headers)
    return response.json()['data']['findProfileById']['comments']['nodes']

def delete_comment(comment_id):
    delete_url = "https://kitsu.io/api/edge/comments/"+comment_id
    requests.delete(delete_url, headers=headers)
    print("https://kitsu.io/comments/"+comment_id+" deleted")

comments = fetch_comments()
while comments != []:
    for comment in comments:
        delete_comment(comment['id'])
    comments = fetch_comments()
