from refuel import *
from web3 import Web3
from web3.contract import Contract
from web3.middleware import geth_poa_middleware
from loguru import logger
from sys import stderr
from multiprocessing.dummy import Pool
from dotenv import load_dotenv

load_dotenv()
BUNGEE_ETH_ROUNER = os.getenv('BUNGEE_ETH_ROUNER')
BUNGEE_OPT_ROUTER = os.getenv('BUNGEE_OPT_ROUTER')
BUNGEE_BSC_ROUTER = os.getenv('BUNGEE_BSC_ROUTER')
BUNGEE_GNO_ROUTER = os.getenv('BUNGEE_GNO_ROUTER')
BUNGEE_MATIC_ROUNER = os.getenv('BUNGEE_MATIC_ROUNER')
BUNGEE_ERA_ROUNER = os.getenv('BUNGEE_ERA_ROUNER')
BUNGEE_ZKEVM_ROUNER = os.getenv('BUNGEE_ZKEVM_ROUNER')
BUNGEE_ARB_ROUNER = os.getenv('BUNGEE_ARB_ROUNER')
BUNGEE_AVAX_ROUNER = os.getenv('BUNGEE_AVAX_ROUNER')
BUNGEE_AUR_ROUNER = os.getenv('BUNGEE_AUR_ROUNER')
BUNGEE_FTM_ROUNER = os.getenv('BUNGEE_FTM_ROUNER')


RPC_ETH = os.getenv('RPC_ETH')
RPC_OPT = os.getenv('RPC_OPT')
RPC_BSC = os.getenv('RPC_BSC')
RPC_GNO =  os.getenv('RPC_GNO')
RPC_MATIC =  os.getenv('RPC_MATIC')
RPC_ERA =  os.getenv('RPC_ERA')
RPC_ZKEVM =  os.getenv('RPC_ZKEVM')
RPC_ARB = os.getenv('RPC_ARB')
RPC_AVAX =  os.getenv('RPC_AVAX')
RPC_AUR =  os.getenv('RPC_AUR')
RPC_FTM =  os.getenv('RPC_FTM')

EXP_ETH = 'https://etherscan.io/'
EXP_OPT = 'https://optimistic.etherscan.io/'
EXP_BSC = 'https://bscscan.com/'
EXP_GNO = 'https://gnosisscan.io/'
EXP_MATIC = 'https://polygonscan.com/'
EXP_ERA = 'https://explorer.zksync.io/'
EXP_ZKEVM = 'https://zkevm.polygonscan.com/'
EXP_ARB = 'https://arbiscan.io/'
EXP_AVAX = 'https://snowtrace.io/'
EXP_AUR = 'https://mainnet.aurora.dev/'
EXP_FTM = 'https://ftmscan.com/'

# Minimum amounts from ETH
min_eth_to_arb = getMinSendAmount('Ethereum', 42161)
min_eth_to_opt = getMinSendAmount('Ethereum', 10)
min_eth_to_bsc = getMinSendAmount('Ethereum', 56)
min_eth_to_matic = getMinSendAmount('Ethereum', 137)
min_eth_to_era = getMinSendAmount('Ethereum', 324)
min_eth_to_zkevm = getMinSendAmount('Ethereum', 1101)
min_eth_to_avax = getMinSendAmount('Ethereum', 43114)
min_eth_to_aur = getMinSendAmount('Ethereum', 1313161554)
min_eth_to_gno = getMinSendAmount('Ethereum', 100)

# Maximum amounts from ETH
max_eth_to_arb = getMaxSendAmount('Ethereum', 42161)
max_eth_to_opt = getMaxSendAmount('Ethereum', 10)
max_eth_to_bsc = getMaxSendAmount('Ethereum', 56)
max_eth_to_matic = getMaxSendAmount('Ethereum', 137)
max_eth_to_era = getMaxSendAmount('Ethereum', 324)
max_eth_to_zkevm = getMaxSendAmount('Ethereum', 1101)
max_eth_to_avax = getMaxSendAmount('Ethereum', 43114)
max_eth_to_aur = getMaxSendAmount('Ethereum', 1313161554)
max_eth_to_gno = getMaxSendAmount('Ethereum', 100)

# Minimum amount from OPT
min_opt_to_arb = getMinSendAmount('Optimism', 42161)
min_opt_to_bsc = getMinSendAmount('Optimism', 56)
min_opt_to_gno = getMinSendAmount('Optimism', 100)
min_opt_to_matic = getMinSendAmount('Optimism', 137)
min_opt_to_era = getMinSendAmount('Optimism', 324)
min_opt_to_zkevm = getMinSendAmount('Optimism', 1101)
min_opt_to_avax = getMinSendAmount('Optimism', 43114)
min_opt_to_aur = getMinSendAmount('Optimism', 1313161554)

# Maximum amounts from OPT
max_opt_to_arb = getMaxSendAmount('Optimism', 42161)
max_opt_to_bsc = getMaxSendAmount('Optimism', 56)
max_opt_to_gno = getMaxSendAmount('Optimism', 100)
max_opt_to_matic = getMaxSendAmount('Optimism', 137)
max_opt_to_era = getMaxSendAmount('Optimism', 324)
max_opt_to_zkevm = getMaxSendAmount('Optimism', 1101)
max_opt_to_avax = getMaxSendAmount('Optimism', 43114)
max_opt_to_aur = getMaxSendAmount('Optimism', 1313161554)

# Minimum amounts from BSC
min_bsc_to_arb = getMinSendAmount('BSC', 42161)
min_bsc_to_opt = getMinSendAmount('BSC', 10)
min_bsc_to_gno = getMinSendAmount('BSC', 100)
min_bsc_to_matic = getMinSendAmount('BSC', 137)
min_bsc_to_era = getMinSendAmount('BSC', 324)
min_bsc_to_zkevm = getMinSendAmount('BSC', 1101)
min_bsc_to_avax = getMinSendAmount('BSC', 43114)
min_bsc_to_aur = getMinSendAmount('BSC', 1313161554)

# Minimum amounts from BSC
max_bsc_to_arb = getMaxSendAmount('BSC', 42161)
max_bsc_to_opt = getMaxSendAmount('BSC', 10)
max_bsc_to_gno = getMaxSendAmount('BSC', 100)
max_bsc_to_matic = getMaxSendAmount('BSC', 137)
max_bsc_to_era = getMaxSendAmount('BSC', 324)
max_bsc_to_zkevm = getMaxSendAmount('BSC', 1101)
max_bsc_to_avax = getMaxSendAmount('BSC', 43114)
max_bsc_to_aur = getMaxSendAmount('BSC', 1313161554)

# Min Amounts from Gnosis
min_gno_to_arb = getMinSendAmount('Gnosis', 42161)
min_gno_to_avax = getMinSendAmount('Gnosis', 43114)
min_gno_to_aur = getMinSendAmount('Gnosis', 1313161554)
min_gno_to_opt = getMinSendAmount('Gnosis', 10)
min_gno_to_bsc = getMinSendAmount('Gnosis', 56)
min_gno_to_matic = getMinSendAmount('Gnosis', 137)
min_gno_to_era = getMinSendAmount('Gnosis', 324)
min_gno_to_zkevm = getMinSendAmount('Gnosis', 1101)

# Max Amounts from Gnosis
max_gno_to_arb = getMinSendAmount('Gnosis', 42161)
max_gno_to_avax = getMinSendAmount('Gnosis', 43114)
max_gno_to_aur = getMinSendAmount('Gnosis', 1313161554)
max_gno_to_opt = getMinSendAmount('Gnosis', 10)
max_gno_to_bsc = getMinSendAmount('Gnosis', 56)
max_gno_to_matic = getMinSendAmount('Gnosis', 137)
max_gno_to_era = getMinSendAmount('Gnosis', 324)
max_gno_to_zkevm = getMinSendAmount('Gnosis', 1101)

# Min Amounts from MATIC
min_matic_to_arb = getMinSendAmount('Polygon', 42161)
min_matic_to_opt = getMinSendAmount('Polygon', 10)
min_matic_to_bsc = getMinSendAmount('Polygon', 56)
min_matic_to_gno = getMinSendAmount('Polygon', 100)
min_matic_to_era = getMinSendAmount('Polygon', 324)
min_matic_to_zkevm = getMinSendAmount('Polygon', 1101)
min_matic_to_avax = getMinSendAmount('Polygon', 43114)
min_matic_to_aur = getMinSendAmount('Polygon', 1313161554)

# Max Amounts from MATIC
max_matic_to_arb = getMaxSendAmount('Polygon', 42161)
max_matic_to_opt = getMaxSendAmount('Polygon', 10)
max_matic_to_bsc = getMaxSendAmount('Polygon', 56)
max_matic_to_gno = getMaxSendAmount('Polygon', 100)
max_matic_to_era = getMaxSendAmount('Polygon', 324)
max_matic_to_zkevm = getMaxSendAmount('Polygon', 1101)
max_matic_to_avax = getMaxSendAmount('Polygon', 43114)
max_matic_to_aur = getMaxSendAmount('Polygon', 1313161554)

# Min Amounts from Era
min_era_to_arb = getMinSendAmount('zkSync', 42161)
min_era_to_opt = getMinSendAmount('zkSync', 10)
min_era_to_bsc = getMinSendAmount('zkSync', 56)
min_era_to_gno = getMinSendAmount('zkSync', 100)
min_era_to_matic = getMinSendAmount('zkSync', 137)
min_era_to_zkevm = getMinSendAmount('zkSync', 1101)
min_era_to_avax = getMinSendAmount('zkSync', 43114)
min_era_to_aur = getMinSendAmount('zkSync', 1313161554)

# Max Amounts from Era
max_era_to_arb = getMaxSendAmount('zkSync', 42161)
max_era_to_opt = getMaxSendAmount('zkSync', 10)
max_era_to_bsc = getMaxSendAmount('zkSync', 56)
max_era_to_gno = getMaxSendAmount('zkSync', 100)
max_era_to_matic = getMaxSendAmount('zkSync', 137)
max_era_to_zkevm = getMaxSendAmount('zkSync', 1101)
max_era_to_avax = getMaxSendAmount('zkSync', 43114)
max_era_to_aur = getMaxSendAmount('zkSync', 1313161554)

# Min Amounts from zkEVM
min_zkevm_to_arb = getMinSendAmount('zkEVM', 42161)
min_zkevm_to_opt = getMinSendAmount('zkEVM', 10)
min_zkevm_to_bsc = getMinSendAmount('zkEVM', 56)
min_zkevm_to_gno = getMinSendAmount('zkEVM', 100)
min_zkevm_to_matic = getMinSendAmount('zkEVM', 137)
min_zkevm_to_era = getMinSendAmount('zkEVM', 324)
min_zkevm_to_avax = getMinSendAmount('zkEVM', 43114)
min_zkevm_to_aur = getMinSendAmount('zkEVM', 1313161554)

# Max Amounts from zkEVM
max_zkevm_to_arb = getMaxSendAmount('zkEVM', 42161)
max_zkevm_to_opt = getMaxSendAmount('zkEVM', 10)
max_zkevm_to_bsc = getMaxSendAmount('zkEVM', 56)
max_zkevm_to_gno = getMaxSendAmount('zkEVM', 100)
max_zkevm_to_matic = getMaxSendAmount('zkEVM', 137)
max_zkevm_to_era = getMaxSendAmount('zkEVM', 324)
max_zkevm_to_avax = getMaxSendAmount('zkEVM', 43114)
max_zkevm_to_aur = getMaxSendAmount('zkEVM', 1313161554)

# Min Amounts from Arbitrum
min_arb_to_zkevm = getMinSendAmount('Arbitrum', 1101)
min_arb_to_opt = getMinSendAmount('Arbitrum', 10)
min_arb_to_bsc = getMinSendAmount('Arbitrum', 56)
min_arb_to_gno = getMinSendAmount('Arbitrum', 100)
min_arb_to_matic = getMinSendAmount('Arbitrum', 137)
min_arb_to_era = getMinSendAmount('Arbitrum', 324)
min_arb_to_avax = getMinSendAmount('Arbitrum', 43114)
min_arb_to_aur = getMinSendAmount('Arbitrum', 1313161554)

# Max Amounts from Arbitrum
max_arb_to_zkevm = getMaxSendAmount('Arbitrum', 1101)
max_arb_to_opt = getMaxSendAmount('Arbitrum', 10)
max_arb_to_bsc = getMaxSendAmount('Arbitrum', 56)
max_arb_to_gno = getMaxSendAmount('Arbitrum', 100)
max_arb_to_matic = getMaxSendAmount('Arbitrum', 137)
max_arb_to_era = getMaxSendAmount('Arbitrum', 324)
max_arb_to_avax = getMaxSendAmount('Arbitrum', 43114)
max_arb_to_aur = getMaxSendAmount('Arbitrum', 1313161554)

# Min Amounts from Avalanche
min_avax_to_zkevm = getMinSendAmount('Avalanche', 1101)
min_avax_to_opt = getMinSendAmount('Avalanche', 10)
min_avax_to_bsc = getMinSendAmount('Avalanche', 56)
min_avax_to_gno = getMinSendAmount('Avalanche', 100)
min_avax_to_matic = getMinSendAmount('Avalanche', 137)
min_avax_to_era = getMinSendAmount('Avalanche', 324)
min_avax_to_arb = getMinSendAmount('Avalanche', 42161)
min_avax_to_aur = getMinSendAmount('Avalanche', 1313161554)

# Max Amounts from Avalanche
max_avax_to_zkevm = getMaxSendAmount('Avalanche', 1101)
max_avax_to_opt = getMaxSendAmount('Avalanche', 10)
max_avax_to_bsc = getMaxSendAmount('Avalanche', 56)
max_avax_to_gno = getMaxSendAmount('Avalanche', 100)
max_avax_to_matic = getMaxSendAmount('Avalanche', 137)
max_avax_to_era = getMaxSendAmount('Avalanche', 324)
max_avax_to_arb = getMaxSendAmount('Avalanche', 42161)
max_avax_to_aur = getMaxSendAmount('Avalanche', 1313161554)

# Min Amounts from Aurora
min_aur_to_zkevm = getMinSendAmount('Aurora', 1101)
min_aur_to_opt = getMinSendAmount('Aurora', 10)
min_aur_to_bsc = getMinSendAmount('Aurora', 56)
min_aur_to_gno = getMinSendAmount('Aurora', 100)
min_aur_to_matic = getMinSendAmount('Aurora', 137)
min_aur_to_era = getMinSendAmount('Aurora', 324)
min_aur_to_arb = getMinSendAmount('Aurora', 42161)
min_aur_to_avax = getMinSendAmount('Aurora', 43114)

# Max Amounts from Aurora
max_aur_to_zkevm = getMaxSendAmount('Aurora', 1101)
max_aur_to_opt = getMaxSendAmount('Aurora', 10)
max_aur_to_bsc = getMaxSendAmount('Aurora', 56)
max_aur_to_gno = getMaxSendAmount('Aurora', 100)
max_aur_to_matic = getMaxSendAmount('Aurora', 137)
max_aur_to_era = getMaxSendAmount('Aurora', 324)
max_aur_to_arb = getMaxSendAmount('Aurora', 42161)
max_aur_to_avax = getMaxSendAmount('Aurora', 43114)

# Min Amounts from Fantom
min_ftm_to_opt = getMinSendAmount('Fantom', 10)
min_ftm_to_bsc = getMinSendAmount('Fantom', 56)
min_ftm_to_gno = getMinSendAmount('Fantom', 100)
min_ftm_to_matic = getMinSendAmount('Fantom', 137)
min_ftm_to_era = getMinSendAmount('Fantom', 324)
min_ftm_to_zkevm = getMinSendAmount('Fantom', 1101)
min_ftm_to_arb = getMinSendAmount('Fantom', 42161)
min_ftm_to_avax = getMinSendAmount('Fantom', 43114)
min_ftm_to_aur = getMinSendAmount('Fantom', 1313161554)

# Max Amounts from Fantom
max_ftm_to_opt = getMaxSendAmount('Fantom', 10)
max_ftm_to_bsc = getMaxSendAmount('Fantom', 56)
max_ftm_to_gno = getMaxSendAmount('Fantom', 100)
max_ftm_to_matic = getMaxSendAmount('Fantom', 137)
max_ftm_to_era = getMaxSendAmount('Fantom', 324)
max_ftm_to_zkevm = getMaxSendAmount('Fantom', 1101)
max_ftm_to_arb = getMaxSendAmount('Fantom', 42161)
max_ftm_to_avax = getMaxSendAmount('Fantom', 43114)
max_ftm_to_aur = getMaxSendAmount('Fantom', 1313161554)

# Min Amounts to Fantom
min_eth_to_ftm = getMinSendAmount('Ethereum', 250)
min_opt_to_ftm = getMinSendAmount('Optimism', 250)
min_bsc_to_ftm = getMinSendAmount('BSC', 250)
min_matic_to_ftm = getMinSendAmount('Polygon', 250)
min_era_to_ftm = getMinSendAmount('zkSync', 250)
min_zkevm_to_ftm = getMinSendAmount('zkEVM', 250)
min_arb_to_ftm = getMinSendAmount('Arbitrum', 250)
min_avax_to_ftm = getMinSendAmount('Avalanche', 250)
min_aur_to_ftm = getMinSendAmount('Aurora', 250)
min_gno_to_ftm = getMinSendAmount('Gnosis', 250)

# Max mounts to Fantom
max_eth_to_ftm = getMaxSendAmount('Ethereum', 250)
max_opt_to_ftm = getMaxSendAmount('Optimism', 250)
max_bsc_to_ftm = getMaxSendAmount('BSC', 250)
max_matic_to_ftm = getMaxSendAmount('Polygon', 250)
max_era_to_ftm = getMaxSendAmount('zkSync', 250)
max_zkevm_to_ftm = getMaxSendAmount('zkEVM', 250)
max_arb_to_ftm = getMaxSendAmount('Arbitrum', 250)
max_avax_to_ftm = getMaxSendAmount('Avalanche', 250)
max_aur_to_ftm = getMaxSendAmount('Aurora', 250)
max_gno_to_ftm = getMaxSendAmount('Gnosis', 250)