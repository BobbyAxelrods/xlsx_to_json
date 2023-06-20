# XLSX to JSON Converter App

This simple web application allows you to convert XLSX files to JSON format. It is designed to assist web developers in converting XLSX files for testing table builders. The app provides the following features:

![alt text](https://miro.medium.com/v2/resize:fit:828/format:webp/1*VOSVN3CNVvXpyaS9GgOpoA.png)

## Features

1. **File Conversion:** Converts XLSX files to JSON format.
2. **Number of Rows:** Allows you to specify the number of rows to read from the XLSX file for faster conversion.
3. **Data Types as String:** Automatically treats all values as strings to avoid losing leading zeros (e.g., leading '000') during the conversion process.

## Complete Features 

1. **Upload and Save Output:** Provides an upload module and buttons to run the conversion script and save the output. This allows users to upload their XLSX files, convert them to JSON, and save the resulting JSON files for further use.
2. **Control Number of Rows:** Includes a module to control the number of rows to read from the XLSX file during conversion, giving users more flexibility in the conversion process.
3. **Download Converted Files:** Adds a button to download the converted JSON files directly from the app after the conversion process is complete.
4. **Clear Files Module:** Allows users to clear the working directory by removing any uploaded or converted files, providing a clean slate for new conversions.
5. **CSS Styling:** Enhances the app's appearance by adding CSS styling to each template, making it visually appealing and user-friendly.

## Upcoming Features 

1. Deploy in cloud so other can access 

## Getting Started

To run the XLSX to JSON Converter App locally, follow these steps:

1. Clone the repository: `git clone https://github.com/BobbyAxelrods/xlsx_to_json.git`
2. Start the server: `python app-flask.py`
3. Access the app in your browser at: `http://localhost:5000`

## Dependencies

The XLSX to JSON Converter App relies on the following dependencies:

- Express: Fast, unopinionated, minimalist web framework for Node.js.
- Multer: Middleware for handling multipart/form-data, used for file uploads.
- XLSX: Library for reading XLSX files and converting them to JSON.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. Make sure to follow the code style and conventions used in the project.

## License

This project is licensed under the [MIT License](LICENSE).


# Guide deploying apps to cloud VM (GCP)
# Deploying Flask App Using Google App Engine

This guide outlines the steps required to deploy a Flask app using Google App Engine.

## Prerequisites

Before deploying your Flask app, make sure you have the following files in your project directory:

1. **main.py**: This file contains your Flask application code.
2. **requirements.txt**: This file lists all the packages required for your Flask app to run.
3. **app.yaml**: This file defines the runtime you are using, for example: `runtime: python38`.

## Deployment Steps

Follow the steps below to deploy your Flask app to Google App Engine:

1. **Create a Google Cloud project**: Visit [Google Cloud Console](https://console.cloud.google.com/) and create a new project.

2. **Download Google Cloud SDK**: Download the Google Cloud SDK from the following link: [GoogleCloudSDKInstaller.exe](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe).

3. **Check if Google Cloud SDK is installed**: Open a command prompt and run the command `gcloud --version` to verify if the SDK is installed correctly.

4. **Login to Google Cloud**: Use the command `gcloud auth login` to log in to your Google Cloud account.

5. **Set your project**: Set your app to use the correct project by running the command `gcloud config set project <project-id>` where `<project-id>` is the name of the project you created in the Google Cloud Console.
- setup SQL instance 
- check compute instance `gcloud compute instances list`
- local ssh with cloud VM  `gcloud compute ssh main-vm002`
    - Install all dependencies such as python , pip, flask 
    - clone code from this repo in the vm 

6. **Deploy the app**: Use the command `gcloud app deploy` to deploy your Flask app to Google App Engine.

- location = 6
- 

7. **Stream logs**: You can stream logs from the command line by running `gcloud app logs tail -s default`.

8. **View your application**: To view your deployed application in a web browser, run the command `gcloud app browse`.

9. **Mitigating 502 bad gateway** : Go to console, click Logging -> & check code refferring to main or app-flask.py 
## Conclusion

By following these steps, you will be able to successfully deploy your Flask app using Google App Engine. For further details and advanced configurations, refer to the official [Google App Engine documentation](https://cloud.google.com/appengine/docs/standard).


## Deployment Steps manually with storage to avoid error readme system only

1. **Create a Google Cloud VM instance**: f1-micro / debian 10gb basic image

2. **Setup the firewall rule**: 
- 443 & 80 allowed , we need remapping 
- create more port for external access 
- all instances in network 
- source ipv4 0.0.0.0/0 to allow all to access 
-

3. **Setup the sql instances and mysql**: 
added 0.0.0.0/0 as an allowed network. This prefix will allow any IPv4 client to pass the network firewall and make login attempts to your instance, including clients you did not intend to allow. Clients still need valid credentials to successfully log in to your instance.


