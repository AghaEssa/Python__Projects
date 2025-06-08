
import csv
import requests
from bs4 import BeautifulSoup

# Ask the user for a car brand
car = input("Enter car brand (e.g., suzuki): ")
url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'
headers = {'User-Agent': 'Mozilla/5.0'}

# Make a request to the URL
response = requests.get(url, headers=headers)
print(f"Fetching data from: {response.url}")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Open a CSV file to write the results
    with open('car_prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Car Name', 'Price'])  # Write header

        # Find all tables in the HTML
        tables = soup.find_all('table')


        # Loop through each table and extract car names and prices
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:  # Ensure there are at least 2 columns
                    car_name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    writer.writerow([car_name, price])  # Write data to CSV

else:
    print("Failed to fetch data.")

with open('car_prices.csv', mode='r' , encoding='utf-8') as file22:
    reader = csv.reader(file22)
    next(reader)

    print('first five entries ....')
    for i in range (5):
        print(next(reader))

