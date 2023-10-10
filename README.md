# JSON File Handling with Python

This repository contains three Python scripts for working with JSON files: **JSON File Writer**, **JSON File Appender**, and **JSON File Loader**. Each script performs a specific operation on a JSON file named `test_original.json`. 

## JSON File Writer (json_file_writer.py)

This script creates a new JSON file and writes specified data into it. It's useful for initializing JSON files with initial data.

**Usage:**

1. Run the script `json_file_writer.py`.

   ```shell
   python json_file_writer.py
   ```

2. The script will create `test_original.json` and write the specified data into it.

## JSON File Appender (json_file_appender.py)

This script appends new data to an existing JSON file. It allows you to add additional information to an existing JSON dataset.

**Usage:**

1. Run the script `json_file_appender.py`.

   ```shell
   python json_file_appender.py
   ```

2. The script will open `test_original.json`, append new data to it, and save the updated JSON content.

## JSON File Loader (json_file_loader.py)

This script loads and prints the contents of a JSON file. It's helpful for reading and displaying JSON data stored in a file.

**Usage:**

1. Run the script `json_file_loader.py`.

   ```shell
   python json_file_loader.py
   ```

2. The script will open `test_original.json` and display the JSON data stored in it.

For each script, ensure that you have `test_original.json` in the same directory as the scripts or provide the correct path to the file. These scripts demonstrate basic JSON file operations in Python, and you can modify the `data` variable in `json_file_writer.py` to store different JSON data.
