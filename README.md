# GCP_Weather_IoT_Simulation_Pipeline

# Description:
WeatherIoTSimulationPipeline is a Python project that simulates IoT sensor devices gathering weather data. The simulated sensors generate atmospheric pressure, cloud formation, wind speed, humidity, and rain intensity readings. These readings are then sent to Google Cloud Pub/Sub for message queuing.

The data is processed through Google Cloud Dataflow, where it undergoes real-time processing, transformation, and enrichment. Finally, the processed weather data is stored in a Google BigQuery table for further analysis and querying.

This project serves as a comprehensive simulation pipeline, emulating the end-to-end flow of weather data from IoT devices to a scalable and analytics-friendly data storage solution.
