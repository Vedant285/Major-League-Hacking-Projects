import requests

def shorten_url(long_url):
    api_url = "http://tinyurl.com/api-create.php?url="
    response = requests.get(api_url + long_url)
    return response.text


short_url = shorten_url("https://www.example.com/this/is/a/very/long/url")
print(short_url)
