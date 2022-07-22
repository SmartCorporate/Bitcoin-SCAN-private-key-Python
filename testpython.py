from bitcointools import *
import sys
import os
import re
from time import sleep
from urllib.request import urlopen
import winsound
import time

print( "\n-------||---||---------------------------------" );
print( "\n---===============-----------------------------" );
print( "\n---==||===========-----------------------------" );
print( "\n-----||--      ---==---------------- ----------" );
print( "\n-----||--      ---==---------------------------" );
print( "\n-----||----- ---==-----------------------------" );
print( "\n-----||---------==-----------------------------" );
print( "\n-----||----- ---=====--------------------------" );
print( "\n-----||--       ----===-----------USA ---------" );
print( "\n-----||--        -----==---------CHINA---------" );
print( "\n-----||--       ----===------------------------" );
print( "\n---==||=============---------------------------" );
print( "\n---===============----------BITCOIN  CHECKER---" );
print( "\n-------||---||--------------------2022---------" );
print( "\n----------------------------------2023---------" );

time.sleep(3)



while True:

  print('===========[]==[] BTC SCAN []==[]================')
 
  priv = random_key()
  print('Private random key is:')
  print (priv )

  pub = privtopub(priv)

  address = pubtoaddr(pub)
  print('Public address is:')
  print (address)


  check_address = address

  blockchain_tags_json = [ 
        'total_received',
        'final_balance',
        ]

  SATOSHIS_PER_BTC = 1e+8
  
  htmlfile = urlopen("https://blockchain.info/address/%s?format=json" % check_address, timeout = 10)
  htmltext = htmlfile.read().decode('utf-8')
  print( "https://blockchain.info --> Checking... ")
  time.sleep(1)



  blockchain_info_array = []
  tag = ''
  try:
        for tag in blockchain_tags_json:
            blockchain_info_array.append (
                float( re.search( r'%s":(\d+),' % tag, htmltext ).group(1) ) )
  except:
        print( "Error '%s'." % tag );
       

  for i, btc_tokens in enumerate(blockchain_info_array):

        sys.stdout.write ("%s \t= " % blockchain_tags_json[i])
        if btc_tokens > 0.0000000:
            print( "%.8f Bitcoin" % (btc_tokens/SATOSHIS_PER_BTC) );
            text_file = open("addressreport.txt","a")
            text_file.write("\nThis is private random key: " + priv)
            text_file.write("\nThis is btc public address: " + check_address)
            text_file.write("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$!!!!!!!!!!")
            text_file.write("\n The Balance Value is")
            text_file.write("\%.8f Bitcoin" % (btc_tokens/SATOSHIS_PER_BTC))
            text_file.write("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$!!!!!!!!!!")
            text_file.close()
            winsound.Beep(440, 500)
            winsound.Beep(500, 700)
            winsound.Beep(440, 500)
            winsound.Beep(500, 700)
            winsound.Beep(440, 500)
            winsound.Beep(500, 700)

            
        else:
            print( "\%.8f Bitcoin" % (btc_tokens/SATOSHIS_PER_BTC) );
            print( "\n----------------------------------------------------" );
            time.sleep(0.1)
          
            
          
            
           






            
         
           



