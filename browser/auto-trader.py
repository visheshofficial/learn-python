import json
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Configure WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

def extract_car_details(url):
    """Extracts car details from an AutoTrader listing using Selenium."""
    
    # Start Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(5)  # Allow time for JavaScript to load

    # Get the page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Extract JSON-LD structured data
    json_ld_tag = soup.find("script", type="application/ld+json")
    json_ld_data = json.loads(json_ld_tag.string) if json_ld_tag else {}

    # Extract relevant car details
    car_details = {
        "Title": json_ld_data.get("name", "Not found"),
        "Price": json_ld_data.get("offers", {}).get("price", "Not found"),
        "Make": json_ld_data.get("brand", {}).get("name", "Not found"),
        "Model": json_ld_data.get("model", "Not found"),
        "Year": json_ld_data.get("productionDate", "Not found"),
        "Fuel Type": json_ld_data.get("fuelType", "Not found"),
        "Mileage": json_ld_data.get("mileageFromOdometer", {}).get("value", "Not found"),
        "Transmission": json_ld_data.get("vehicleTransmission", "Not found"),
        "Location": json_ld_data.get("offers", {}).get("availableAtOrFrom", {}).get("address", {}).get("addressLocality", "Not found"),
        "Seller": json_ld_data.get("offers", {}).get("seller", {}).get("name", "Not found"),
        "Images": json_ld_data.get("image", []),
        "URL": url
    }

    return car_details

# Example URL
car_url = "https://www.autotrader.co.uk/car-details/202501127959996"

# Extract details and print
car_data = extract_car_details(car_url)
print(json.dumps(car_data, indent=4))

# Save data to CSV (optional)
csv_file = "car_listings.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=car_data.keys())
    writer.writeheader()
    writer.writerow(car_data)

print(f"Car details saved to {csv_file}")
