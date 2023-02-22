import json
from urllib import request, parse


def post(url, data=None):
  data = parse.urlencode(data).encode("utf-8")
  req = request.Request(url, data)
  response = request.urlopen(req)
  output = response.read().decode("utf-8")
  return output


def get(url):
  response = request.urlopen(url)
  output = response.read().decode("utf-8")
  return json.loads(output)
