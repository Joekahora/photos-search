import requests
import json
import webbrowser

flickrApiKey = ""

def flickr_api_response(tagstring):
    dictionary_parameters = {}