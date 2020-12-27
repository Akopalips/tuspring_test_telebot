import json


if __name__ == '__main__':
   with open('conf.cfg', 'r') as fele:
      config = json.loads(fele.read())
   print(config['token'])
   