#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, render_template
import os
import json
import pandas as pd
import shutil

app = Flask(__name__)  # Pass __name__ as an argument to Flask()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Handle the uploaded file here
        file = request.files['file']
        rows = int(request.form['rows'])  # Get the number of rows from the form input
        filename = file.filename
        file_extension = os.path.splitext(filename)[1].lower()

        if file_extension == '.xlsx':
            converted_filename = convert_to_json_from_excel(file, rows)
        elif file_extension == '.csv':
            converted_filename = convert_to_json_from_csv(file, rows)
        else:
            return "Unsupported file format"

        converted_file_path = os.path.join('output', f"{converted_filename}.json")
        return render_template('result.html', filename=converted_filename, file_path=converted_file_path)

    return render_template('upload.html')

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def convert_to_json_from_excel(file, rows):
    working_path = os.getcwd()
    excel_folder = os.path.join(working_path, 'excel_folder')
    output_folder = os.path.join(working_path, 'output')
    create_directory(excel_folder)
    create_directory(output_folder)

    # Save the uploaded file to the excel folder
    file_path = os.path.join(excel_folder, file.filename)
    file.save(file_path)

    # Perform the conversion to JSON
    df = pd.read_excel(file_path, nrows=rows, dtype=str)
    converted_filename = os.path.splitext(file.filename)[0]
    converted_file_path = os.path.join(output_folder, f"{converted_filename}.json")
    df.to_json(converted_file_path, orient='records', indent=2)

    return converted_filename

def convert_to_json_from_csv(file, rows):
    working_path = os.getcwd()
    csv_folder = os.path.join(working_path, 'csv_folder')
    output_folder = os.path.join(working_path, 'output')
    create_directory(csv_folder)
    create_directory(output_folder)

    # Save the uploaded file to the csv folder
    file_path = os.path.join(csv_folder, file.filename)
    file.save(file_path)

    # Perform the conversion to JSON
    df = pd.read_csv(file_path, nrows=rows, dtype=str)
    converted_filename = os.path.splitext(file.filename)[0]
    converted_file_path = os.path.join(output_folder, f"{converted_filename}.json")
    df.to_json(converted_file_path, orient='records', indent=2)

    return converted_filename

def clear_directory(directory):
    folder_path = os.path.join(os.getcwd(), directory)
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

@app.route('/clear_files', methods=['POST'])
def clear_files():
    directories = ['output', 'excel_folder', 'csv_folder']
    for directory in directories:
        clear_directory(directory)
    return '''
        <h2>Files cleared successfully.</h2>
        <form action="/" method="get">
            <button type="submit">Go Home</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
