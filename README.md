# GCP_Weather_IoT_Simulation_Pipeline
### Description:
WeatherIoTSimulationPipeline is a Python project that simulates IoT sensor devices gathering weather data. The simulated sensors generate atmospheric pressure, cloud formation, wind speed, humidity, and rain intensity readings. These readings are then sent to Google Cloud Pub/Sub for message queuing.

The data is processed through Google Cloud Dataflow, where it undergoes real-time processing, transformation, and enrichment. Finally, the processed weather data is stored in a Google BigQuery table for further analysis and querying.

This project serves as a comprehensive simulation pipeline, emulating the end-to-end flow of weather data from IoT devices to a scalable and analytics-friendly data storage solution.

### Project Architecture:
![Project_architecture](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/9ca46e82-b825-4591-8126-fed49abcb35e)

### Services Used:


## Steps to Set Up

1. **Create a Topic**
   - Create a Google Cloud Pub/Sub topic to receive weather data messages.

2. **Create a Subscription for the Topic**
   - Set up a subscription for the created Pub/Sub topic to handle incoming messages.

3. **Create a Table in BigQuery**
   - Create a BigQuery table to store processed weather data.

4. **Create a Job in Dataflow**
   - Set up a Google Cloud Dataflow job for real-time processing, transformation, and enrichment of weather data.

5. **Modify Code**
   - Open the Python code and add the Pub/Sub topic name and Google Cloud project ID as configuration parameters.

6. **Run the Code**
   - Execute the Python code to simulate IoT devices, send data to Pub/Sub, and process it through Dataflow.

7. **Verify Data in BigQuery**
   - Check the BigQuery table to verify that the processed weather data has been successfully stored.

## Usage

Provide any additional details or considerations for users to effectively use and customize the WeatherIoT Simulation Pipeline.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.


