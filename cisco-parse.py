from ciscoconfparse import CiscoConfParse
import sys

def cryptomap():
    cisco_conf = CiscoConfParse("cisco.config")
    cis_map  = cisco_conf.find_objects(r'^crypto map CRYPTO')

    for i in cis_map:
        print i.text
        for j in i.children:
            print j.text

def pfsmap():
    cisco_conf = CiscoConfParse("cisco.config")
    cis_map  = cisco_conf.find_objects_w_child(parentspec=r'^crypto map CRYPTO',\
                                               childspec=r'pfs group2')
    for i in cis_map:
        print i.text
        for j in i.children:
            print j.text

def notaes():
    cisco_conf = CiscoConfParse("cisco.config")
    cis_map  = cisco_conf.find_objects_wo_child(r'^crypto map CRYPTO',\
                                              r'transform-set AES')
    for i in cis_map:
        print i.text
        for j in i.children:
            print j.text

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "allmaps":
            cryptomap()
        elif sys.argv[1] == "pfs2":
            pfsmap()
        elif sys.argv[1] == "notaes":
            notaes()

            
