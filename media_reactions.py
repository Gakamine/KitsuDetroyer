import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ACCESS_TOKEN")
kitsu_id = os.getenv('KITSU_ID')

headers = {'Authorization':'Bearer '+token}
query = """query {
  findProfileById(id: """+kitsu_id+""") {
    mediaReactions(first: 10) {
      nodes {
        id
      }
    }
  }
}
"""


def fecth_reactions():    
    response = requests.post("https://kitsu.io/api/graphql",json={"query": query},headers=headers)
    return response.json()['data']['findProfileById']['mediaReactions']['nodes']

def delete_reaction(reaction_id):
    delete_url = "https://kitsu.io/api/edge/media-reactions/"+reaction_id
    requests.delete(delete_url, headers=headers)
    print("https://kitsu.io/media-reactions/"+reaction_id+" deleted")

reactions = fecth_reactions()
while reactions != []:
    for reaction in reactions:
        delete_reaction(reaction['id'])
    reactions = fecth_reactions()
