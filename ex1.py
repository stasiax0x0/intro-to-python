#web scrapping in 4 lines

import request, re  # Import libraries for web requests and regular expressions
html = request.get("https://rte.ie").text  # Download the HTML content of the page
links = re.findall(r'href="(http.*?)"', html)  # Find all links that start with http
print(links)  # Print the list of found links