import requests
r=requests.get("https//api.github.com/events") #this is the url for the github api, we are making a get request to this url to get the events data from github
print(r) #this will print the response object, which contains the status code and the data from the api
