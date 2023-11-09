# Summary

Setup up an api endpoint to take a websites url (eg: https://someapp.com/catalog/app/lists) and returns an shortened URL such as https://someapp.com/GeAi9P.

## Pre-requisites

1. python 3.11.6

## Starting The Service

1. Clone repo

    `git clone https://github.com/smetroid/URLShortening.git`

1. Change into URLShortening

    `cd URLShortening`

1. Create the virtual environment

    `python -m venv .venv`

1. Source the virtual env

    `source .venv/bin/activate`

1. Install python packages

    `pip install -r requirements.txt`

1. Start the flask app

    `waitress-serve 'shorturl:shorturl'`

## Usage

1. Shortening a url using curl

    ```
    curl --header "Content-Type: application/json" -X POST localhost:8080/encode --data '{"url": "https://www.yahoo.com/news/dog-adopted-7-years-pennsylvania-210548824.html"}'
    ```

    Result:

    ```
    {"id":"rcj3GA","short_url":"https://www.yahoo.com/rcj3GA"}
    ```

2. Retrieving original URL using the id above

    ```
    curl --header "Content-Type: application/json" -X POST localhost:5000/decode --data '{"id": "rcj3GA"}'
    ```

    Result:

    ```
    {"id":"rcj3GA","original_url":"https://www.yahoo.com/news/trump-legal-news-brief-live-updates-as-trump-takes-the-witness-stand-154827487.html"}
    ```

## Running Development Environment

1. Export the apps

    `export FLASK_APP=shorturl.py`

1. Start development server

    `flask run`

1. Running tests

    `pytest`

## VSCode Debug HowTo

I've included my `.vscode/settings`  which includes a `launch.json` file which you can use to run the VSCode debugger.  It may need to be updated based on your Operating System.
