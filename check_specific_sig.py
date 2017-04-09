from urllib2 import urlopen
from time import time
import xml.etree.ElementTree as ET
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from Cryptodome.Signature import pkcs1_15

BEACON_CERT = "/Users/firechant/Downloads/beacon.cer" #TODO: use the one gotten from the site
#TODO: figure out whether you should use the one from the site or the one we downloaded a long time ago


def check_signature():
    #TODO: figure out how to pass XML elements rather than by timestamp
    ts = 1491186870
    xmldata = urlopen("https://beacon.nist.gov/rest/record/%d" % ts)
    ns = {'beacon': 'http://beacon.nist.gov/record/0.1/'} # define xml namespace
    tree = ET.parse(xmldata)
    root = tree.getroot()
    message = root.find('beacon:outputValue', ns)
    signature = root.find('beacon:signature', ns)

    with open(BEACON_CERT, 'r') as f:
        key = RSA.importKey(f.read())
    h = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(h, signature)
        print "valid!"
    except(ValueError, TypeError):
        print "NOT VALID!!!"

check_signature()


def get_current_record():
    #TODO: record -> outputvalue
    ts = int(time())
    xmldata = urlopen("https://beacon.nist.gov/rest/record/%d" % ts)
    ns = {'beacon': 'http://beacon.nist.gov/record/0.1/'} # define xml namespace
    # Parse tree, get root ('record')
    tree = ET.parse(xmldata)
    root = tree.getroot()

    # Get outputValue
    outputValue = root.find('beacon:outputValue', ns)
    return outputValue.text

# Still to do:
# Check signature
# HTTPS
# Get most recent signature
