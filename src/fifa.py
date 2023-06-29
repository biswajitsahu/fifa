import collections

import requests
from bs4 import BeautifulSoup
from src.data import countries

BASE_URL = "https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup_squads"


class Fifa:
    def __init__(self, year: int):
        self.year = year
        self.data = self.get_master_data()

    def get_url(self):
        return BASE_URL.format(year=self.year)

    def get_master_data(self):
        """
        Generate master data for the respective year.
        :return:
            Dictionary with key as country and value as list of player details.
            {
                'England': [{
                                'player_name': 'p1',
                                'dob': 'd1',
                                'caps': 'caps1',
                                'club': 'club1'
                              },
                              {
                                'player_name': 'p2',
                                'dob': 'd2',
                                'caps': 'caps2',
                                'club': 'club2'
                              }
                'Argentina': [{
                                'player_name': 'p3',
                                'dob': 'd3',
                                'caps': 'caps3',
                                'club': 'club3'
                              },
                              {
                                'player_name': 'p4',
                                'dob': 'd4',
                                'caps': 'caps3',
                                'club': 'club4'
                              }
                            ]
            }
        """

        url = self.get_url()
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        h3_tags = soup.find_all("h3")
        fifa_data = collections.defaultdict(list)

        for country in countries:
            for h3_tag in h3_tags:
                country_data = h3_tag.find("span", text=country)
                if not country_data:
                    continue
                table = h3_tag.find_next_sibling("table")
                rows = table.find_all("tr")[1:]
                for row in rows:
                    player_data = {}
                    cells = row.find_all("td")
                    player_data['player_name'] = row.find('th').text.strip()
                    player_data['dob'] = cells[2].text.strip("()").split(")")[0].lstrip(" (")  # Extract date of birth
                    player_data['caps'] = cells[3].text.strip()  # Extract caps
                    player_data['club'] = cells[4].text.strip()  # Extract club name
                    fifa_data[country].append(player_data)
        return fifa_data

    def get_duplicate_bday_count(self):
        """
        This function returns no of teams having players sharing bday on same day.
        """

        count = 0
        for country, data in self.data.items():
            dob_array = set([player['dob'] for player in data])
            if len(data) != len(dob_array):
                count += 1
        return count


if __name__ == '__main__':
    fifa = Fifa(2022)
    print(fifa.get_duplicate_bday_count())
