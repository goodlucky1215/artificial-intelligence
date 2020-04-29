import urllib.request as request
import json


json_str =  request.urlopen("http://api.github.com/repositories").read().decode('utf8')
output = json.loads(json_str)

print(type(output))
print(output)


for item in output:
    print(item["name"])
    print(item["id"])
    print(item["owner"]["id"])
    print()
