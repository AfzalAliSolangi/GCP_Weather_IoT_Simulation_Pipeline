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
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/a7c16b0c-907d-46d4-b34b-fd3cbaaf87ee)
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/6c5a79e9-68e5-455f-9302-70e116c522ec)

2. **Create a Subscription for the Topic**
   - Set up a subscription for the created Pub/Sub topic to handle incoming messages.
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/62be6f94-d975-457e-bcc8-36b8e69061bc)
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/80be73d2-4536-42e2-9a34-647d36fb292a)

3. **Create a Table in BigQuery**
   - Create a BigQuery table in the dataset to store processed weather data.
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/f190fa0b-f480-46a0-af10-6040eade503e)
   - Add the schema for the table
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/ddf54cb4-c414-4db9-94cc-4fa6793bd8bb)
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/c0db8e46-7b18-4df7-be3a-d7b1cf6abed8)
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/c21055cb-bc53-4ffd-b80f-b16446d727dd)

4. **Create a Job in Dataflow**
   - Set up a Google Cloud Dataflow job for real-time processing, transformation, and enrichment of weather data.
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/241d7eaf-dac8-4c9c-86ea-8bcecf6bb8c2)
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/981046df-b1a0-446b-9aff-80cb71201666)
   - Select the table from BigQuery and fill all the necessary input fields.
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/84e6463a-060f-4811-9bea-a3b70020d19f)
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/74d5dd1f-0c84-4e20-a696-eadefa91eb41)

5. **Modify Code**
   - Open the Python code and add the Pub/Sub topic name and Google Cloud project ID as configuration parameters.
   ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/ed25e360-037c-498f-96a9-3d2fce9fe955)


6. **Run the Code**
   - Execute the Python code to simulate IoT devices, send data to Pub/Sub, and process it through Dataflow.

7. **Verify Data in BigQuery**
   - Check the BigQuery table to verify that the processed weather data has been successfully stored.

## Usage

Provide any additional details or considerations for users to effectively use and customize the WeatherIoT Simulation Pipeline.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.


