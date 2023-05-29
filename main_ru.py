from config import *
logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white>"
                          " | <level>{level: <8}</level>"
                          " | <cyan>{line}</cyan>"
                          " - <white>{message}</white>")

def minGasAmount(parent_chain, destination_chain) -> float:
     # From Ethereum
     if (parent_chain == 'ETH') and (destination_chain == 'OPT'):
          return min_eth_to_opt 
        
     if (parent_chain == 'ETH') and (destination_chain == 'BSC'):
          return min_eth_to_bsc 

     if (parent_chain == 'ETH') and (destination_chain == 'GNO'):
          return min_eth_to_gno

     if (parent_chain == 'ETH') and (destination_chain == 'MATIC'):
          return min_eth_to_matic

     if (parent_chain == 'ETH') and (destination_chain == 'ERA'):
          return min_eth_to_era

     if (parent_chain == 'ETH') and (destination_chain == 'ZKEVM'):
          return min_eth_to_zkevm
            
     if (parent_chain == 'ETH') and (destination_chain == 'ARB'):
          return min_eth_to_arb 
          
     if (parent_chain == 'ETH') and (destination_chain == 'AVAX'):
          return min_eth_to_avax
      
     if (parent_chain == 'ETH') and (destination_chain == 'AUR'):
          return min_eth_to_aur
         
     # From Optimism        
     if (parent_chain == 'OPT') and (destination_chain == 'BSC'):
          return min_opt_to_bsc 

     if (parent_chain == 'OPT') and (destination_chain == 'GNO'):
          return min_opt_to_gno

     if (parent_chain == 'OPT') and (destination_chain == 'MATIC'):
          return min_opt_to_matic

     if (parent_chain == 'OPT') and (destination_chain == 'ERA'):
          return min_opt_to_era

     if (parent_chain == 'OPT') and (destination_chain == 'ZKEVM'):
          return min_opt_to_zkevm
            
     if (parent_chain == 'OPT') and (destination_chain == 'ARB'):
          return min_opt_to_arb 
          
     if (parent_chain == 'OPT') and (destination_chain == 'AVAX'):
          return min_opt_to_avax
      
     if (parent_chain == 'OPT') and (destination_chain == 'AUR'):
          return min_opt_to_aur

     # From BNB Chain       
     if (parent_chain == 'BSC') and (destination_chain == 'OPT'):
          return min_bsc_to_opt 

     if (parent_chain == 'BSC') and (destination_chain == 'GNO'):
          return min_bsc_to_gno

     if (parent_chain == 'BSC') and (destination_chain == 'MATIC'):
          return min_bsc_to_matic

     if (parent_chain == 'BSC') and (destination_chain == 'ERA'):
          return min_bsc_to_era

     if (parent_chain == 'BSC') and (destination_chain == 'ZKEVM'):
          return min_bsc_to_zkevm
            
     if (parent_chain == 'BSC') and (destination_chain == 'ARB'):
          return min_bsc_to_arb 
          
     if (parent_chain == 'BSC') and (destination_chain == 'AVAX'):
          return min_bsc_to_avax
      
     if (parent_chain == 'BSC') and (destination_chain == 'AUR'):
          return min_bsc_to_aur

     # From Gnosis 
     if (parent_chain == 'GNO') and (destination_chain == 'OPT'):
          return min_gno_to_opt 

     if (parent_chain == 'GNO') and (destination_chain == 'BSC'):
          return min_gno_to_bsc

     if (parent_chain == 'GNO') and (destination_chain == 'MATIC'):
          return min_gno_to_matic

     if (parent_chain == 'GNO') and (destination_chain == 'ERA'):
          return min_gno_to_era

     if (parent_chain == 'GNO') and (destination_chain == 'ZKEVM'):
          return min_gno_to_zkevm
            
     if (parent_chain == 'GNO') and (destination_chain == 'ARB'):
          return min_gno_to_arb 
          
     if (parent_chain == 'GNO') and (destination_chain == 'AVAX'):
          return min_gno_to_avax
      
     if (parent_chain == 'GNO') and (destination_chain == 'AUR'):
          return min_gno_to_aur

     # From Polygon 
     if (parent_chain == 'MATIC') and (destination_chain == 'OPT'):
          return min_matic_to_opt 

     if (parent_chain == 'MATIC') and (destination_chain == 'GNO'):
          return min_matic_to_gno

     if (parent_chain == 'MATIC') and (destination_chain == 'BSC'):
          return min_matic_to_bsc

     if (parent_chain == 'MATIC') and (destination_chain == 'ERA'):
          return min_matic_to_era

     if (parent_chain == 'MATIC') and (destination_chain == 'ZKEVM'):
          return min_matic_to_zkevm
            
     if (parent_chain == 'MATIC') and (destination_chain == 'ARB'):
          return min_matic_to_arb 
          
     if (parent_chain == 'MATIC') and (destination_chain == 'AVAX'):
          return min_matic_to_avax
      
     if (parent_chain == 'MATIC') and (destination_chain == 'AUR'):
          return min_matic_to_aur

      # From Arbitrum
     if (parent_chain == 'ARB') and (destination_chain == 'OPT'):
          return min_arb_to_opt 

     if (parent_chain == 'ARB') and (destination_chain == 'BSC'):
          return min_arb_to_bsc

     if (parent_chain == 'ARB') and (destination_chain == 'GNO'):
          return min_arb_to_gno

     if (parent_chain == 'ARB') and (destination_chain == 'MATIC'):
          return min_arb_to_matic

     if (parent_chain == 'ARB') and (destination_chain == 'ERA'):
          return min_arb_to_era

     if (parent_chain == 'ARB') and (destination_chain == 'ZKEVM'):
          return min_arb_to_zkevm
            
     if (parent_chain == 'ARB') and (destination_chain == 'AVAX'):
          return min_arb_to_avax 
               
     if (parent_chain == 'ARB') and (destination_chain == 'AUR'):
          return min_arb_to_aur     
     
     # From AVAX 
     if (parent_chain == 'AVAX') and (destination_chain == 'OPT'):
          return min_avax_to_opt 

     if (parent_chain == 'AVAX') and (destination_chain == 'BSC'):
          return min_avax_to_bsc

     if (parent_chain == 'AVAX') and (destination_chain == 'GNO'):
          return min_avax_to_gno

     if (parent_chain == 'AVAX') and (destination_chain == 'MATIC'):
          return min_avax_to_matic

     if (parent_chain == 'AVAX') and (destination_chain == 'ERA'):
          return min_avax_to_era

     if (parent_chain == 'AVAX') and (destination_chain == 'ZKEVM'):
          return min_avax_to_zkevm
            
     if (parent_chain == 'AVAX') and (destination_chain == 'ARB'):
          return min_avax_to_arb 
               
     if (parent_chain == 'AVAX') and (destination_chain == 'AUR'):
          return min_avax_to_aur

      # From Aurora
     if (parent_chain == 'AUR') and (destination_chain == 'OPT'):
          return min_aur_to_opt 

     if (parent_chain == 'AUR') and (destination_chain == 'BSC'):
          return min_aur_to_bsc

     if (parent_chain == 'AUR') and (destination_chain == 'GNO'):
          return min_aur_to_gno

     if (parent_chain == 'AUR') and (destination_chain == 'MATIC'):
          return min_aur_to_matic

     if (parent_chain == 'AUR') and (destination_chain == 'ERA'):
          return min_aur_to_era

     if (parent_chain == 'AUR') and (destination_chain == 'ZKEVM'):
          return min_aur_to_zkevm
            
     if (parent_chain == 'AUR') and (destination_chain == 'AVAX'):
          return min_aur_to_arb
      
     if (parent_chain == 'AUR') and (destination_chain == 'AVAX'):
          return min_aur_to_avax
     
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
            'value': w3.to_wei((gas_amount *1.1),'ether')
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
            'value': w3.to_wei((gas_amount*1.1),'ether')
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
                logger.info(f'Газ успешно отправлен с адреса: {address} | {tx_explorer}tx/{tx_hash}')
                logger.info(f'Ожидайте транзакцию в сети назначения ({destination_chain}) {dist_tx_explorer}address/{address}/#internaltx')
            
            else:
                raise ValueError(f"Refueling from {address} failed with receipt status {receipt['status']}")

    except Exception as error:
        logger.error(f'{address} | {error}) ')

if __name__ == '__main__':
    print('-' * 108)
    print((' '*32)+'BUNGEE BATCH REFUELER'+(' '*32))
    print('-' * 108)
    print('Выберите исходную сеть для отправки газа:')
    print('0. Ethereum(ETH)')
    print('1. Optimism(OPT)')
    print('2. BNB Chain(BSC)')
    print('3. Gnosis(GNO)')
    print('4. Polygon(Matic)')
    print('5. zkSync(пока ещё не реализована)')
    print('6. zkEVM(пока ещё не реализована)')
    print('7. Arbitrum(ARB)')
    print('8. Fantom(приостановлена)')
    print('9. Avalanche C-Chain(AVAX)')
    print('10. Aurora(AUR)')
    parent_chain = input('Введите короткое имя сети(ETH,ARB etc.): ')
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
#     elif parent_chain == 'FTM':
#          chainId = 250
#          rpc = RPC_FTM
#          contract = BUNGEE_FTM_ROUNER
#          tx_explorer = EXP_FTM
    print(f'{parent_chain} выбрана в качестве исходной сети')

    destinationChainId = chainId
    while (destinationChainId ==  chainId):
        destination_chain = input(f'Выберите сеть назначения (ETH и {parent_chain} не могут быть выбраны): ')
        destination_chain = destination_chain.upper()

        if destination_chain == chainId:
            print(f'исходная сеть {destination_chain} не может быть выбрана в качестве сети назначения')

        elif destination_chain == 'ETH':
            print(f'{destination_chain} не может быть выбрана в качестве сети назначения')
        
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
            
     #    elif destination_chain == 'FTM':
     #        destinationChainId = 250
     #        gas_amount = minGasAmount(parent_chain,destination_chain)
     #        dist_tx_explorer = EXP_FTM   
       
    print(f'Начинаю отправлять газ из {parent_chain} в {destination_chain}')
    print(f'Минимальная сумма отправки: {gas_amount} {parent_chain} + 25%')
    
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
    logger.info(f'Загружено {num_wallets} кошельков')

    processed_addresses = 0
    while processed_addresses < num_wallets:
        with Pool(processes=len(private_keys)) as executor:
            executor.map(send_tx, private_keys)
        processed_addresses += num_wallets - processed_addresses

    input('Для выхода нажмите любую клавишу..')