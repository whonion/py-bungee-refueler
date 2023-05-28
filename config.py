from refuel import *
import os
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

# Min Amounts from ETH
min_eth_to_arb = getMinSendAmount(0,6)
min_eth_to_opt = getMinSendAmount(0,0)
min_eth_to_bsc = getMinSendAmount(0,1)
min_eth_to_matic = getMinSendAmount(0,3)
min_eth_to_ftm = 0.00044
min_eth_to_avax = getMinSendAmount(0,7)

# Max Amounts from ETH
max_eth_to_arb = getMaxSendAmount(0,6)
max_eth_to_opt = getMaxSendAmount(0,0)
max_eth_to_bsc = getMaxSendAmount(0,1)
max_eth_to_matic = getMaxSendAmount(0,3)
max_eth_to_ftm = 0.017
max_eth_to_avax = getMaxSendAmount(0,7)

# Min Amounts from OPT
#min_opt_to_eth = ''
min_opt_to_arb = getMinSendAmount(1,6)
min_opt_to_bsc = getMinSendAmount(1,0)
min_opt_to_matic = getMinSendAmount(1,3)
min_opt_to_ftm = 0.00059
min_opt_to_avax = getMinSendAmount(1,7)

# Max Amounts from OPT
max_opt_to_arb = getMaxSendAmount(1,6)
max_opt_to_bsc = getMaxSendAmount(1,0)
max_opt_to_matic = getMaxSendAmount(1,3)
max_opt_to_ftm = 0.017
max_opt_to_avax = getMaxSendAmount(1,7)

# Min Amounts from BSC
#min_bsc_to_eth = ''
min_bsc_to_arb = getMinSendAmount(2,5)
min_bsc_to_opt = getMinSendAmount(2,0)
min_bsc_to_matic = getMinSendAmount(2,2)
min_bsc_to_ftm = 0.0035
min_bsc_to_avax = getMinSendAmount(2,6)

# Max Amounts from BSC
max_bsc_to_arb = getMaxSendAmount(2,5)
max_bsc_to_opt = getMaxSendAmount(2,0)
max_bsc_to_matic = getMaxSendAmount(2,2)
max_bsc_to_ftm = 0.1
max_bsc_to_avax = getMaxSendAmount(2,6)

# Min Amounts from Gnosis
min_gno_to_arb = getMinSendAmount(8,6)
min_gno_to_opt = getMinSendAmount(8,0)
min_gno_to_bsc = getMinSendAmount(8,1)
min_gno_to_matic = getMinSendAmount(8,3)
min_gno_to_ftm = 0.0

# Max Amounts from Gnosis
max_gno_to_arb = getMinSendAmount(8,6)
max_gno_to_opt = getMinSendAmount(8,0)
max_gno_to_bsc = getMinSendAmount(8,1)
max_gno_to_matic = getMinSendAmount(8,3)
max_gno_to_ftm = 0.0

# Min Amounts from MATIC
#min_matic_to_eth = ''
min_matic_to_arb = getMinSendAmount(4,5)
min_matic_to_opt = getMinSendAmount(4,0)
min_matic_to_bsc = getMinSendAmount(4,1)
min_matic_to_ftm = 1.23
min_matic_avax = getMinSendAmount(4,6)

# Max Amounts from MATIC
max_matic_to_arb = getMaxSendAmount(4,5)
max_matic_to_opt = getMaxSendAmount(4,0)
max_matic_to_bsc = getMaxSendAmount(4,1)
max_matic_to_ftm = 37.71
max_matic_to_avax = getMaxSendAmount(4,6)

# Min Amounts from ARB
#min_arb_to_eth = ''
min_arb_to_opt = getMinSendAmount(7,0)
min_arb_to_bsc = getMinSendAmount(7,1)
min_arb_to_matic = getMinSendAmount(7,3)
min_arb_to_ftm = 0.00059
min_arb_to_avax = getMinSendAmount(7,6)

# Max Amounts from ARB
max_arb_to_opt = getMaxSendAmount(7,0)
max_arb_to_bsc = getMaxSendAmount(7,1)
max_arb_to_matic = getMaxSendAmount(7,3)
max_arb_to_ftm = 0.017
max_arb_to_avax = getMaxSendAmount(7,6)

# Min Amounts from AVAX
min_avax_to_arb = getMinSendAmount(8,6)
min_avax_to_opt = getMinSendAmount(8,0)
min_avax_to_bsc = getMinSendAmount(8,1)
min_avax_to_matic = getMinSendAmount(8,3)
min_avax_to_ftm = 0.055

# Max Amounts from AVAX
max_avax_to_arb = getMaxSendAmount(8,6)
max_avax_to_opt = getMaxSendAmount(8,0)
max_avax_to_bsc = getMaxSendAmount(8,1)
max_avax_to_matic = getMaxSendAmount(8,3)
max_avax_to_ftm = 2.22

# Min Amounts from Aurora
max_aur_to_arb = getMinSendAmount(8,6)
max_aur_to_opt = getMinSendAmount(8,0)
max_aur_to_bsc = getMinSendAmount(8,1)
max_aur_to_matic = getMinSendAmount(8,3)
max_aur_to_ftm = 0.0

# Max Amounts from Aurora
max_aur_to_arb = getMinSendAmount(8,6)
max_aur_to_opt = getMinSendAmount(8,0)
max_aur_to_bsc = getMinSendAmount(8,1)
max_aur_to_matic = getMinSendAmount(8,3)
max_aur_to_ftm = 0.0

# Min Amounts from FTM
min_ftm_to_arb = 21.09
min_ftm_to_opt = 30.29
min_ftm_to_bsc = 2.23
min_ftm_to_matic = 0.7
min_ftm_to_avax = 1.84

# Max Amounts from FTM
max_ftm_to_arb = 84.34
max_ftm_to_opt = 140.81
max_ftm_to_bsc = 17.8
max_ftm_to_matic = 48.31
max_ftm_to_avax = 45.93






