#import decimal,math
import os
import time
from web3 import Web3
from web3.contract import Contract
from web3.middleware import geth_poa_middleware
from loguru import logger
from sys import stderr
from multiprocessing.dummy import Pool
from dotenv import load_dotenv

load_dotenv()
BUNGEE_ETH_ROUNER = os.getenv('BUNGEE_ETH_ROUNER')
BUNGEE_ARB_ROUNER = os.getenv('BUNGEE_ARB_ROUNER')
BUNGEE_OPT_ROUTER = os.getenv('BUNGEE_OPT_ROUTER')
BUNGEE_BSC_ROUTER = os.getenv('BUNGEE_BSC_ROUTER')
BUNGEE_MATIC_ROUNER = os.getenv('BUNGEE_MATIC_ROUNER')
BUNGEE_FTM_ROUNER = os.getenv('BUNGEE_FTM_ROUNER')

RPC_ETH = os.getenv('RPC_ETH')
RPC_ARB = os.getenv('RPC_ARB')
RPC_OPT = os.getenv('RPC_OPT')
RPC_BSC = os.getenv('RPC_BSC')
RPC_MATIC =  os.getenv('RPC_MATIC')
RPC_FTM =  os.getenv('RPC_FTM')

EXP_ETH = 'https://etherscan.io/tx/'
EXP_ARB = 'https://arbiscan.io/tx/'
EXP_OPT = 'https://optimistic.etherscan.io/tx/'
EXP_BSC = 'https://bscscan.com/tx/'
EXP_MATIC = 'https://polygonscan.com/tx/'
EXP_FTM = 'https://ftmscan.com/tx/'

MIN_ETH_TO_ARB = 0.0021
MIN_ETH_TO_OPT = 0.0045
MIN_ETH_TO_BSC = 0.00045
MIN_ETH_TO_MATIC = 0.00014
MIN_ETH_TO_FTM = ''

MAX_ETH_TO_ARB = 0.015
MAX_ETH_TO_OPT = 0.027
MAX_ETH_TO_BSC = 0.0034
MAX_ETH_TO_MATIC = 0.011

#MIN_ARB_TO_ETH = ''
MIN_ARB_TO_OPT = 0.0045
MIN_ARB_TO_BSC = 0.00045
MIN_ARB_TO_MATIC = 0.00021
MIN_ARB_TO_FTM = 0.00059


MAX_ARB_TO_OPT = 0.027
MAX_ARB_TO_BSC = 0.0034
MAX_ARB_TO_MATIC = 0.011
MAX_ARB_TO_FTM = 0.017

#MIN_OPT_TO_ETH = ''
MIN_OPT_TO_ARB = 0.003
MIN_OPT_TO_BSC = 0.00045
MIN_OPT_TO_MATIC = 0.00021
MIN_OPT_TO_FTM = 0.00059

MAX_OPT_TO_ARB = 0.016
MAX_OPT_TO_BSC = 0.0034
MAX_OPT_TO_MATIC = 0.0095
MAX_OPT_TO_FTM = 0.017


#MIN_BSC_TO_ETH = ''
MIN_BSC_TO_ARB = 0.012
MIN_BSC_TO_OPT = 0.027
MIN_BSC_TO_MATIC = 0.0013
MIN_BSC_TO_FTM = 0.0035

MAX_BSC_TO_ARB = 0.098
MAX_BSC_TO_OPT = 0.16
MAX_BSC_TO_MATIC = 0.063
MAX_BSC_TO_FTM = 0.1

#MIN_MATIC_TO_ETH = ''
MIN_MATIC_TO_ARB = 4.19
MIN_MATIC_TO_OPT = 9.32
MIN_MATIC_TO_BSC = 0.93
MIN_MATIC_TO_FTM = 1.23

MAX_MATIC_TO_ARB = 36.36
MAX_MATIC_TO_OPT = 59.01
MAX_MATIC_TO_BSC = 7.46
MAX_MATIC_TO_FTM = 37.71

MIN_FTM_TO_ARB = 21.09
MIN_FTM_TO_OPT = 30.29
MIN_FTM_TO_BSC = 2.23
MIN_FTM_TO_MATIC = 0.7

MAX_FTM_TO_ARB = 84.34
MAX_FTM_TO_OPT = 140.81
MAX_FTM_TO_BSC = 17.8
MAX_FTM_TO_MATIC = 48.31


