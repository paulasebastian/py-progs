

import json
import pandas as pd


data = '''
{
    "weather": [
        {"location": {"city": "Kochi"}, "temperature": 30, "humidity": 75},
        {"location": {"city": "Thrissur"}, "temperature": 32, "humidity": 70},
        {"location": {"city": "Kozhikode"}, "temperature": 29, "humidity": 80}
    ]
}
'''


weather_data = json.loads(data)


df = pd.json_normalize(weather_data["weather"])


df = df.rename(columns={
    "location.city": "City",
    "temperature": "Temperature",
    "humidity": "Humidity"
})


print("Weather Information:")
print(df)


print("\nAverage Temperature:", round(df["Temperature"].mean(), 2))
print("Average Humidity:", round(df["Humidity"].mean(), 2))


print("\nWeather Report for Each City:")
for index, row in df.iterrows():
    print(row["City"], "- Temperature:", row["Temperature"],
          "°C, Humidity:", row["Humidity"], "%")