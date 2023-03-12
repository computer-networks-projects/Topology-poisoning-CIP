import sys
import time
from os import popen
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sendp, IP, UDP, Ether, TCP, sniff
from random import randrange
import time

def main():
  launchAttack()

def launchAttack():

  for i in range(0, 6):
      print("hi", sys.argv[1], sys.argv[2])
      packets=sniff(iface=sys.argv[1], prn=lambda x:x.summary(), count=1) 
      sendp(packets, iface = sys.argv[2])

      packets=sniff(iface=sys.argv[2], prn=lambda x:x.summary(), count=1) 
      sendp(packets, iface = sys.argv[1])
if __name__=="__main__":
  main()
                                                                                                                                                                                                                                                                                                       
