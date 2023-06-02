from config import *
logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white>"
                          " | <level>{level: <8}</level>"
                          " | <cyan>{line}</cyan>"
                          " - <white>{message}</white>")

def getNativeSimbol(chain:str)->str:
     if (chain == 'ETH') or (chain == 'OPT') or (chain == 'ARB') or (chain == 'AUR') or (chain == 'ERA'):
          return 'ether'
     
     elif (chain == 'MATIC') or (chain == 'ZKEVM'):
          return 'matic'
     
     elif (chain == 'BSC'):
          return 'bnb'
     
     elif (chain == 'GNO'):
          return 'xdai'
     
     elif (chain == 'AVAX'):
          return 'avax'
     
     elif (chain == 'FTM'):
          return 'ftm'
     
def minGasAmount(parent_chain, destination_chain) -> tuple:
     # From Ethereum
     if (parent_chain == 'ETH') and (destination_chain == 'OPT'):
          return min_eth_to_opt,max_eth_to_opt 
        
     if (parent_chain == 'ETH') and (destination_chain == 'BSC'):
          return min_eth_to_bsc,max_eth_to_bsc

     if (parent_chain == 'ETH') and (destination_chain == 'GNO'):
          return min_eth_to_gno,max_eth_to_gno

     if (parent_chain == 'ETH') and (destination_chain == 'MATIC'):
          return min_eth_to_matic,max_eth_to_matic

     if (parent_chain == 'ETH') and (destination_chain == 'ERA'):
          return min_eth_to_era,max_eth_to_era

     if (parent_chain == 'ETH') and (destination_chain == 'ZKEVM'):
          return min_eth_to_zkevm,max_eth_to_zkevm
            
     if (parent_chain == 'ETH') and (destination_chain == 'ARB'):
          return min_eth_to_arb,max_eth_to_arb 
          
     if (parent_chain == 'ETH') and (destination_chain == 'AVAX'):
          return min_eth_to_avax,max_eth_to_avax
      
     if (parent_chain == 'ETH') and (destination_chain == 'AUR'):
          return min_eth_to_aur,max_eth_to_aur
     
     if (parent_chain == 'ETH') and (destination_chain == 'FTM'):
          return min_eth_to_ftm,max_eth_to_ftm
         
     # From Optimism        
     if (parent_chain == 'OPT') and (destination_chain == 'BSC'):
          return min_opt_to_bsc,max_opt_to_bsc 

     if (parent_chain == 'OPT') and (destination_chain == 'GNO'):
          return min_opt_to_gno,max_opt_to_gno

     if (parent_chain == 'OPT') and (destination_chain == 'MATIC'):
          return min_opt_to_matic,max_opt_to_matic

     if (parent_chain == 'OPT') and (destination_chain == 'ERA'):
          return min_opt_to_era,max_opt_to_era

     if (parent_chain == 'OPT') and (destination_chain == 'ZKEVM'):
          return min_opt_to_zkevm
            
     if (parent_chain == 'OPT') and (destination_chain == 'ARB'):
          return min_opt_to_arb,max_opt_to_arb 
          
     if (parent_chain == 'OPT') and (destination_chain == 'AVAX'):
          return min_opt_to_avax,max_opt_to_avax
      
     if (parent_chain == 'OPT') and (destination_chain == 'AUR'):
          return min_opt_to_aur,max_opt_to_aur
     
     if (parent_chain == 'OPT') and (destination_chain == 'FTM'):
          return min_opt_to_ftm,max_opt_to_ftm

     # From BNB Chain       
     if (parent_chain == 'BSC') and (destination_chain == 'OPT'):
          return min_bsc_to_opt,max_bsc_to_opt

     if (parent_chain == 'BSC') and (destination_chain == 'GNO'):
          return min_bsc_to_gno,max_bsc_to_gno

     if (parent_chain == 'BSC') and (destination_chain == 'MATIC'):
          return min_bsc_to_matic,max_bsc_to_matic

     if (parent_chain == 'BSC') and (destination_chain == 'ERA'):
          return min_bsc_to_era,max_bsc_to_era

     if (parent_chain == 'BSC') and (destination_chain == 'ZKEVM'):
          return min_bsc_to_zkevm,max_bsc_to_zkevm
            
     if (parent_chain == 'BSC') and (destination_chain == 'ARB'):
          return min_bsc_to_arb,max_bsc_to_arb 
          
     if (parent_chain == 'BSC') and (destination_chain == 'AVAX'):
          return min_bsc_to_avax,max_bsc_to_avax
      
     if (parent_chain == 'BSC') and (destination_chain == 'AUR'):
          return min_bsc_to_aur,max_bsc_to_aur
     
     if (parent_chain == 'BSC') and (destination_chain == 'FTM'):
          return min_bsc_to_ftm,max_bsc_to_ftm

     # From Gnosis 
     if (parent_chain == 'GNO') and (destination_chain == 'OPT'):
          return min_gno_to_opt,max_gno_to_opt 

     if (parent_chain == 'GNO') and (destination_chain == 'BSC'):
          return min_gno_to_bsc,max_gno_to_bsc

     if (parent_chain == 'GNO') and (destination_chain == 'MATIC'):
          return min_gno_to_matic,max_gno_to_matic

     if (parent_chain == 'GNO') and (destination_chain == 'ERA'):
          return min_gno_to_era,max_gno_to_era

     if (parent_chain == 'GNO') and (destination_chain == 'ZKEVM'):
          return min_gno_to_zkevm,max_gno_to_zkevm
            
     if (parent_chain == 'GNO') and (destination_chain == 'ARB'):
          return min_gno_to_arb,max_gno_to_arb 
          
     if (parent_chain == 'GNO') and (destination_chain == 'AVAX'):
          return min_gno_to_avax,max_gno_to_avax
      
     if (parent_chain == 'GNO') and (destination_chain == 'AUR'):
          return min_gno_to_aur,max_gno_to_aur
     
     if (parent_chain == 'GNO') and (destination_chain == 'FTM'):
          return min_gno_to_ftm,max_gno_to_ftm

     # From Polygon 
     if (parent_chain == 'MATIC') and (destination_chain == 'OPT'):
          return min_matic_to_opt,max_matic_to_opt 

     if (parent_chain == 'MATIC') and (destination_chain == 'GNO'):
          return min_matic_to_gno,max_matic_to_gno

     if (parent_chain == 'MATIC') and (destination_chain == 'BSC'):
          return min_matic_to_bsc,max_matic_to_bsc

     if (parent_chain == 'MATIC') and (destination_chain == 'ERA'):
          return min_matic_to_era,max_matic_to_era

     if (parent_chain == 'MATIC') and (destination_chain == 'ZKEVM'):
          return min_matic_to_zkevm,max_matic_to_zkevm
            
     if (parent_chain == 'MATIC') and (destination_chain == 'ARB'):
          return min_matic_to_arb,max_matic_to_arb 
          
     if (parent_chain == 'MATIC') and (destination_chain == 'AVAX'):
          return min_matic_to_avax,max_matic_to_avax
      
     if (parent_chain == 'MATIC') and (destination_chain == 'AUR'):
          return min_matic_to_aur,max_matic_to_aur
     
     if (parent_chain == 'MATIC') and (destination_chain == 'FTM'):
          return min_matic_to_ftm,max_matic_to_ftm

      # From Arbitrum
     if (parent_chain == 'ARB') and (destination_chain == 'OPT'):
          return min_arb_to_opt,max_arb_to_opt 

     if (parent_chain == 'ARB') and (destination_chain == 'BSC'):
          return min_arb_to_bsc,max_arb_to_bsc

     if (parent_chain == 'ARB') and (destination_chain == 'GNO'):
          return min_arb_to_gno,max_arb_to_gno

     if (parent_chain == 'ARB') and (destination_chain == 'MATIC'):
          return min_arb_to_matic,max_arb_to_matic

     if (parent_chain == 'ARB') and (destination_chain == 'ERA'):
          return min_arb_to_era,max_arb_to_era

     if (parent_chain == 'ARB') and (destination_chain == 'ZKEVM'):
          return min_arb_to_zkevm,max_arb_to_zkevm
            
     if (parent_chain == 'ARB') and (destination_chain == 'AVAX'):
          return min_arb_to_avax,max_arb_to_avax 
               
     if (parent_chain == 'ARB') and (destination_chain == 'AUR'):
          return min_arb_to_aur,max_arb_to_aur
          
     if (parent_chain == 'ARB') and (destination_chain == 'FTM'):
          return min_arb_to_ftm,max_arb_to_ftm    
     
     # From AVAX 
     if (parent_chain == 'AVAX') and (destination_chain == 'OPT'):
          return min_avax_to_opt,max_avax_to_opt 

     if (parent_chain == 'AVAX') and (destination_chain == 'BSC'):
          return min_avax_to_bsc,max_avax_to_bsc

     if (parent_chain == 'AVAX') and (destination_chain == 'GNO'):
          return min_avax_to_gno,max_avax_to_gno

     if (parent_chain == 'AVAX') and (destination_chain == 'MATIC'):
          return min_avax_to_matic,max_avax_to_matic

     if (parent_chain == 'AVAX') and (destination_chain == 'ERA'):
          return min_avax_to_era,max_avax_to_era

     if (parent_chain == 'AVAX') and (destination_chain == 'ZKEVM'):
          return min_avax_to_zkevm,max_avax_to_zkevm
            
     if (parent_chain == 'AVAX') and (destination_chain == 'ARB'):
          return min_avax_to_arb,max_avax_to_arb 
               
     if (parent_chain == 'AVAX') and (destination_chain == 'AUR'):
          return min_avax_to_aur,max_avax_to_aur
     
     if (parent_chain == 'AVAX') and (destination_chain == 'FTM'):
          return min_avax_to_aur,max_avax_to_aur

      # From Aurora
     if (parent_chain == 'AUR') and (destination_chain == 'OPT'):
          return min_aur_to_opt,max_aur_to_opt 

     if (parent_chain == 'AUR') and (destination_chain == 'BSC'):
          return min_aur_to_bsc,max_aur_to_bsc

     if (parent_chain == 'AUR') and (destination_chain == 'GNO'):
          return min_aur_to_gno,max_aur_to_gno

     if (parent_chain == 'AUR') and (destination_chain == 'MATIC'):
          return min_aur_to_matic,max_aur_to_matic

     if (parent_chain == 'AUR') and (destination_chain == 'ERA'):
          return min_aur_to_era,max_aur_to_era

     if (parent_chain == 'AUR') and (destination_chain == 'ZKEVM'):
          return min_aur_to_zkevm,max_aur_to_zkevm
            
     if (parent_chain == 'AUR') and (destination_chain == 'ARB'):
          return min_aur_to_arb,max_aur_to_arb
      
     if (parent_chain == 'AUR') and (destination_chain == 'AVAX'):
          return min_aur_to_avax,max_aur_to_avax
      
     if (parent_chain == 'AUR') and (destination_chain == 'FTM'):
          return min_aur_to_ftm,max_aur_to_ftm

     # From Fantom
     if (parent_chain == 'FTM') and (destination_chain == 'OPT'):
          return min_opt_to_ftm, max_opt_to_ftm
     if (parent_chain == 'FTM') and (destination_chain == 'BSC'):
          return min_ftm_to_bsc,max_ftm_to_bsc

     if (parent_chain == 'FTM') and (destination_chain == 'GNO'):
          return min_ftm_to_gno,max_ftm_to_gno

     if (parent_chain == 'FTM') and (destination_chain == 'MATIC'):
          return min_ftm_to_matic,max_ftm_to_matic

     if (parent_chain == 'FTM') and (destination_chain == 'ERA'):
          return min_ftm_to_era,max_ftm_to_era

     if (parent_chain == 'FTM') and (destination_chain == 'ZKEVM'):
          return min_ftm_to_zkevm,max_ftm_to_zkevm
            
     if (parent_chain == 'FTM') and (destination_chain == 'ARB'):
          return min_ftm_to_arb,max_ftm_to_arb
      
     if (parent_chain == 'FTM') and (destination_chain == 'AVAX'):
          return min_ftm_to_avax,max_ftm_to_avax
      
     if (parent_chain == 'FTM') and (destination_chain == 'AUR'):
          return min_ftm_to_aur,max_ftm_to_aur
  
               
def calculateGasPrice(private_key,tx:dict):
        w3 = Web3(Web3.HTTPProvider(rpc))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        address = Web3.to_checksum_address(w3.eth.account.from_key(private_key).address)
        gas_price = w3.to_wei(str(w3.eth.gas_price), 'wei')
        gas_limit = getGasLimit(parent_chain)   
        nonce = w3.eth.get_transaction_count(address)
        tx = {
            'nonce': nonce,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'value': w3.to_wei(send_amount,'ether')
        }              
        estimated_gas = w3.eth.estimate_gas(tx)
        gas_limit = int(estimated_gas * 1.3)
        # update the update the gas-parameters of tx
        tx['gas'] = gas_limit
        return tx

def send_tx(args):
    #Function: depositNativeToken(uint256 destinationChainId,address _to)
    private_key = args #recipient_addresses(this implementation has been remove)
    address = None
    try:
        address = Web3.to_checksum_address(w3.eth.account.from_key(private_key).address)
        gas_price = w3.to_wei(str(w3.eth.gas_price), 'wei')
        gas_limit = getGasLimit(parent_chain)   
        nonce = w3.eth.get_transaction_count(address)
        # Prepare the transaction data
        tx_data = {
            #'from': address,
            'nonce': nonce,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'value': w3.to_wei(send_amount,'ether')
        }
        #recalculate gas
        tx_data = calculateGasPrice(private_key=private_key,tx=tx_data)
        if True:#tx_type == 1:
            transaction = contract_refuel.functions.depositNativeToken(destinationChainId,address).build_transaction(tx_data)
            
            # Sign the transaction with the receiver's private key
            signed_txn = w3.eth.account.sign_transaction(transaction,private_key=private_key)
            
            # Send the transaction to the network
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

            # Wait for the transaction to be mined
            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            tx_hash = w3.to_hex(w3.keccak(signed_txn.rawTransaction))

            # Check if the transaction was successful
            if receipt['status'] == 1:
                logger.info(f'Refueling from {address} | {tx_explorer}tx/{tx_hash}')
                logger.info(f'Waiting txn for destination chain ({destination_chain}) {dist_tx_explorer}address/{address}/#internaltx')
            
            else:
                raise ValueError(f"Refueling from {address} failed with receipt status {receipt['status']}")

    except Exception as error:
        logger.error(f'{address} | {error}')

if __name__ == '__main__':
    print('-' * 108)
    print((' '*32)+'BUNGEE BATCH REFUELER'+(' '*32))
    print('-' * 108)
    print('Select origin chain:')
    print('0. Ethereum(ETH)')
    print('1. Optimism(OPT)')
    print('2. BNB Chain(BSC)')
    print('3. Gnosis(GNO)')
    print('4. Polygon(Matic)')
    print('5. ERA(while no implementaton)')
    print('6. ZKEVM(while no implementaton)')
    print('7. Arbitrum(ARB)')
    print('8. Fantom')
    print('9. Avalanche C-Chain(AVAX)')
    print('10. Aurora(AUR)')
    parent_chain = input('Input short name of chain(ETH,ARB etc.): ')
    parent_chain = parent_chain.upper()
    if parent_chain == 'ETH':
         chainId = 1
         rpc = RPC_ETH
         contract = BUNGEE_ETH_ROUNER
         tx_explorer = EXP_ETH
    elif parent_chain == 'OPT':
         chainId = 10
         rpc = RPC_OPT
         contract = BUNGEE_OPT_ROUTER
         tx_explorer = EXP_OPT
    elif parent_chain == 'BSC':
         chainId = 56
         rpc = RPC_BSC
         contract = BUNGEE_BSC_ROUTER
         tx_explorer = EXP_BSC
         
    elif parent_chain == 'GNO':
         chainId = 100
         rpc = RPC_GNO
         contract = BUNGEE_GNO_ROUTER
         tx_explorer = EXP_GNO

    elif parent_chain == 'MATIC':
         chainId = 137
         rpc = RPC_MATIC
         contract = BUNGEE_MATIC_ROUNER
         tx_explorer = EXP_MATIC

    elif parent_chain == 'ERA':
         chainId = 1101
         rpc = RPC_ERA
         contract = BUNGEE_ERA_ROUNER
         tx_explorer = EXP_ERA

    elif parent_chain == 'ZKEVM':
         chainId = 1101
         rpc = RPC_ZKEVM
         contract = BUNGEE_ZKEVM_ROUNER
         tx_explorer = EXP_ZKEVM

    elif parent_chain == 'ARB':
         chainId = 42161
         rpc = RPC_ARB
         contract = BUNGEE_ARB_ROUNER
         tx_explorer = EXP_ARB

    elif parent_chain == 'AVAX':
         chainId = 43114
         rpc = RPC_AVAX
         contract = BUNGEE_AVAX_ROUNER
         tx_explorer = EXP_AVAX

    elif parent_chain == 'AUR':
         chainId = 1313161554
         rpc = RPC_AUR
         contract = BUNGEE_AUR_ROUNER
         tx_explorer = EXP_AUR

    elif parent_chain == 'FTM':
         chainId = 250
         rpc = RPC_FTM
         contract = BUNGEE_FTM_ROUNER
         tx_explorer = EXP_FTM         

    print(f'{parent_chain} selected like origin chain')

    destinationChainId = chainId
    while (destinationChainId ==  chainId):
        destination_chain = input(f'Select target chain (ETH and {parent_chain} can not be select): ')
        destination_chain = destination_chain.upper()

        if destination_chain == chainId:
            print(f'origin chain {destination_chain} can not be select like destination chain')

        elif destination_chain == 'ETH':
            print(f'{destination_chain} can not be select like destination chain')
        
        elif destination_chain == 'OPT':
            destinationChainId = 10
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_OPT
 
        elif destination_chain == 'BSC':
            destinationChainId = 56
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_BSC

        elif destination_chain == 'GNO':
            destinationChainId = 100
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_GNO
            
        elif destination_chain == 'MATIC':
            destinationChainId = 137
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_MATIC

        elif destination_chain == 'ERA':
            destinationChainId = 324
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_ERA

        elif destination_chain == 'ZKEVM':
            destinationChainId = 1101
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_ZKEVM

        elif destination_chain == 'ARB':
            destinationChainId = 42161
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_ARB

        elif destination_chain == 'AVAX':
            destinationChainId = 43114
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_AVAX

        elif destination_chain == 'AUR':
            destinationChainId = 1313161554
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_AUR

        elif destination_chain == 'FTM':
            destinationChainId = 250
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_AUR
                     
    gas_token = getNativeSimbol(parent_chain)
    print(f"Minimum amount for send = {gas_amount[0]} {gas_token} + 10%")    
    print(f"Maximum amount for send = {gas_amount[1]} {gas_token} - 10%")

    #print(f'Minimum Gas amount: {gas_amount} {gas_token} + 10%')
    print(f"You can input value >= {gas_amount[0]} {gas_token} <= {gas_amount[1]} {gas_token}")
    print (f"You also can input 'min'/ 'max' for send minimum/maximum amounts {gas_token}")
    amount = ''
    while (amount != 'MAX') or (amount != 'MIN') or ((amount) < gas_amount[0]) or (float(amount) > gas_amount[1]):
     amount = input('Input amount to send: ')
     amount = amount.upper()

     #Setting gas amount for send
     if amount == 'MAX':
          amount = gas_amount[1] * 0.9
          send_amount = float(amount)
          break

     elif amount == 'MIN':
          amount = gas_amount[0] * 1.1
          send_amount = float(amount)
          break

     else:
          send_amount = float(amount)
          break

    print(f'Starting send Gas from {parent_chain} to {destination_chain}')
    print(f"{amount} {gas_token} will be send from all your addressess")
    w3 = Web3(Web3.HTTPProvider(rpc))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    #Loads ABI for contracts
    with open('ABI/socket.json', 'r', encoding='utf-8-sig') as file:
            SOCKET_ABI = file.read().strip().replace('\n', '').replace(' ', '')   
    contract_refuel = w3.eth.contract(address=Web3.to_checksum_address(contract),
                               abi=SOCKET_ABI)
    
    #Loads private_keys
    with open('accounts.txt', encoding='utf-8-sig') as file:
        private_keys = [row.strip() for row in file]
    num_wallets = len(private_keys)
    logger.info(f'Loaded {num_wallets} wallets')

    # Loads chain.json      
    file_path = "chains.json"  # Path to the JSON file

     # Load the JSON data from the file
    with open(file_path) as file:
     data = json.load(file)

    processed_addresses = 0
    while processed_addresses < num_wallets:
        with Pool(processes=len(private_keys)) as executor:
            executor.map(send_tx, private_keys)
        processed_addresses += num_wallets - processed_addresses

    input('Press any key to exit..')