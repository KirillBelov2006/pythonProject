# import requests
# import json
#
# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# texts = json.loads(r.content)
# print(type(texts))
#
# for text in texts:
#     print(texts)

# import requests
# import json
#
# r = requests.get('https://api.github.com')
#
# d = json.loads(r.content)
# print(type(d))
# print(d["following_url"])


# import requests
#
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем POST-запрос
# print(r.content)  # содержимое ответа и его обработка происходит так же, как и с GET-запросами, разницы никакой нет

import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
r = json.loads(r.content)

print(r[0])





