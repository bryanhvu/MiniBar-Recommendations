import lxml
import requests
from bs4 import BeautifulSoup

# TODO webscrape top cocktail
top_cocktails = []
response1 = requests.get('https://www.thecocktailservice.co.uk/the-worlds-top-100-cocktails/')
soup1 = BeautifulSoup(response1.text, "lxml")

drinks1 = soup1.select("div [class~=flex-grow] > h2")
top_cocktails += [drink.get_text().split('. ')[1] for drink in drinks1 if len(drink.get_text()) > 0]


response2 = requests.get('https://www.socialandcocktail.co.uk/top-100-cocktails/')
soup2 = BeautifulSoup(response2.text, "lxml")

drink2 = soup2.select("div [class~=pjax] h3")
top_cocktails += [drink.get_text() for drink in drink2]

# TODO remove duplicate entries

print()
# div class="recipe_summary pjax" > h3

# TODO construct drink dictionary (data frame friendly)


# TODO compile general ingredient costs?
