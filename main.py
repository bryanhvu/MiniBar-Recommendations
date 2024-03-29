import os.path
import csv
import lxml
import json
import requests
from bs4 import BeautifulSoup


if os.path.isfile('./cocktails_and_ingredients.json'):
    # TODO add google trend api calls
    pass
else:
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

    count = 0
    ingredients = []
    top_cocktail_avail = []
    for cocktail in top_cocktail_names:
        api_url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail}'
        api_response = requests.get(api_url)
        result = api_response.json()['drinks']
        if result is not None:
            ingredients.append([val for key, val in result[0].items() if key.startswith('strIngredient') and val is not None])
            top_cocktail_avail.append(cocktail)
        count += 1
        print(f'{count/len(top_cocktail_names)*100:.2f}% complete')

    top_cocktails = {
        "names": top_cocktail_avail,
        "ingredients": ingredients,
    }

    top_cocktails_and_ingredients = json.dumps(top_cocktails, indent=4)

    with open("cocktails_and_ingredients.json", "w") as outfile:
        outfile.write(top_cocktails_and_ingredients)
