import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape():
    url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'wikitable'})

    # titles for columns in table
    world_titles = soup.find_all('th')

    world_table_titles = [title.text.strip() for title in world_titles]

    df = pd.DataFrame(columns=world_table_titles)

    column_data = table.find_all('tr')

    for row in column_data[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]

        if len(individual_row_data) < len(world_table_titles):
            individual_row_data += [None] * (len(world_table_titles) - len(individual_row_data))
        df = df._append(pd.Series(individual_row_data, index=df.columns), ignore_index=True)

    df.to_csv('scraped_data_wikipedia.csv', index=False)

    print('Data has been successfully scraped and saved to CSV.')


if __name__ == '__main__':
    scrape()
