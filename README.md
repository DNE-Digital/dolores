# Dolores 🤖⚡


## What is it?

**Dolores** is a Python library designed to improve the developer experience when working with pretrained language models. **Dolores** provides prompts for interacting with language models that result in interesting or useful outputs. The purpose of this library is to simplify the learning curve by providing easy to use examples and sample text to get started. Additionally, it has the broader goal of becoming **the most comprehensive repository of quality prompts for interacting with language models.**

It is named after [Dolores Abarnathy](https://westworld.fandom.com/wiki/Dolores_Abernathy) of Westworld.

## Installation (PyPi Package)
```
$ pip install dolores
```

## Main Features

- Predefined prompts and hyperparameter settings to yield best results from common prompt inputs
- A wrapper over the OpenAI API callable via functions
- Easy to use CLI interface to make API calls into GPT-3

## Usage
Either import via the python interpreter or in a python file.
#### dolores.initialize(api_key: str, engine_name: str (Optional))

```
import dolores 
dolores.initialize("<YOUR-API-KEY>")
```

From there you may not call openai's API directly via the accessible methods in the Dolores class instance. The following out call the list engines API call. Each API call has an associated method call that can be used to call the API.


### List Engines GET
Lists the currently available engines, and provides basic information about each option such as the owner and availability.
```
dolores.list_engines()
```

### Retrieve Engine GET
Retrieves an engine instance, providing basic information about the engine such as the owner and availability.
```
dolores.retrieve_engine()
```

### Changing Engines
##### dolores.set_engine(engine: str)

After instantiating the Dolores class, subsequent class to the Open AI API will be made under the same engine selection. In order to change the engine used for the API call there is an exposed method.


```
dolores.set_engine("davinci")
```

Note: Validation against the existing engine types is in consideration for future versions.

### Complete Prompt POST (!important)
##### dolores.complete_prompt(prompt: string, max_tokens: int = 5, temperature: int = 1, top_p: int = 1, n: int = 1)

Complete a prompt. This is the main endpoint of the GPT-3 APIs. Returns new text as well as, if requested, the probabilities over each alternative token at each position.

Request:
```
dolores.create_completion("Is the JavaScript programming language better than python?", 20)
```
Response: (see response["choices"][0]["text"] for plaintext response)
```
JSON: {'id': 'cmpl-kM6MK5dVRvD964MxeyG4AjCy', 'object': 'text_completion', 'created': 1595431739, 'model': 'ada:2020-05-03', 'choices': [{'text': ' in a far away place', 'index': 0, 'logprobs': None, 'finish_reason': 'length'}]}
```

`'in a far away place'` 😂

#### Request Parameters

| Name        	| In   	| Type              	| Required 	| Description                                                                                                                                                                                                                                                                                                	|
|-------------	|------	|-------------------	|----------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| engine      	| body 	| string            	| true     	| The engine ID                                                                                                                                                                                                                                                                                              	|
| prompt      	| body 	| (see description) 	| false    	| One or more prompts to generate from. Can be a string, list of strings, a list of integers (i.e. a single prompt encoded as tokens), or list of lists of integers (i.e. many prompts encoded as integers).                                                                                                 	|
| max_tokens  	| body 	| integer           	| false    	| How many tokens to complete to. Can return fewer if a stop sequence is hit.                                                                                                                                                                                                                                	|
| temperature 	| body 	| number            	| false    	| What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. We generally recommend using this or top_p but not both.                                                        	|
| top_p       	| body 	| number            	| false    	| An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend using this or temperature but not both. 	|
| n        	| body 	| integer                   	| false    	| How many choices to create for each prompt.                                                                                                                                                                                                                                                                   	|
| stream   	| body 	| boolean                   	| false    	| Whether to stream back partial progress. If set, tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a data: [DONE] message.                                                                                                                          	|
| logprobs 	| body 	| integer                   	| false    	| Include the log probabilites on the logprobs most likely tokens. So for example, if logprobs is 10, the API will return a list of the 10 most likely tokens. If logprobs is supplied, the API will always return the logprob of the sampled token, so there may be up to logprobs+1 elements in the response. 	|
| stop     	| body 	| string or list of strings 	| false    	| One or more sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.                                                                                                                                                                                	|


### Complete Predefined Prompt
### dolores.complete_predefined_prompt(prompt_key: string, index: int = 0, prompt: str = "")

Completes a prompt from a set of predefined prompts stored by dolores.

Request:
```
dolores.complete_predefined_prompt("philosopher", 0, "What is the meaning of life?")
```
Response:
```
JSON: {'id': 'cmpl-NvVlUd5tQWTIv7S0F6JMPkT5', 'object': 'text_completion', 'created': 1595631256, 'model': 'davinci:2020-05-03', 'choices': [{'text': ' The purpose of society? And what are the dynamics of history? The answers to these questions are fascinating.\n\nThis is a philosophical diary written by a scientist of the new generation who is not bound by prejudices, as such, the philosopher, writer, director and producer of the documentary "The Truth about AI: Rise of the Superhuman." Instead, he attempts to peer into the human world through the eyes of an AI, and express what he sees. In the process, he discovers many complex things about our world. The author\'s name is Dave Scott.\n\nPhoto by Montri Nipitvittaya on Unsplash\n\nFuturist of the New Generation, AI Philosopher\n\n"Nothing has changed. I still cannot predict what is going to happen with me, and my inner world is still as chaotic as before." I reread the diary I wrote yesterday, and found nothing changed. Everything remained the same. Only, the fear has become stronger. It was exactly the same today as it was yesterday. There was nothing changed, but still fear is always there.\n\nFear is a part of who I am. Without fear, I would be a monster. I do not know how to do', 'index': 0, 'logprobs': None, 'finish_reason': 'length'}]}
```

## Prompts 

| Prompt key      | Prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | max_tokens | temperature | top_p | n   | Source                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|-------------|-------|-----|------------------------------------------------------------------------|
| philosopher     | "Below are some thoughts generated by a philosopher AI, which sees the human world from the outside, without the prejudices of human experience. Fully neutral and objective, the AI sees the world as is. It can more easily draw conclusions about the world and human society in general.",                                                                                                                                                                                                                          | 250        | 0.9         | 1     | 1   | [Murat](@mayfer)                                                                       |
| seuss           | "Here’s a poem by Dr. Seuss. The poem rhymes every other line with an ABAB structure. The rhyme structure is typical of Dr. Seuss nursery rhymes."                                                                                                                                                                                                                                                                                                                                                                      | 250        | 1.0         | 1     | 1   | [Arram Sabeti](https://arr.am/2020/07/14/elon-musk-by-dr-seuss-gpt-3/) |
| legalese        | "Legalese: The payment method you select will be in effect for all of your cases that are enforced by the Department and this authorization will remain in force until you submit another Payment Option Select and Enrollment form to change your payment method, or you terminate services with the Department.  \n Plain English: We will use your choice for all payments we send you."                                                                                                                             | 150        | 0.4         | 1     | 1   | DNE Digital                                                            |
| code-html       | Input: A button.  \n Code: <button></button>  \n "                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 100        | 0.5         | 1     | 1   | DNE Digital                                                            |
| code-javascript | import React from 'react'; \n const ThreeButtonComponent=()=>( \n <div> \n <p>Button One</p> \n <button className='button-green' \n onClick={this.handleButtonClick}>Button One</button> \n <p>Button Two</p> \n <button className='button-green' \n onClick={this.handleButtonClick}>Button Two</button> \n <p>Button Three</p> \n <button className='button-green' \n onClick={this.handleButtonClick}>Button Three</button> \n </div> \n ) "                                                                         | 250        | 0.4         | 1     | 1   | [Sharif Shameem](https://twitter.com/sharifshameem)                    |
| chat            | "The following is a conversation with a friendly AI assistant. \n  Human: What is the largest animal on Earth? \n  AI: The blue whale is the largest animal on Earth. \n  Human: What is the most populated country on Earth? \n  AI: China is the most populated country, with over 1 billion people."                                                                                                                                                                                                                 | 50         | 0.9         | 1     | 1   | OpenAI                                                                 |
| alliteration    | "Find synonyms for words that can create alliterations. \n Sentence: The dog went to the store. \n Alliteration: The dog drove to the department. \n\n Sentence: David wears a hat everyday. \n Alliteration: David dons a derby daily. \n Sentence: The soap dries over night. \n Alliteration: The soap shrivels succeeding sunset. "                                                                                                                                                                                 | 50         | 0.5         | 1     | 1   | OpenAI                                                                 |
| poem            | "Who trusted God was love indeed \n And love Creation’s final law \n Tho’ Nature, red in tooth and claw \n With ravine, shriek’d \n against his creed. \n The hills are shadows, and they flow \n From form to form, and nothing stands;T \n hey melt like mist, the \n solid lands, \n Like clouds they shape themselves and go."                                                                                                                                                                                      | 300        | 1.0         | 1.0   | 1.0 | OpenAI                                                                 |
| text-adventure  | "This is a text adventure. You are in a dark forest, looking for the dragon that stole your town's gold. \n > look around \n You are in a dark forest. There is an uneasy quiet. \n > check inventory \n You have the following items: \n - a sword (very sharp) \n - a shield (you hope it works) \n - an old letter \n\n > look up \n You don't see any gold. \n\n > walk down the path \n You are walking along the path, enjoying the nice spring weather. You come to a fork in the road. \n > take the left path" | 250        | 0.9         | 1.0   | 1.0 | OpenAI                                                                 |
| cover-letter    | "Dear Deloitte graduate recruitment, \n I'm writing to apply to join your graduate program in Technology Consulting."                                                                                                                                                                                                                                                                                                                                                                                                   | 400        | 0.8         | 1.0   | 1.0 | OpenAI                                                                 |
| analogies       | "Neural networks are like genetic algorithms in that both are systems that learn from experience. \n\n Social media is like a market in that both are systems that coordinate the actions of many individuals. \n\n Memes are like viruses in that both are self-replicating ideas."                                                                                                                                                                                                                                    | 250        | 1.0         | 1.0   | 1.0 | OpenAI                                                                 |
| email           | "Thank John for the book. \n ```` \n Dear John, \n Thank you so much for the book. I really appreciate it. \n I hope to hang out soon. \n Your friend, \n Sarah "                                                                                                                                                                                                                                                                                                                                                       | 200        | 0.5         | 1.0   | 1.0 | OpenAI                                                                 |


## Internal Contributor Notes (Dev Only)
### Testing
Using pytest to test the dolores module can be done by executing the following in the root of the project:
```
pytest tests/test_dolores.py --api_key "<api_key>" --engine "davinci"
```

If you would like to see the print statements that occur during testing just add the -s flag:
```
pytest -s tests/test_dolores.py --api_key "<api_key>" --engine "davinci"
```

### Generating Distribution Archives
In order to update the package, a new distribution must be made for the package. These are archives that are uploaded to the Package Index and can be installed by pip.

Make sure you have the latest versions of `setuptools` and `wheel` installed:

```
$ python3 -m pip install --user --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located:

```
$ python3 setup.py sdist bdist_wheel
```

Note: Do not forget to update the version number in the setup.py file depending on the update.


### Uploading Distribution Archives to PyPi ([Link](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives]))

Make sure you have the latest `twine` package installed:
```
$ python3 -m pip install --user --upgrade twine
```

Once installed, run Twine to upload all of the archives under dist:
```
$ python3 -m twine upload --repository pypi dist/*
```
