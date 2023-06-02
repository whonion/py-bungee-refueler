# py-bungee-refueler
[![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/whonion/py-bungee-refueler/blob/main/) [![Test Run](https://github.com/whonion/py-bungee-refueler/actions/workflows/test.yml/badge.svg)](https://github.com/whonion/py-bungee-refueler/actions/workflows/test.yml) [![Python version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3111/) [![Web3.py version](https://img.shields.io/badge/Web3.py-6.0.0-blue.svg)](https://pypi.org/project/web3/6.0.0/) <br>
Мультисендер газа через [bungee.exchange](https://bungee.exchange) (Powered by Socket)<br>

`main.py` предпросмотр<br>

![py-bungee-refueler](https://github.com/whonion/py-bungee-refueler/blob/main/py-bungee-refueler.png?raw=true)

`main_ru.py` предпросмотр<br>

![py-bungee-refueler-ru](https://github.com/whonion/py-bungee-refueler/blob/main/py-bungee-refueler-ru.png?raw=true)

## Описание проекта

- `main.py` - основной скрипт для запуска;
- `main_ru.py` - основной скрипт для запуска(русская локализация);
- `refuel.py` - модуль для получения актуальных данных о EVM-сетях (минимальная/максимальная сумма отправки, доступность сети);
- `chains.json` - отформатированный json-файл полученный из `https://refuel.socket.tech/chains` (обновляется при отсутствии в рабочей дирректории);
- `config.py` - модуль, содержащий требуемые импорты настройки минимальной/максимальной суммы отправки газа, url-адреса обозревателей блоков;
- `ABI/socket.json` - ABI-файл для взаимодействия с контрактами Socket Refuel.


## Описание необходимых файлов для работы скрипта

- `accounts.txt` - приватные ключи от кошельков (каждый с новой строки)
- ~~`recipient_addresses.txt` - адреса получателей (если вы хотите отправить на другой адрес) (реализация удалена)~~
- `.env` - файл, хранящий переменные для работы такие как адреса контрактов Socket Refuel, ваши частные RPC для EVM-сетей

_пример `.env`-файла_

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

# Необходимо указать `API_KEY` если вы используете например Ankr, либо ваши собственные узлы
# Не рекомендуется использовать публичные ноды если у вас много кошельков, так как вы можете столкнуться с ошибкой '429 Client Error: Too Many Requests for url'

RPC_ETH = 'https://rpc.ankr.com/eth/API_KEY'
RPC_ARB = 'https://rpc.ankr.com/arbitrum/API_KEY'
RPC_OPT = 'https://rpc.ankr.com/optimism/API_KEY'
RPC_BSC = 'https://rpc.ankr.com/bsc/API_KEY'
RPC_MATIC =  'https://rpc.ankr.com/polygon/API_KEY'
RPC_FTM =  'https://rpc.ankr.com/fantom/API_KEY'
RPC_AVAX = 'https://rpc.ankr.com/avalanche/API_KEY'
RPC_GNO = 'https://rpc.ankr.com/gnosis/API_KEY'
RPC_AUR = 'https://endpoints.omniatech.io/v1/aurora/mainnet/public'
```

## Запуск скрипта

- Установите Python в вашу систему;
- Активируйте виртуальное окружения Python (рекомендуется);
```sh
#Для Windows
 python -m venv .venv
 .\.venv\Scripts\activate
# Для Linux 
 source .venv/bin/activate
```
- Установите зависимости для проекта.

```sh
pip install -r requierements.txt
```

- Укажите приватные ключи от кошельков в файл `accounts.txt`;
- Укажите адреса ваших RPC в файле `.env`;
- ~~Добавьте адреса получателей в файл `recipient_addresses.txt` для получения нативного токена сети на другой адрес (реализация удалена);<br/>~~
- Запустите `main.py` и следуйте подсказкам на экране.

_для Windows_

```sh
python .\main.py
```

_для Linux_

```sh
python3 ./main.py
```
