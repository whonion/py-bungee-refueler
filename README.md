# py-bungee-refueler
Batch send gas-token  with Socket<br>

`main.py` preview<br>

![py-bungee-refueler](https://github.com/whonion/py-bungee-refueler/blob/main/py-bungee-refueler.png?raw=true)

`main_ru.py` preview<br>

![py-bungee-refueler-ru](https://github.com/whonion/py-bungee-refueler/blob/main/py-bungee-refueler-ru.png?raw=true)

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
BUNGEE_OPT_ROUTER = '0x5800249621da520adfdca16da20d8a5fc0f814d8'
BUNGEE_BSC_ROUTER = '0xBE51D38547992293c89CC589105784ab60b004A9'
BUNGEE_GNO_ROUNER = '0xBE51D38547992293c89CC589105784ab60b004A9'
BUNGEE_MATIC_ROUNER = '0xAC313d7491910516E06FBfC2A0b5BB49bb072D91'
BUNGEE_ERA_ROUNER = '0xaDdE7028e7ec226777e5dea5D53F6457C21ec7D6'
BUNGEE_ZKEVM_ROUNER = '0x3a23F943181408EAC424116Af7b7790c94Cb97a5'
BUNGEE_ARB_ROUNER = '0xc0e02aa55d10e38855e13b64a8e1387a04681a00'
BUNGEE_AVAX_ROUNER = '0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB'
BUNGEE_AUR_ROUNER = '0x2b42AFFD4b7C14d9B7C2579229495c052672Ccd3'
BUNGEE_FTM_ROUNER = '0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB'

#Specify your `API_KEY`` if you use Anr or change RPC's constants and specify your own private RPCs
API_KEY = 'API_KEY' 

# Don't recommended to use a public node if you've many wallets else you'll get '429 Client Error: Too Many Requests for url'
RPC_ETH = f"https://rpc.ankr.com/eth/"+API_KEY
RPC_ARB = f'https://rpc.ankr.com/arbitrum/'+API_KEY
RPC_OPT = f'https://rpc.ankr.com/optimism/'+API_KEY
RPC_BSC = f'https://rpc.ankr.com/bsc/'+API_KEY
RPC_MATIC =  f'https://rpc.ankr.com/polygon/'+API_KEY
RPC_FTM =  f'https://rpc.ankr.com/fantom/'+API_KEY
RPC_AVAX = f'https://rpc.ankr.com/avalanche/'+API_KEY
RPC_GNO = f'https://rpc.ankr.com/gnosis/'+API_KEY
RPC_AUR = f'https://endpoints.omniatech.io/v1/aurora/mainnet/public'
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
