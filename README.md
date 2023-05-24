# py-bungee-refueler

Batch send gas-token  with Socket

## Package description

- `main.py` - main module for execute;
- `config.py` - module containing the required imports, settings of minimum amounts to send, url-addresses of block explorers;
- `main_ru.py` - main module for execute(russian localization).

## Description of required files

- `accounts.txt` - private keys of wallets
- `recipient_addresses.txt` - addresses of recipient (if you want to send to another address)
- `.env` - the file with your RPC variables and contract address of Socket GasMovr

_example of `.env`-file_

```sh
# https://docs.socket.tech/socket-api/contract-addresses

BUNGEE_ETH_ROUNER = '0xb584d4be1a5470ca1a8778e9b86c81e165204599'
BUNGEE_ARB_ROUNER = '0xc0e02aa55d10e38855e13b64a8e1387a04681a00'
BUNGEE_OPT_ROUTER = '0x5800249621da520adfdca16da20d8a5fc0f814d8'
BUNGEE_BSC_ROUTER = '0xc30141B657f4216252dc59Af2e7CdB9D8792e1B0'
BUNGEE_MATIC_ROUNER = '0xAC313d7491910516E06FBfC2A0b5BB49bb072D91'
BUNGEE_FTM_ROUNER = '0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB'
BUNGEE_AVAX_ROUNER = '0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB'

# Specify your own RPCs or use a public one, as in the example
RPC_ETH = 'https://mainnet.infura.io/v3/{YOUR_API_KEY}' #1
RPC_ARB = 'https://arb-mainnet.g.alchemy.com/v2/{YOUR_API_KEY}' #42161
RPC_OPT = 'https://opt-mainnet.g.alchemy.com/v2/{YOUR_API_KEY}' #10
RPC_BSC = 'https://bsc-dataseed.binance.org' #56
RPC_MATIC =  'https://polygon.llamarpc.com' #137
RPC_FTM =  'https://fantom.publicnode.com' #250
RPC_AVAX = 'https://avalanche-c-chain.publicnode.com' #43114
```

## How run

- Install Python to your system
- Install dependencies

```sh
pip install -r requierements.txt
```

- Add your private keys to the `accounts.txt` file
- Add your RPCs to the `.env' file
- Add recipient addresses to `recipient_addresses.txt` for receive in the target network's native token on another address   <br/>
- Run `main.py` nd follow the script prompts

```sh
python .\main.py
```

_for Linux_

```sh
python3 ./main.py
```

```
