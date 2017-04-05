from urllib2 import urlopen
import xml.etree.ElementTree as ET

# Get XML data from NIST beacon record
xmldata = urlopen('https://beacon.nist.gov/rest/record/1491186870') # example record

# Define XML namespace
ns = {'beacon': 'http://beacon.nist.gov/record/0.1/'}

# Parse tree, get root ('record')
tree = ET.parse(xmldata)
root = tree.getroot()

# Get outputValue
outputValue = root.find('beacon:outputValue', ns)
print outputValue.text

# Still to do:
# Check signature
# HTTPS
# Get most recent signature