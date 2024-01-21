import os
import numpy as np
import pandas as pd
import shutil
import logging


def extractor(src_folder, dest_folder, logs_folder,common_prefix):
    # List all files in the specified directory
    files = os.listdir(src_folder)
    # Filter files that start with the common prefix and end with ".csv"
    filtered_files = [file for file in files if file.startswith(common_prefix) and file.endswith(".csv")]
    # Iterate through the files to read
    for file in filtered_files:

        # Extract the table name and timestamp from the file name
        parts = file.split("_")
        timestamp = parts[0]
        table_name = parts[1].split(".")[0]

        new_file_name = f"{table_name}.csv"

        df = pd.read_csv(os.path.join(src_folder, file), delimiter=";")
        df = df.replace({np.nan: None})
        df.columns = map(lambda x: str(x).upper(), df.columns)
        df.to_csv(os.path.join(dest_folder, new_file_name), index=False)
        # Move the file from the source to the destination folder
        logging.info('new raw files placed in seed folder for DWH loading')
        shutil.move(os.path.join(src_folder, file), os.path.join(logs_folder, file))
        logging.info('new raw files moved to raw_files backup folder')

def move_files(src_folder, dest_folder, common_prefix):
    # List all files in the specified directory
    files = os.listdir(src_folder)


    # Iterate through the files to move
    for file in files:
        new_file = common_prefix + "_" + file

        # Move the file from the source to the destination folder
        shutil.move(os.path.join(src_folder, file), os.path.join(dest_folder, new_file))
        logging.info('files moved from seed folder to processed folder')



seed_folder = "../seeds"
processed_folder = "../logs/processed_files"
src_folder = "../src_data"
logs_folder = "../logs/raw_files"
script_directory = os.path.dirname(os.path.abspath(__file__))
src_folder = os.path.join(script_directory, src_folder)
logs_folder = os.path.join(script_directory, logs_folder)
processed_folder = os.path.join(script_directory, processed_folder)
seed_folder = os.path.join(script_directory, seed_folder)
#common_prefix = datetime.today().strftime("%Y%m%d") #+ "22"
common_prefix = "20201201"


extractor(src_folder, seed_folder, logs_folder, common_prefix)