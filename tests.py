from tv_episode import *

# Run test scenarios
if tv_episode_get_details_200() :
    print ("tv_episode_get_details_200: pass!")
else :
    tv_episode_get_details_200()

if tv_episode_get_details_404() :
    print ("tv_episode_get_details_404: pass!")
else :
    tv_episode_get_details_404()

if tv_episode_get_details_401() :
    print ("tv_episode_get_details_401: pass!")
else : tv_episode_get_details_401()

if tv_episode_get_details_append_videos() :
    print ("tv_episode_get_details_append_videos: pass!")
else : tv_episode_get_details_append_videos()

if tv_episode_rating_post_no_header() :
    print ("tv_episode_get_details_append_videos: pass!")
else : tv_episode_get_details_append_videos()
