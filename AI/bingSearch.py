# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# You may need the below as well
# pip install pipenv
# pipenv install requests
# <importsAndVars>
import json
import os
from pprint import pprint
import requests 

'''
This sample uses the Bing Custom Search API to search for a query topic and get back user-controlled web page results.
Bing Custom Search API: https://docs.microsoft.com/en-us/bing/search-apis/bing-custom-search/overview 
'''

# Add your Bing Custom Search subscription key and endpoint to your environment variables.
subscriptionKey = "e8947f61cbd74c03a7ceab5e830e494e"
endpoint = "https://www.bing.com/"
customConfigId = "780cd651-ec47-4dbe-910f-88fc2a2651f8"  # you can also use "1"
searchTerm = "中国大语言模型开源"
# </importsAndVars>
# <url>
# Add your Bing Custom Search endpoint to your environment variables.
url = endpoint + "/bingcustomsearch/v7.0/search?q=" + searchTerm + "&customconfig=" + customConfigId
# </url>
# <request>
r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
print(r.text)
#pprint(json.loads(r.text)) #返回不是完整的json数据,--报错了
# </request>
