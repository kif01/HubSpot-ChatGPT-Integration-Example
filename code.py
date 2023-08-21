import os
import hubspot
import re
from hubspot import HubSpot
from hubspot.crm.tickets import ApiException

import requests

def main(event):

  # How to use secrets
  # Secrets are a way for you to save API keys or private apps and set them as a variable to use anywhere in your code
  # Each secret needs to be defined like the example below
  hubspot = HubSpot(access_token=os.getenv('PRIVATEKEY'))
  
  url = "https://api.openai.com/v1/chat/completions"
  params = {"model": "gpt-3.5-turbo","messages": [{"role": "system","content": "You will be provided with a block of text, and your task is to classify its sentiment as concerned, happy, neutral or angry and extract the main category from it."
    },
    {
      "role": "user",
      "content": <INPUT DATA> #For example a property that contains the data that you want to process like "ticket description"
    }
  	],
  "temperature": 0.5,
  "max_tokens": 256,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0}
  
  headers = {'accept': 'application/json', 'Authorization': 'Bearer {}'.format(os.getenv('OPENAIKEY'))}
  #response = requests.request("POST", url, headers=headers, params=querystring)
  response = requests.post(url, json= params, headers=headers)
  result = response.json()
  
  result= result['choices'][0]['message']['content']
  
  #Parsing the result to extract sentiment and topic from the result
  array1 = result.split(":")
  array2 = array1[1].split("\n")
  sentiment= array2[0]
  category = array1[2]

  
  return {
   "outputFields": {
      "sentiment": sentiment,
       "category": category
    }
  }

  
   


  

  

