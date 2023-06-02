import os
import requests
import json

def getGasLimit(chain:str)->int:
     if chain == 'ETH':
          gas_limit = data['result'][0]['gasLimit']
          return gas_limit
     elif chain == 'OPT':
          gas_limit = data['result'][1]['gasLimit']
          return gas_limit
     elif chain == 'BSC':
          gas_limit = data['result'][2]['gasLimit']
          return gas_limit
     elif chain == 'GNO':
          gas_limit = data['result'][3]['gasLimit']
          return gas_limit
     elif chain == 'MATIC':
          gas_limit = data['result'][4]['gasLimit']
          return gas_limit
     elif chain == 'ERA':
          gas_limit = data['result'][6]['gasLimit']
          return gas_limit     
     elif chain == 'ZKEVM':
          gas_limit = data['result'][7]['gasLimit']
          return gas_limit    
     elif chain == 'ARB':
          gas_limit = data['result'][8]['gasLimit']
          return gas_limit    
     elif chain == 'AVAX':
          gas_limit = data['result'][9]['gasLimit']
          return gas_limit
     elif chain == 'AUR':
          gas_limit = data['result'][10]['gasLimit']
          return gas_limit
     elif chain == 'FTM':
          gas_limit = data['result'][5]['gasLimit']
          return gas_limit
def getMinSendAmount(parent_chain, destination_chain_id) -> float:
    try:
        # Check if the required keys exist in the JSON data
        if 'result' in data and isinstance(data['result'], list):
            for chain in data['result']:
                if 'name' in chain and chain['name'] == parent_chain:
                    parent_result = chain
                    break
            else:
                return None  # Parent chain not found
            
            if 'limits' in parent_result and isinstance(parent_result['limits'], list):
                for limit in parent_result['limits']:
                    if 'chainId' in limit and limit['chainId'] == destination_chain_id:
                        destination_limits = limit
                        break
                else:
                    return None  # Destination chain not found
                    
                if 'minAmount' in destination_limits:
                    min_amount = float(destination_limits['minAmount'])
                    return min_amount / 10**18
    except (KeyError, IndexError, ValueError):
        pass  # Handle the error gracefully, e.g., return a default value or raise an exception
    return None  # Return None if the values could not be retrieved


def getMaxSendAmount(parent_chain, destination_chain_id) -> float:
    try:
        # Check if the required keys exist in the JSON data
        if 'result' in data and isinstance(data['result'], list):
            for chain in data['result']:
                if 'name' in chain and chain['name'] == parent_chain:
                    parent_result = chain
                    break
            else:
                return None  # Parent chain not found
            
            if 'limits' in parent_result and isinstance(parent_result['limits'], list):
                for limit in parent_result['limits']:
                    if 'chainId' in limit and limit['chainId'] == destination_chain_id:
                        destination_limits = limit
                        break
                else:
                    return None  # Destination chain not found
                    
                if 'maxAmount' in destination_limits:
                    max_amount = float(destination_limits['maxAmount'])
                    return max_amount / 10**18
    except (KeyError, IndexError, ValueError):
        pass  # Handle the error gracefully, e.g., return a default value or raise an exception
    return None  # Return None if the values could not be retrieved

url = "https://refuel.socket.tech/chains"
output_file = "chains.json"  # File name to save the JSON data
re_download = False  # Set this flag to True if you want to re-download the JSON file

if re_download or not os.path.exists(output_file):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = json.loads(response.text)

        # Save the JSON data to a file
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"JSON data saved to {output_file} successfully.")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
else:
    print(f"Using existing file: {output_file}")

# Load the JSON data from the file
with open(output_file) as file:
    data = json.load(file)