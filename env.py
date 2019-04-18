#add your API key here
API_KEY =  #{YOUR API KEY HERE}

# base url for API
base_url = 'https://api.themoviedb.org/3'

# tv episode - tv id 1399 info
tv_id = 1399 # Game of Thones
season_number = 4
episode_number = 3
episode_name = 'Breaker of Chains'
header = {
'content-type': "application/json;charset=utf-8"
}
site = 'YouTube'

# urls / params variables
tv_episode_endpoint_url = '/tv/' + str(tv_id) + '/season/' + str(season_number) + '/episode/' + str(episode_number)
tv_episode_endpoint_url_append = tv_episode_endpoint_url + "?api_key=" + API_KEY + "&append_to_response=videos"
base_params = {
'api_key': API_KEY,
'language': 'en-US'
}

# invalid data
invalid_episode_number = 'abc'
invalid_tv_episode_endpoint_url = '/tv/' + str(tv_id) + '/season/' + str(season_number) + '/episode/' + str(invalid_episode_number)
invalid_api_params = {
'api_key': 'abc1234567',
'language': 'en-US'
}

#error messages
error_401 = 'Invalid API key: You must be granted a valid key.'
error_404 = 'The resource you requested could not be found.'
status_200 = "status should be 200"
