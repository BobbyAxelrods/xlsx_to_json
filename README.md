# XLSX to JSON Converter App

This simple web application allows you to convert XLSX files to JSON format. It is designed to assist web developers in converting XLSX files for testing table builders. The app provides the following features:

## Features

1. **File Conversion:** Converts XLSX files to JSON format.
2. **Number of Rows:** Allows you to specify the number of rows to read from the XLSX file for faster conversion.
3. **Data Types as String:** Automatically treats all values as strings to avoid losing leading zeros (e.g., leading '000') during the conversion process.

## Upcoming Features

1. **Upload and Save Output:** Provides an upload module and buttons to run the conversion script and save the output. This allows users to upload their XLSX files, convert them to JSON, and save the resulting JSON files for further use.
2. **Control Number of Rows:** Includes a module to control the number of rows to read from the XLSX file during conversion, giving users more flexibility in the conversion process.
3. **Download Converted Files:** Adds a button to download the converted JSON files directly from the app after the conversion process is complete.
4. **Clear Files Module:** Allows users to clear the working directory by removing any uploaded or converted files, providing a clean slate for new conversions.
5. **CSS Styling:** Enhances the app's appearance by adding CSS styling to each template, making it visually appealing and user-friendly.

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
