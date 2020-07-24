import json
import requests

# #                                               # #
#   Dolores - abstraction module over openai's API   #
# #                                               # #


# Defile module-scoped variables
engine = ""
api_key = ""
headers = {}
prompts = {}


# Initialize module
def initialize(_api_key, _engine="davinci"):
  global api_key, engine, headers, prompts

  if _api_key:
    api_key = _api_key
    engine = _engine
  else:
    print("No API Key provided. Initialization failed.")
    return

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {_api_key}"
  }

  prompts = json.load(open("./dolores/prompts.json"))

#
def get_globals():
  global api_key, engine, headers, prompts

  return api_key, engine, headers, prompts

# Change engine setting
def set_engine(_engine):
  global engine
  engine = _engine

# List Engines GET
# Lists the currently available engines, and provides basic information about each option such as the owner and availability.
def list_engines():
  global headers

  url = "https://api.openai.com/v1/engines"
  response = requests.get(url, headers=headers)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    response.raise_for_status()

# Retrieve Engine GET
# Retrieves an engine instance, providing basic information about the engine such as the owner and availability.
def retrieve_engine():
  global headers

  url = f"https://api.openai.com/v1/engines/{engine}"
  response = requests.get(url, headers=headers)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    response.raise_for_status()

# Create Completion POST
# Returns new text as well as, if requested, the probabilities over each alternative token at each position.
def complete_prompt(prompt, max_tokens=5, temperature=1, top_p=1, n=1):
  global engine, headers

# Create payload for API Request
  payload = {
    "prompt": prompt,
    "max_tokens": max_tokens,
    "temperature": temperature,
    "top_p": top_p,
    "n": n
  }

  url = f"https://api.openai.com/v1/engines/{engine}/completions"
  response = requests.post(url, headers=headers, json=payload)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    response.raise_for_status()

def complete_predefined_prompt(prompt_key, index=0, prompt = ""):
  global prompts

  # If key exists in prompt dictionary select it complete it
  if prompt_key in prompts:
    payload = {}

    if prompt != "":
      # Append custom prompt to predefined prompt
      payload = prompts[prompt_key][index]
      payload["prompt"] = prompts[prompt_key][index]["prompt"] + " " + prompt

    elif prompt == "":
      # Set predefined prompt
      payload = prompts[prompt_key][index]


    return complete_prompt(
      payload["prompt"],
      payload["max_tokens"],
      payload["temperature"],
      payload["top_p"],
      payload["n"]
    )

  else:
    return "Unable to access predefined prompt."


# Search POST
# Perform a semantic search over a list of documents.
def search(payload):
  global engine, headers

  url = f"https://api.openai.com/v1/engines/{engine}/search"
  response = requests.post(url, headers=headers, json=payload)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    return response.raise_for_status()
