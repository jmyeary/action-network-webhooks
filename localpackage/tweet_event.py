from pytwitter import Api

#tweet_text: str
def send_tweet():

    with open('/etc/pubkey/twitter-access-token') as f:
        ACCESS_TOKEN=f.readline()[0]
    with open('/public/twitter-api-key') as f:
        CONSUMER_KEY=f.readline()[0]
    with open('/private/twitter-secret-api-key') as f:
        CONSUMER_SECRET=f.readline()[0]
    with open('/etc/privkey/twitter-secret-access-token') as f:
        SECRET_ACCESS_TOKEN=f.readline()[0]

    api = Api(consumer_key=CONSUMER_KEY,
              consumer_secret=CONSUMER_SECRET)

    auth_url = api.get_authorize_url()

    return api.generate_access_token(response=auth_url)
    # {
    #   'oauth_token': <'oauth-token'>,
    #   'oauth_token_secret': <'oauth-token-secret'>,
    #    'user_id': <'user id'>,
    #    'screen_name': <'screen name'>
    # }

send_tweet()