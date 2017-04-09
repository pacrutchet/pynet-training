import telnetlib
import socket
import sys
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main(ip_addr, username, password, cmd):
    try:
        remote_con = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("ERROR: connection timeout")
    output = remote_con.read_until("sername:", TELNET_TIMEOUT)
    remote_con.write(username + '\n')
    output += remote_con.read_until("assword:", TELNET_TIMEOUT)
    remote_con.write(password + '\n')
    cmd = cmd.rstrip()
    time.sleep(1)
    output += remote_con.read_very_eager()
    remote_con.write("terminal len 0" + '\n')
    time.sleep(1)
    output += remote_con.read_very_eager()
    print output
    remote_con.write(cmd + '\n')
    time.sleep(1)
    output = remote_con.read_very_eager()
    print output
    remote_con.close()
    return output


if __name__ == "__main__":
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    cmd = sys.argv[1]
    main(ip_addr, username, password, cmd)

