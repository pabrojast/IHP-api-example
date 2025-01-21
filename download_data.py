import json
import requests
import os
from urllib.parse import urlparse

# Configure API URL
api_url = "https://ihp-wins.unesco.org/api/3/action/package_show?id=south-korea-hydrometeorological-data-from-wamis"
# Folder where files will be saved
destination_folder = 'south_korea_data'

def download_file(url, filename, destination_folder):
    """
    Downloads a file from a URL and saves it in the specified folder
    """
    try:
        # Create folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            
        # Complete file path
        file_path = os.path.join(destination_folder, filename)
        
        # Perform download
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Save file
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    
        print(f"File successfully downloaded: {filename}")
        return True
        
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")
        return False

def main():

    try:
        # Get API data
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        # Verify if response was successful
        if not data.get('success'):
            print("Error getting API data")
            return
        
        # Get resources list
        resources = data['result']['resources']
        
        # Downloaded files counter
        files_downloaded = 0
        
        # Download each resource
        for resource in resources:
            url = resource.get('url')
            name = resource.get('name')
            
            if url and name:
                # Create filename
                filename = f"{name.lower().replace(' ', '_')}.csv"
                
                # Try to download the file
                if download_file(url, filename, destination_folder):
                    files_downloaded += 1
                    print(f"Downloaded: {name}")
        
        print(f"\nProcess completed. {files_downloaded} files downloaded out of {len(resources)} resources.")
        
    except Exception as e:
        print(f"Error in process: {str(e)}")

if __name__ == "__main__":
    main()