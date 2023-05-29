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
min_eth_to_era = getMinSendAmount(0,4)
min_eth_to_zkevm = getMinSendAmount(0,5)
min_eth_to_avax = getMinSendAmount(0,7)
min_eth_to_aur = getMinSendAmount(0,8)
min_eth_to_gno  = getMinSendAmount(0,2)

# Max Amounts from ETH
max_eth_to_arb = getMaxSendAmount(0,6)
max_eth_to_opt = getMaxSendAmount(0,0)
max_eth_to_bsc = getMaxSendAmount(0,1)
max_eth_to_matic = getMaxSendAmount(0,3)
max_eth_to_era = getMaxSendAmount(0,4)
max_eth_to_zkevm = getMaxSendAmount(0,5)
max_eth_to_avax = getMaxSendAmount(0,7)
max_eth_to_aur = getMaxSendAmount(0,8)
max_eth_to_gno  = getMaxSendAmount(0,2)

# Min Amounts from OPT
#min_opt_to_eth = ''
min_opt_to_arb = getMinSendAmount(1,5)
min_opt_to_bsc = getMinSendAmount(1,0)
min_opt_to_gno = getMinSendAmount(1,1)
min_opt_to_matic = getMinSendAmount(1,2)
min_opt_to_era = getMinSendAmount(1,3)
min_opt_to_zkevm = getMinSendAmount(1,4)
min_opt_to_avax = getMinSendAmount(1,6)
min_opt_to_aur = getMinSendAmount(1,7)

# Max Amounts from OPT
max_opt_to_arb = getMaxSendAmount(1,5)
max_opt_to_bsc = getMaxSendAmount(1,0)
max_opt_to_gno = getMaxSendAmount(1,1)
max_opt_to_matic = getMaxSendAmount(1,2)
max_opt_to_era = getMaxSendAmount(1,3)
max_opt_to_zkevm = getMaxSendAmount(1,4)
max_opt_to_avax = getMaxSendAmount(1,6)
max_opt_to_aur = getMaxSendAmount(1,7)

# Min Amounts from BSC
#min_bsc_to_eth = ''
min_bsc_to_arb = getMinSendAmount(2,5)
min_bsc_to_opt = getMinSendAmount(2,0)
min_bsc_to_gno = getMinSendAmount(2,1)
min_bsc_to_matic = getMinSendAmount(2,2)
min_bsc_to_era = getMinSendAmount(2,3)
min_bsc_to_zkevm = getMinSendAmount(2,4)
min_bsc_to_avax = getMinSendAmount(2,6)
min_bsc_to_aur = getMinSendAmount(2,7)

# Max Amounts from BSC
max_bsc_to_arb = getMaxSendAmount(2,5)
max_bsc_to_opt = getMaxSendAmount(2,0)
max_bsc_to_gno = getMaxSendAmount(2,1)
max_bsc_to_matic = getMaxSendAmount(2,2)
max_bsc_to_era = getMaxSendAmount(2,3)
max_bsc_to_zkevm = getMaxSendAmount(2,4)
max_bsc_to_avax = getMaxSendAmount(2,6)
max_bsc_to_aur = getMaxSendAmount(2,7)

# Min Amounts from Gnosis
min_gno_to_arb = getMinSendAmount(3,5)
min_gno_to_avax = getMinSendAmount(3,6)
min_gno_to_aur = getMinSendAmount(3,7)
min_gno_to_opt = getMinSendAmount(3,0)
min_gno_to_bsc = getMinSendAmount(3,1)
min_gno_to_matic = getMinSendAmount(3,2)
min_gno_to_era = getMinSendAmount(3,3)
min_gno_to_zkevm = getMinSendAmount(3,4)

# Max Amounts from Gnosis
max_gno_to_arb = getMinSendAmount(3,5)
max_gno_to_avax = getMinSendAmount(3,6)
max_gno_to_aur  = getMinSendAmount(3,7)
max_gno_to_opt = getMinSendAmount(3,0)
max_gno_to_bsc = getMinSendAmount(3,1)
max_gno_to_matic = getMinSendAmount(3,2)
max_gno_to_era = getMinSendAmount(3,3)
max_gno_to_zkevm = getMinSendAmount(3,4)

# Min Amounts from MATIC
min_matic_to_arb = getMinSendAmount(4,5)
min_matic_to_opt = getMinSendAmount(4,0)
min_matic_to_bsc = getMinSendAmount(4,1)
min_matic_to_gno = getMinSendAmount(4,2)
min_matic_to_era = getMinSendAmount(4,3)
min_matic_to_zkevm = getMinSendAmount(4,4)
min_matic_to_avax = getMinSendAmount(4,6)
min_matic_to_aur = getMinSendAmount(4,7)

# Max Amounts from MATIC
max_matic_to_arb = getMaxSendAmount(4,5)
max_matic_to_opt = getMaxSendAmount(4,0)
max_matic_to_bsc = getMaxSendAmount(4,1)
max_matic_to_gno = getMaxSendAmount(4,2)
max_matic_to_era = getMaxSendAmount(4,3)
max_matic_to_zkevm = getMaxSendAmount(4,4)
max_matic_to_avax = getMaxSendAmount(4,6)
max_matic_to_aur = getMaxSendAmount(4,7)

# Min Amounts from Era
#min_era_to_eth = ''
min_era_to_arb = getMinSendAmount(5,5)
min_era_to_opt = getMinSendAmount(5,0)
min_era_to_bsc = getMinSendAmount(5,1)
min_era_to_gno = getMinSendAmount(5,2)
min_era_to_matic = getMinSendAmount(5,3)
min_era_to_zkevm = getMinSendAmount(5,4)
min_era_to_avax = getMinSendAmount(5,6)
min_era_to_aur = getMinSendAmount(5,7)

# Max Amounts from Era
max_era_to_arb = getMaxSendAmount(5,5)
max_era_to_opt = getMaxSendAmount(5,0)
max_era_to_bsc = getMaxSendAmount(5,1)
max_era_to_gno = getMaxSendAmount(5,2)
max_era_to_matic = getMaxSendAmount(5,3)
max_era_to_zkevm = getMaxSendAmount(5,4)
max_era_to_avax = getMaxSendAmount(5,6)
max_era_to_aur = getMaxSendAmount(5,7)

# Min Amounts from zkEVM
#min_zkevm_to_eth = ''
min_zkevm_to_arb = getMinSendAmount(6,5)
min_zkevm_to_opt = getMinSendAmount(6,0)
min_zkevm_to_bsc = getMinSendAmount(6,1)
min_zkevm_to_gno = getMinSendAmount(6,2)
min_zkevm_to_matic = getMinSendAmount(6,3)
min_zkevm_to_era = getMinSendAmount(6,4)
min_zkevm_to_avax = getMinSendAmount(6,6)
min_zkevm_to_aur = getMinSendAmount(6,7)

# Max Amounts from zkeEVM
max_zkevm_to_arb = getMaxSendAmount(6,5)
max_zkevm_to_opt = getMaxSendAmount(6,0)
max_zkevm_to_bsc = getMaxSendAmount(6,1)
max_zkevm_to_gno = getMaxSendAmount(6,2)
max_zkevm_to_matic = getMaxSendAmount(6,3)
max_zkevm_to_era = getMaxSendAmount(6,4)
max_zkevm_to_avax = getMaxSendAmount(6,6)
max_zkevm_to_aur = getMaxSendAmount(6,7)

# Min Amounts from Arbitrum
#min_arb_to_eth = ''
min_arb_to_zkevm = getMinSendAmount(7,5)
min_arb_to_opt = getMinSendAmount(7,0)
min_arb_to_bsc = getMinSendAmount(7,1)
min_arb_to_gno = getMinSendAmount(7,2)
min_arb_to_matic = getMinSendAmount(7,3)
min_arb_to_era = getMinSendAmount(7,4)
min_arb_to_avax = getMinSendAmount(7,6)
min_arb_to_aur = getMinSendAmount(7,7)

# Max Amounts from Arbitrum
max_arb_to_zkevm = getMaxSendAmount(7,5)
max_arb_to_opt = getMaxSendAmount(7,0)
max_arb_to_bsc = getMaxSendAmount(7,1)
max_arb_to_gno = getMaxSendAmount(7,2)
max_arb_to_matic = getMaxSendAmount(7,3)
max_arb_to_era = getMaxSendAmount(7,4)
max_arb_to_avax = getMaxSendAmount(7,6)
max_arb_to_aur = getMaxSendAmount(7,7)

# Min Amounts from Avalanche
#min_avax_to_eth = ''
min_avax_to_zkevm = getMinSendAmount(8,5)
min_avax_to_opt = getMinSendAmount(8,0)
min_avax_to_bsc = getMinSendAmount(8,1)
min_avax_to_gno = getMinSendAmount(8,2)
min_avax_to_matic = getMinSendAmount(8,3)
min_avax_to_era = getMinSendAmount(8,4)
min_avax_to_arb = getMinSendAmount(8,6)
min_avax_to_aur = getMinSendAmount(8,7)

# Max Amounts from Avalanche
max_avax_to_zkevm = getMaxSendAmount(8,5)
max_avax_to_opt = getMaxSendAmount(8,0)
max_avax_to_bsc = getMaxSendAmount(8,1)
max_avax_to_gno = getMaxSendAmount(8,2)
max_avax_to_matic = getMaxSendAmount(8,3)
max_avax_to_era = getMaxSendAmount(8,4)
max_avax_to_arb = getMaxSendAmount(8,6)
max_avax_to_aur = getMaxSendAmount(8,7)

# Min Amounts from Avalanche
#min_aur_to_eth = ''
min_aur_to_zkevm = getMinSendAmount(9,5)
min_aur_to_opt = getMinSendAmount(9,0)
min_aur_to_bsc = getMinSendAmount(9,1)
min_aur_to_gno = getMinSendAmount(9,2)
min_aur_to_matic = getMinSendAmount(9,3)
min_aur_to_era = getMinSendAmount(9,4)
min_aur_to_arb = getMinSendAmount(9,6)
min_aur_to_avax= getMinSendAmount(9,7)

# Max Amounts from Avalanche
max_aur_to_zkevm = getMaxSendAmount(9,5)
max_aur_to_opt = getMaxSendAmount(9,0)
max_aur_to_bsc = getMaxSendAmount(9,1)
max_aur_to_gno = getMaxSendAmount(9,2)
max_aur_to_matic = getMaxSendAmount(9,3)
max_aur_to_era = getMaxSendAmount(9,4)
max_aur_to_arb = getMaxSendAmount(9,6)
max_aur_to_avax = getMaxSendAmount(9,7)

# Min Amounts from Aurora
min_aur_to_opt = getMinSendAmount(8,0)
min_aur_to_bsc = getMinSendAmount(8,1)
min_aur_to_gno = getMinSendAmount(8,2)
min_aur_to_matic = getMinSendAmount(8,3)
min_aur_to_era = getMinSendAmount(8,4)
min_aur_to_zkevm = getMinSendAmount(8,5)
min_aur_to_arb = getMinSendAmount(8,6)
min_aur_to_avax = getMinSendAmount(8,7)

# Max Amounts from Aurora
max_aur_to_opt = getMinSendAmount(8,0)
max_aur_to_bsc = getMinSendAmount(8,1)
max_aur_to_gno = getMinSendAmount(8,2)
max_aur_to_matic = getMinSendAmount(8,3)
max_aur_to_era = getMinSendAmount(8,4)
max_aur_to_zkevm = getMinSendAmount(8,5)
max_aur_to_arb = getMinSendAmount(8,6)
max_aur_to_avax = getMinSendAmount(8,7)


