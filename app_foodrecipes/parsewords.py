import requests 

url = 'https://kreekly.com/lists/3000-samyh-populyarnyh-angliyskih-slov/'

headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }



response = requests.get(url = url, headers=headers)

print(response.content.decode())