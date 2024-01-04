import os
import zipfile

def extract_all_zip_in_folder(folder_path):
    # List all the files in the given folder
    for file in os.listdir(folder_path):
        # Check if the file is a zip file
        if file.endswith('.zip'):
            zip_path = os.path.join(folder_path, file)
            # Extract the folder name from the zip file name
            folder_name = os.path.splitext(file)[0]
            folder_path_to_extract = os.path.join(folder_path, folder_name)

            # Create the folder if it does not exist
            if not os.path.exists(folder_path_to_extract):
                os.makedirs(folder_path_to_extract)

            # Extract the zip file in the folder
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path_to_extract)
                print(f"Extracted {file} in {folder_path_to_extract}")

# Example usage - replace 'path_to_directory' with the path to your directory containing zip files
extract_all_zip_in_folder('/home/meron/Documents/work/tenacademy/week3/redash_llm_chatbot/data/youtube-data')
