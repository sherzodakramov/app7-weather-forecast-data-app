import requests

API_KEY = "c9fe2db87b299fce404cbf97ddceb1bd"


def get_data(place, forecasted_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecasted_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecasted_days=3, kind="Sky"))
