import requests
import pandas as pd

API_DEV = "XXXXXXXXXXXX"

def patch_ckan(name='Daily Water Level Data', 
                description='Test Data', 
                url='https://data.dev-wins.com/api/action/resource_patch', 
                path_to_file="daily_wl_data.csv", 
                resource_id="XXXXXX", 
                package_id="YYYYYY"):
    """
    Patch data to CKAN platform
    """
    files = {'upload': open(path_to_file, 'rb')}
    headers = {"API-Key": API_DEV}
    data_dict = {
        'id': resource_id,
        'package_id': package_id,
        'name': name,
        'description': description
    }
    # POST request
    response = requests.post(url, headers=headers, data=data_dict, files=files)
    
    # Logging
    print("Status Code", response.status_code)
    print("JSON Response", response.json())

patch_ckan(name='Testing2323', description='Test2323', url='https://data.dev-wins.com/api/3/action/resource_patch', pathtofile="example_data.csv", resource_id="7bc71960-6a9f-4189-94f1-6db211a912d6", package_id="702b0105-d9f7-4747-ba42-8fa2f36ae086")
