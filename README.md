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
Either do so in the python interpreter or in a python file.
#### dolores.initialize(api_key: str, engine_name: str)

```
from dolores import Dolores

dolores.initialize"80085", "davinci")
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
