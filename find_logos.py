import requests
import re

text = requests.get('https://midasteknoloji.com/').text
urls = re.findall(r'https?://[^\'\"]+(?:logo|favicon)[^\'\"]*', text)
for u in set(urls):
    print(u)
