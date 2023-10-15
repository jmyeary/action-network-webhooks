import flask
import json
import functions_framework


@functions_framework.http
def actnet_event(r: flask.request) -> flask.typing.ResponseReturnValue:
  request_json = r.get_json()

  #the things we will need to post
  event_name = request_json['title']
  event_venue = request_json['location']['venue']
  event_zip = request_json['location']['']
  event_description = request_json['description']
  event_startdate = request_json['start_date']
  event_address = request['location']['address_lines']
  event_state = request['location']['region']



  #return an http response
  return 'OK'