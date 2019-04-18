from env import *

# generates url path for request depending on endpoint needs
def url_generator (url, endpoint_url, sub = None) :
     global base_url
     sub = "" # needed to handle additional endpoint info passed in the url if needed
     url = base_url + endpoint_url + sub
     return url
