import json


json_str = """[
 {"name":"사과","price":1000},
 {"name":"바나나","price":1500},
 {"name":"딸기","price":2000},
 {"name":"참외","price":3000},
 {"name":"수박","price":10000}
  ]"""

#JSON문자열 => 파이썬 자료형
output = json.loads(json_str)
print(output)
print()
#파이썬 자료형 => JSON문자열
text = json.dumps(output)
print(text)
