import random
import time
from google.cloud import pubsub_v1
import json

project_id = "academic-pier-405912"
topic = "weather_world"

cities = ["New York", "London", "Tokyo", "Sydney", "Paris", "Berlin"]

def simulate_sensor_readings():
    while True:
        atmospheric_pressure = str(round(random.uniform(980, 1020) + random.uniform(-1, 1), 2))  # in hPa with slight variations
        cloud_formation = str(min(100, max(0, round(random.gauss(50, 20)))))  # percentage with Gaussian distribution
        wind_speed = str(round(random.uniform(0, 30) + random.uniform(-2, 2), 2))  # in km/h with slight variations
        humidity = str(min(100, max(0, round(random.gauss(50, 15)))))  # percentage with Gaussian distribution
        rain_intensity = str(round(max(0, random.gauss(2, 3)), 2))  # in mm/h with Gaussian distribution
        city = random.choice(cities)
        
        weather_dict = {
                    "atmospheric_pressure": "{}".format(atmospheric_pressure),
                    "cloud_formation": "{}".format(cloud_formation),
                    "wind_speed": "{}".format(wind_speed),
                    "humidity": "{}".format(humidity),
                    "rain_intensity": "{}".format(rain_intensity),
                    "city":"{}".format(city)
                       }

        json_weather_obj = json.dumps(weather_dict, indent = 4) 
        print(weather_dict) 

        publisher = pubsub_v1.PublisherClient()
        topic_name = 'projects/{}/topics/{}'.format(project_id,topic)  #Specifying the topic

        future = publisher.publish(topic_name, str.encode(json_weather_obj), spam='eggs')  #Publishing the topic
        future.result()

        time.sleep(5)  # Wait for 5 seconds before the next readings

if __name__ == "__main__":
    simulate_sensor_readings()
    