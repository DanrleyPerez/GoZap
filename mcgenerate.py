"""
Mac control if necessary
"""

import getmac
from cryptography.fernet import Fernet
from GoZap import docman

true_mac = getmac.get_mac_address().encode('UTF-8')

chave = Fernet(b'9WsX7EKxNugFasdfdwvzSQTDKohJaBbrdUghwLYBrFw=')

mccry = str(chave.encrypt(true_mac))

docman.grava_txt(mccry, "database\\mc.txt")
