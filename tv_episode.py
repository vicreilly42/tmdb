import requests, json
from helper import *

# this are some test scenarios for the tv episode episode endpoint

def tv_episode_get_details_200():
    """
    TODO: Get Details - This GET request will have valid path params (tv_id, season_number, episode_number) and the status code
    returned should be 200, the episode name and number should be match expected values. This will test a basic happy flow and validate expected data.
    """
    path = url_generator(base_url,tv_episode_endpoint_url) # create the specific url for the test
    response = requests.request('GET', path, data=base_params) # makes a get request with url and params and saves it in 'response'
    r = response.json() # converts response to json to make assert checks easier
    assert response.status_code == 200, status_200
    assert r['episode_number'] == episode_number, 'returned unexpected episode number'
    assert r['name'] == episode_name, 'returned unexpected episode name'
    return True #this is hacky as shit

def tv_episode_get_details_404():
    """
    TODO: Get Details - This GET request will have invalid path param (invalid tv episode number) and should return a 404 and resource not found status message.
    This will validate that bad urls for this path fail properly.
    """
    path = url_generator(base_url, invalid_tv_episode_endpoint_url)
    response = requests.request('GET', path, data=base_params)
    r = response.json()
    assert response.status_code == 404, ('status code should be 404, ' + str(response.status_code) + ' was returned instead.')
    assert r['status_message'] == error_404, ('the error message shoud be: ' + error_404)
    return True

def tv_episode_get_details_401():
    """
    TODO: Get Details - This GET request with an invalid api key should return a 401 and an invalid api key status message.
    This will validate that api keys are being checked before allowing access to the api.
    """
    path = url_generator(base_url, tv_episode_endpoint_url,invalid_api_params)
    response = requests.request("GET", path,)
    r = response.json()
    assert response.status_code == 401, ('status code should be 401, ' + str(response.status_code) + ' was returned instead.')
    assert r['status_message'] == error_401, ('the error message shoud be: ' + error_401)
    return True

def tv_episode_get_details_append_videos():
    """
    TODO: Get Details - This GET request with append_to_response with videos should return the details of the episode and associated videos all in one request.
    This will validate that append_to_reponse returned multiple correct responses in one request.
    """
    path = url_generator(base_url, tv_episode_endpoint_url_append)
    response = requests.request('GET', path)
    r = response.json()
    assert r[u'videos'][u'results'][1][u'site'] == site, "video should be appended to request" # confirming youtube video is returned in request
    assert r['name'] == episode_name, 'returned unexpected episode name'
    assert response.status_code == 200, status_200
    return True

def tv_episode_get_details():
    """
    TODO: Get Details - This GET request with valid and invalid append_to_response (videos, foobar) should return 200 and episode details, videos - nothing for foobar.
    This will validate that the request does not fail despite an incorrect value for append_to_response and expected responses are correct for valid ones.
    """

def tv_episode_rating_post_200():
    """
    TODO: Rate TV Episode - This POST requests with valid path params(tv_id, season_number, episode_number), headers (content_type), API_KEY and request body should return 200 and "Success" in the status message.
    This tests a basic happy flow for a post for a tv episode rating and validate expected response.
    """

def tv_episode_rating_post_no_header():
    """
    TODO: Rate TV Episode - This POST request with valid path params, request body, and no headers should return 404 and "The resource you requested could not be found." as the status message.
    This validates that headers are required in the POST request and fails appropriately when missing.
    """

def tv_episode_rating_post_no_request_body():
    """
    TODO: Rate TV Episode - This POST request with valid path params and headers but no request body (value) should return 404 and "The resource you requested could not be found." as the status message.
    This validates that the request body ('value': some value ) is required and fails appropriately when missing.
    """

def tv_episode_rating_post_invalid_api_key():
    """
    TODO: Rate TV Episode - This POST request with an invalid API key should return a 401 and ""Invalid API key: You must be granted a valid key" status message.
    This validates that a invalid api key does not allow access to the api and fails with the expected error messages.
    """

def tv_episode_rating_post_no_session_id():
    """
    TODO: Rate TV Episode - This POST request has a valid API Key but the associated developer account does not have a valid guest or session ID and should return 401 and "Authentication failed: You do not have permissions to access the service" error.
    This validates the requirement that a developer account needs a valid api key with a guest or session id setup already for this POST request. This is different than sending a guest or session id in the query string as those are optional.
    """

def tv_episode_rating_post_rating_over_limit():
    """
    TODO: Rate TV Episode - This POST requeest with 'value' outside maximum for rating ('value':11) should fail.
    This will test that the boundary limit fails as expected for 'value'.
    """

def tv_episode_rating_post_no_value():
    """
    TODO: Rate TV Episode - This POST request with 'value' in request with empty value ('value':'') should fail.
    This will confirm that 'value' cannot be sent with no value and will fail appropriately.
    """

def tv_episode_rating_post_no_value():
    """
    TODO: Rate TV Episode - This POST request with an empty key in place of 'value' and a valid value ('':'4') should fail.
    This will confirm that 'value' cannot be empty and will fail appropriately.
    """

def tv_episode_rating_delete_200():
    """
    TODO: Delete Rating - This DELETE request with valid path parameters (tv_id, season_number, episode_number), headers (Content-Type: application/json;charset=utf-8), API_KEY (rating and guest or session id exists); should return 200 and status message 'The item/record was deleted successfully.'
    This will test the happy flow deleting a rating for a tv episode.
    """

def tv_episode_rating_delete_no_session_id():
    """
    TODO: Delete Rating - This DELETE request with no guest or session id associated with API_KEY developer account and should return 401 status with status message "Authentication failed: You do not have permissions to access the service".
    This will validate that the guest / session id assoicated with the API KEY requirement fails as expected and does not allow a delete to occur without it.
    """

def tv_episode_rating_delete_no_header():
    """
    TODO: Delete Rating - This DELETE request with no header with all other requirements fullfilled should return a 404 and "The resource you requested could not be found." as the status message."
    This will validate that the request is respecting the header requirements and fails as expected.
    """

def tv_episode_rating_delete_no_rating():
    """
    TODO: Delete Rating - This DELETE request with no existing / previously deleted rating associated with episode on the API KEY should fail.
    This will validate that we cannot delete something that doesn't exist or previously existed.
    """

def tv_episode_rating_delete_missing_header_value():
    """
    TODO: Delete Rating - This DELETE request with header missing value ('header': '') should fail.
    This validates that the request is respecting the header requirements by failing since the value of the key is missing.
    """
