#Set up a docker environment for this code, and don't try to include superfluous packages!
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random
from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from os.path import exists, join
import os

blackblankimage = random.randint(0, 255) * np.ones(shape=[512, 512, 3], dtype=np.uint8)

cv.putText(blackblankimage, "You did it!", (100, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255))
cv.rectangle(blackblankimage, pt1=(200,200), pt2=(300, 300), color=(0,0,255), thickness=-1)
plt.axis('off')
plt.imshow(blackblankimage)

plt.savefig("./pythonCode1Image.png")

#modify this code so that it also generates self signed certificate and keys
def create_self_signed_cert():    
    k=crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)
    cert=crypto.X509()
    cert.get_subject().C="US"
    cert.get_subject().ST="NV"
    cert.get_subject().L="Reno"
    cert.get_subject().O="University of Nevada, Reno"
    cert.get_subject().OU="CSE"
    cert.get_subject().CN=gethostname()
    cert.set_serial_number(42)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(157680000)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')
    open("josephhogan_selfSignedCertificate.crt","wb").write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    open("josephhogan_privateKey.PEM","wb").write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    cmd='openssl rsa -in josephhogan_privateKey.PEM -pubout -out josephhogan_publicKey.PEM'
    os.system(cmd)
create_self_signed_cert()
