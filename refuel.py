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
          gas_limit = data['result'][5]['gasLimit']
          return gas_limit     
     elif chain == 'ZKEVM':
          gas_limit = data['result'][6]['gasLimit']
          return gas_limit    
     elif chain == 'ARB':
          gas_limit = data['result'][7]['gasLimit']
          return gas_limit    
     elif chain == 'AVAX':
          gas_limit = data['result'][8]['gasLimit']
          return gas_limit
     elif chain == 'AUR':
          gas_limit = data['result'][9]['gasLimit']
          return gas_limit
    #  elif chain == 'FTM':
    #       gas_limit = data['result'][nil]['gasLimit']
    #       return gas_limit
      
def getMinSendAmount(parent_chainId,destination_chainId) -> float:
    # Get the value of 'minAmount'
    min_amount = float(data['result'][parent_chainId]['limits'][destination_chainId]['minAmount'])
    min_amount = min_amount / 10**18
    #print(f"Minimum Amount: {min_amount}")
    return min_amount

def getMaxSendAmount(parent_chainId,destination_chainId) -> float:
    # Get the value of 'maxAmount'
    max_amount = float(data['result'][parent_chainId]['limits'][destination_chainId]['maxAmount'])
    max_amount = max_amount / 10**18
    #print(f"Maximum Amount: {max_amount}")
    return max_amount

url = "https://refuel.socket.tech/chains"
output_file = "chains.json"  # File name to save the JSON data

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

file_path = "chains.json"  # Path to the JSON file

# Load the JSON data from the file
with open(file_path) as file:
    data = json.load(file)