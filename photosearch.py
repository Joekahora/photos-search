import requests
import json
import webbrowser

flickrApiKey = "d35c727be4d635f05c0af09f9580557e"

def flickr_api_response(tagstring):
    baseurl = "https://api.flickr.com/services/rest/"
    dictionary_parameters = {}
    dictionary_parameters["api_key"] = flickrApiKey
    dictionary_parameters["tags"] = tagstring
    dictionary_parameters["tag_model"] = "all"
    dictionary_parameters["method"] = "flickr.photos.search"
    dictionary_parameters["per_page"] = 5
    dictionary_parameters["media"] = "photos"
    dictionary_parameters["format"] = "json"
    dictionary_parameters["nojsoncallback"] = 1
    flickr_result = requests.get(baseurl, params = dictionary_parameters)
    return flickr_result.json()

results = flickr_api_response(input())
print(json.dumps(results, indent=4))
photos_result = results["photos"]["photo"]
for photo in photos_result:
    owner = photo["owner"]
    photo_id = photo["id"]
    url = "https://www.flickr.com/photos/{}/{}".format(owner,photo_id)
    webbrowser.open(url)
