import webbrowser
from urllib.parse import urlencode

def generate_autotrader_url():
    """
    Generates an AutoTrader search URL with predefined parameters.
    """
    base_url = "https://www.autotrader.co.uk/car-search"
    
    # Configurable search parameters
    postcode = "RG6 3HA"  # User's postcode
    price_from = 3500  # Minimum price of the car
    price_to = 5500  # Maximum price of the car
    radius = 50  # Search radius in miles
    year_from = 2015  # Minimum car model year
    max_mileage = 100000  # Maximum mileage allowed
    min_engine_power = 100  # Minimum engine power in HP
    body_type = "Hatchback"  # Type of car body
    fuel_types = ["Petrol", "Petrol Hybrid", "Petrol Plug-in Hybrid"]  # Fuel type options
    transmission = "Manual"  # Type of transmission
    seller_type = "trade"  # Type of seller (private/trade)
    doors = 5  # Number of doors in the car
    sort = "year-dsc"  # Sorting preference (descending by year)
    
    query_params = {
        "annual-tax-cars": "TO_35",
        "body-type": body_type,
        "exclude-writeoff-categories": "on",
        "fuel-type": fuel_types,
        "maximum-mileage": max_mileage,
        "min-engine-power": min_engine_power,
        "postcode": postcode,
        "price-from": price_from,
        "price-to": price_to,
        "quantity-of-doors": doors,
        "radius": radius,
        "seller-type": seller_type,
        "sort": sort,
        "transmission": transmission,
        "year-from": year_from
    }
    
    url = f"{base_url}?{urlencode(query_params, doseq=True)}"
    return url

def open_autotrader_search():
    """
    Opens the AutoTrader search link in the default web browser.
    """
    url = generate_autotrader_url()
    print(f"Opening URL: {url}")
    webbrowser.open(url)

# Execute the function
open_autotrader_search()
