import requests
import json
import webbrowser

flickrApiKey = ""

def flickr_api_response(tagstring):
    baseurl = "https://api.flickr.com/services/rest/"
    dictionary_parameters = {}
    dictionary_parameters["apikey"] = flickrApiKey
    dictionary_parameters["tags"] = tagstring
    dictionary_parameters["tagmode"] = "all"
    dictionary_parameters["method"] = "flickr.photos.search"
    dictionary_parameters["per_page"] = 5
    dictionary_parameters["media"] = "photos"
    dictionary_parameters["format"] = "json"
    dictionary_parameters["nojscallback"] = 1
    flickr_result = requests.get(baseurl, params=dictionary_parameters)
    return flickr_result.json()


