import requests
import logging
import pprint
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_country_by_region_and_keyword(url:str,region:str,keyword:str)->List:
    """
    Fetch countries mathcing the provided criteria.
    """
    countries = []
    page = 1
    try:
        while True:

            params = {"page": page,"region":region,"name":keyword}
            resposne = requests.get(url, params=params)
            data = resposne.json()
            # print(data)
            resposne.raise_for_status()

            countries.extend(data.get("data", []))

            if page == data.get("total_pages",0):
                break
            page += 1
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.RequestException as e:
        print(e)
    except Exception as e:
        print(e)
    return countries


def format_and_sort(countries):

    for country in countries:
        print(country("name"))
        if country.get("population",0):
            country["population"]=0

    sorted_countries=sorted(countries, key = lambda c:(c.population,c.name))
    return sorted_countries

def find_contries(url:str) -> List[str] :
    countries= fetch_country_by_region_and_keyword(url,"Asia","stan")

    format_and_sort(countries)



def main():
    """
    Entrypoint of the application
    """

    BASE_URL = "https://jsonmock.hackerrank.com/api/countries/search"

    countries = find_contries(BASE_URL)
    if countries:
        pprint.pprint([ (x["name"],x["population"],x["region"]) for x in countries])


if __name__ == "__main__":
    main()
