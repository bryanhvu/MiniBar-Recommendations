import lxml
import requests
from bs4 import BeautifulSoup

# aggregate list of top cocktails
top_cocktail_names = []
response1 = requests.get('https://www.thecocktailservice.co.uk/the-worlds-top-100-cocktails/')
soup1 = BeautifulSoup(response1.text, "lxml")
drinks1 = soup1.select("div [class~=flex-grow] > h2")
top_cocktail_names += [drink.get_text().split('. ')[1] for drink in drinks1 if len(drink.get_text()) > 0]

response2 = requests.get('https://www.socialandcocktail.co.uk/top-100-cocktails/')
soup2 = BeautifulSoup(response2.text, "lxml")
drink2 = soup2.select("div [class~=pjax] h3")
top_cocktail_names += [drink.get_text() for drink in drink2]

# remove duplicate entries
top_cocktail_names = list(set(top_cocktail_names))


# TODO construct drink dictionary (data frame friendly)
# test for single query
# update to get nested list containing ingredients for each top cocktail item
cocktail = "margarita"
api_url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail}'
api_response = requests.get(api_url)
first_drink_result = api_response.json()['drinks'][0]
ingredients = [val for key, val in first_drink_result.items() if key.startswith('strIngredient') and val is not None]

top_cocktails = {
    "names": top_cocktail_names,
    "ingredients": ingredients,
}

print(api_response)

# TODO compile general ingredient costs?
