""" Module provide Search By Countri capability interfacing with external API"""

from typing import  Dict, List, Any
import logging
import requests


# Configure logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s")
logger=logging.getLogger()

class APIClient:
    """
    Handle communication with external APIs
    Responsible for making HTTP requests and handling resposne
    """
    def __init__(self, base_url) -> None:
        """
        
        """
        self.base_url = base_url
        self.session=requests.session()

    def get(self,params=None):
        try:
            url=f"{self.base_url}"
            resposne=self.session.get(url=url,params=params)
            resposne.raise_for_status()
            return resposne.json()
        except requests.exceptions.HTTPError as httpError:
            logger.error(f"Http error occuered: {httpError}")
        except requests.exceptions.RequestException as reqException:
            logger.error(f"RequestException error occuered: {reqException}")
        except Exception as exception:
            logger.error(f"An exception occured: {exception}")
        return {}

class Country:
    """
    Represent a country with it's relevant information
    """
    def __init__(self,name:str,region:str, population:int) -> None:
        """ 
        Initilize Country object
        """
        self.name=name
        self.popolation=population
        self.region=region
    
    @classmethod
    def from_dict(cls,data:Dict[str,Any]):
        return cls(name=data.get("name"),region=data.get("region"),population=data.get("population"))
    
    def __str__(self)->str:
        return f"{self.name} | {self.region} | {self.popolation} "

class CountrySearchService:
    def __init__(self,api_client:APIClient) -> None:
        self.api_client=api_client

    def search_countries(self,region:str,keyword:str)->List[Country]:
        countries:List[Country]=[]
        page = 1
        while True:
            params = {"page":page,"region":region,"name":keyword}
            resposne=self.api_client.get(params=params)

            countries.extend([Country.from_dict(x) for x in resposne.get("data",{})])

            if page>=resposne.get("total_pages",0):
                break
            page+=1

        return countries
    
    def format_and_sort_countries(self, countries:List[Country]):
        return sorted(countries,key=lambda c : [c.name,c.popolation])



if __name__=="__main__":
    logger.info("User logged in")
    api_client=APIClient(base_url="https://jsonmock.hackerrank.com/api/countries/search")
    country_search_service=CountrySearchService(api_client=api_client)
    countries=country_search_service.search_countries("asia","stan")
    formatted_sorted=country_search_service.format_and_sort_countries(countries)
    for country  in formatted_sorted:
        print(country)
