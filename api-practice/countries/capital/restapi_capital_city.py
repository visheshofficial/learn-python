"""Module provide Search By Countri capability interfacing with external API"""

from typing import Dict, List, Any
import logging
from dataclasses import dataclass
import requests


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger()


class APIClient:
    """
    Handle communication with external APIs
    Responsible for making HTTP requests and handling resposne
    """

    def __init__(self, base_url) -> None:
        """
        Initialize API Client with the base url
        """
        self.base_url = base_url
        self.session = requests.session()

    def get(self, params=None):
        """
        Make GET request to API with the provided parameters
        """
        try:
            url = f"{self.base_url}"
            resposne = self.session.get(url=url, params=params)
            resposne.raise_for_status()
            return resposne.json()
        except requests.exceptions.HTTPError as http_error:
            logger.error("Http error occuered: %s", http_error)
        except requests.exceptions.RequestException as req_exception:
            logger.error("RequestException error occuered: %s", req_exception)
        except Exception as exception:
            logger.error("An exception occured: %s", exception)
        return {}


@dataclass
class Country:
    """
    Represent a country with it's relevant information
    """
    name: str
    population: int
    region: str

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create country object from directory
        """
        return cls(
            name=data.get("name"),
            population=data.get("population"),
            region=data.get("region"),
        )


class CountrySearchService:
    """
    Service that provides search functionality for countries
    """

    def __init__(self, api_client: APIClient) -> None:
        self.api_client = api_client

    def search_countries(self, region: str, keyword: str) -> List[Country]:
        """
        Search countries based on region and keyword in the name of the country
        """
        countries: List[Country] = []
        page = 1
        while True:
            params = {"page": page, "region": region, "name": keyword}
            resposne = self.api_client.get(params=params)

            countries.extend([Country.from_dict(x) for x in resposne.get("data", {})])

            if page >= resposne.get("total_pages", 0):
                break
            page += 1

        return countries

    def format_and_sort_countries(self, countries: List[Country]):
        """
        Format and sort countries by name and then by population
        """
        sorted_data = sorted(countries, key=lambda c: [c.name, c.population])
        return [str(c) for c in sorted_data]


if __name__ == "__main__":
    logger.info("User logged in")

    country_search_service = CountrySearchService(
        api_client=APIClient(
            base_url="https://jsonmock.hackerrank.com/api/countries/search"
        )
    )

    region = "europe"
    keyword = "land"
    countries_result = country_search_service.search_countries(
        region=region, keyword=keyword
    )
    formatted_sorted = country_search_service.format_and_sort_countries(
        countries_result
    )
    for country in formatted_sorted:
        print(country)
