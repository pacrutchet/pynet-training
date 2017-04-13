#!/usr/bin/env python
'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
import time
import socket
import sys
import getpass



class TelnetCisco():
    ip_addr = ""
    username = ""
    password = ""
    remote_conn = ""
    TELNET_PORT = 23
    TELNET_TIMEOUT = 6

    def __init__(self, ip_addr, username, password):
        '''
        Write a script that connects to the lab pynet-rtr1, logins, and executes the
        'show ip int brief' command.
        '''
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

        self.remote_conn = self.telnet_connect()
        output = self.login()

        time.sleep(1)
        output += self.remote_conn.read_very_eager()
        self.disable_paging()

        print "\n\n"
        print output
        print "\n\n"

    def __del__(self):
        self.remote_conn.close()

    def send_command(self, cmd):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(1)
        return self.remote_conn.read_very_eager()

    def login(self):
        '''
        Login to network device
        '''
        output = self.remote_conn.read_until("sername:", self.TELNET_TIMEOUT)
        self.remote_conn.write(self.username + '\n')
        output += self.remote_conn.read_until("ssword:", self.TELNET_TIMEOUT)
        self.remote_conn.write(self.password + '\n')
        return output

    def disable_paging(self, paging_cmd='terminal length 0'):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        return self.send_command(paging_cmd)

    def telnet_connect(self):
        '''
        Establish telnet connection
        '''
        try:
            return telnetlib.Telnet(self.ip_addr, self.TELNET_PORT, self.TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")




if __name__ == "__main__":
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()
    device = TelnetCisco(ip_addr, username, password)
    output = device.send_command("sho ip int brief")
    print "\n\n"
    print output
    print "\n\n"

