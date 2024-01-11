import requests
from bs4 import BeautifulSoup

# Define the URL of the article
url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"

# Send an HTTP GET request to the URL and retrieve the HTML content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the title of the article
    title = soup.find("h1", class_="headline__text inline-placeholder").text

    # Find and extract the main content of the article
    content = ""
    article_body = soup.find("div", class_="article__content")
    paragraphs = article_body.find_all("p")
    for paragraph in paragraphs:
        content += paragraph.text + "\n"

    # Find and extract the updated date of the article
    updated_date = soup.find("div", class_="timestamp").text

    # Find and extract the author of the article
    author = soup.find("span", class_="byline__name").text

    # Print the titlem updated date and content of the article
    print("Title:", title)
    print("Author:", author)
    print("Updated Date:", updated_date)
    print("\nContent:")
    print(content)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
