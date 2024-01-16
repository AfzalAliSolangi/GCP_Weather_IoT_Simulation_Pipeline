# GCP_Weather_IoT_Simulation_Pipeline
### Description:
WeatherIoTSimulationPipeline is a Python project that simulates IoT sensor devices gathering weather data. The simulated sensors generate atmospheric pressure, cloud formation, wind speed, humidity, and rain intensity readings. These readings are then sent to Google Cloud Pub/Sub for message queuing.

The data is processed through Google Cloud Dataflow, where it undergoes real-time processing, transformation, and enrichment. Finally, the processed weather data is stored in a Google BigQuery table for further analysis and querying.

This project serves as a comprehensive simulation pipeline, emulating the end-to-end flow of weather data from IoT devices to a scalable and analytics-friendly data storage solution.

### Project Architecture:
![Project_architecture](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/9ca46e82-b825-4591-8126-fed49abcb35e)

### Services Used in WeatherIoT Simulation Pipeline

1. **Google Cloud Pub/Sub**
   - Google Cloud Pub/Sub is a messaging service that enables real-time communication between components of a distributed system. In this    
     project, Pub/Sub serves as the messaging middleware for IoT devices, allowing simulated sensors to publish weather data messages to a 
     designated topic.

2. **Google Cloud BigQuery**
   - Google Cloud BigQuery is a fully-managed, serverless data warehouse that enables super-fast SQL queries using the processing power of             Google's infrastructure. In this project, BigQuery is used to store and manage the processed weather data in a structured table,             
     facilitating efficient analytics and querying.

3. **Google Cloud Dataflow**
   - Google Cloud Dataflow is a fully managed stream and batch processing service that enables users to process data in real-time or batch mode.       In this project, Dataflow is employed to process, transform, and enrich the incoming weather data messages from Pub/Sub. It provides a       
     scalable and parallelized processing environment for handling large volumes of data.

4. **Python Code**
   - The Python code is the core of the WeatherIoT Simulation Pipeline. It simulates IoT sensor devices, generating weather data readings such as      atmospheric pressure, cloud formation, wind speed, humidity, and rain intensity. The code then publishes these readings to the Pub/Sub    
     topic, initiating the entire data processing pipeline.

5. **BigQuery Table**
   - The BigQuery table is the destination for the processed weather data. The table structure is designed to accommodate the enriched data from       Dataflow, making it easy to perform analytics and queries on the collected information. It serves as the persistent storage solution for the      final output of the simulation pipeline.

    These services collectively form an end-to-end data processing pipeline, allowing users to simulate and analyze weather data in a scalable 
    and cloud-native environment.



### Steps to Set Up

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
     ![image](https://github.com/AfzalAliSolangi/GCP_Weather_IoT_Simulation_Pipeline/assets/100179604/0d9de178-7c3f-4627-816c-d09920a4c087)


## Usage

Instead of simulating the IoT devices this Architecture can be hooked with actual IoT devices and the analysis can be conducted using BigQuery. 


