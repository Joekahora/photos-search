import requests
import json
import webbrowser

flickrApiKey = ""

def flickr_api_response(tagstring):
    baseurl = "https://api.flickr.com/services/rest/"
    dictionary_parameters = {}
    dictionary_parameters["apikey"] = flickrApiKey
