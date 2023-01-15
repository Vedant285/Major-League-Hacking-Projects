# Major-League-Hacking-Projects


URL_Shortner : This code uses the requests library to make a GET request to the TinyURL API. The API expects the long URL to be appended to the end of the base URL, so we concatenate the two strings together before making the request. The response from the API is the shortened URL, which the function then returns.

It is important to notice that using external APIs like TinyURL has some limitations, such as rate limits and the possibility of the service being discontinued, so it is highly recommended to use a self-hosted URL shortener solution.
