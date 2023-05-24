# py-bungee-refueler
![py-bungee-refueler](https://github.com/whonion/py-bungee-refueler/blob/main/py-bungee-refueler.png?raw=true)
Batch send gas-token  with Socket

## Package description

- `main.py` - main module for execute;
- `config.py` - module containing the required imports, settings of minimum amounts to send, url-addresses of block explorers;
- `ABI/socket.json` - ABI of Socket GasMovr contract;
- `main_ru.py` - main module for execute(russian localization).

## Description of required files

- `accounts.txt` - private keys of wallets
- ~~`recipient_addresses.txt` - addresses of recipient (if you want to send to another address)~~
- `.env` - the file with your RPC variables and contract address of Socket GasMovr

_example of `.env`-file_

```sh
# https://docs.socket.tech/socket-api/contract-addresses

BUNGEE_ETH_ROUNER = '0xb584d4be1a5470ca1a8778e9b86c81e165204599'
BUNGEE_ARB_ROUNER = '0xc0e02aa55d10e38855e13b64a8e1387a04681a00'
BUNGEE_OPT_ROUTER = '0x5800249621da520adfdca16da20d8a5fc0f814d8'
BUNGEE_BSC_ROUTER = '0xBE51D38547992293c89CC589105784ab60b004A9'
BUNGEE_MATIC_ROUNER = '0xAC313d7491910516E06FBfC2A0b5BB49bb072D91'
BUNGEE_FTM_ROUNER = '0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB'
BUNGEE_AVAX_ROUNER = '0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB'

# Specify your own private RPCs
# Don't recommended to use a public node you'll get '429 Client Error: Too Many Requests for url'
RPC_ETH = 'https://rpc.ankr.com/eth/{YOUR_API_KEY}'
RPC_ARB = 'https://rpc.ankr.com/arbitrum/{YOUR_API_KEY}'
RPC_OPT = 'https://rpc.ankr.com/optimism/{YOUR_API_KEY}'
RPC_BSC = 'https://rpc.ankr.com/bsc/{YOUR_API_KEY}'
RPC_MATIC =  'https://rpc.ankr.com/polygon/{YOUR_API_KEY}'
RPC_FTM =  'https://rpc.ankr.com/fantom/{YOUR_API_KEY}'
RPC_AVAX = 'https://rpc.ankr.com/avalanche/{YOUR_API_KEY}'
```

## How run

- Install Python to your system;
- Activate the Python Virtual Environment (recommended);
- Install dependencies.

```sh
pip install -r requierements.txt
```

- Add your private keys to the `accounts.txt` file;
- Add your RPCs to the `.env' file;
- Add recipient addresses to `recipient_addresses.txt` for receive in the target network's native token on another address;<br/>
- Run `main.py` and follow the script prompts.

_for Windows_

```sh
python .\main.py
```

_for Linux_

```sh
python3 ./main.py
```
