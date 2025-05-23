# BotPythonChatGPT

A simple Python project demonstrating how to interact with OpenAI's GPT models and Wikipedia using the OpenAI API and the `wikipedia` library.

## Purpose

This project was created as an experiment in creating a command line ChatGPT chat bot, or alternately to grab information from a website and then have ChatGPT summarize it.   It is currently used as a personal code reference.

## Features

- Send prompts to OpenAI's GPT models and receive responses.
- Summarize Wikipedia articles using GPT.
- Securely manage your OpenAI API key via environment variables.

## Requirements

- Python 3.7+
- [openai](https://pypi.org/project/openai/)
- [wikipedia](https://pypi.org/project/wikipedia/)

## Installation

```sh
git clone https://github.com/joncaudill/botpythonchatgpt.git
cd botpythonchatgpt
pip install openai wikipedia
```

## Setup

Set your OpenAI API key as an environment variable:

**Windows:**
```sh
set OPENAI_TEST_KEY=your_openai_api_key
```

**macOS/Linux:**
```sh
export OPENAI_TEST_KEY=your_openai_api_key
```

## Usage

### Basic Chat Example

Run the basic chat script:

```sh
python app.py
```

### Wikipedia Summarizer

Run the Wikipedia summarizer:

```sh
python wikibot.py
```

You will be prompted to enter the title of a Wikipedia article. The script will fetch the article and use GPT to generate a 5-bullet point summary.

## Files

- [`app.py`](app.py): Basic example of sending a prompt to OpenAI's GPT model.
- [`wikibot.py`](wikibot.py): Fetches a Wikipedia article and summarizes it using GPT.

## License

This project was created for Educational purposes