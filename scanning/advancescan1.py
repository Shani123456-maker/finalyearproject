from socket import * #from socket import every thing
import optparse  #help us to prompt help options to the users
from threading import * # the code is going to be threaded
from termcolor import colored # importing colors for print commands

def scan(target_host, target_port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((target_host, target_port))
        print(colored('[+] %d/tcp port is open ' % target_port, 'green'))
    except:
        print(colored('[-] %d/tcp port is close ' % target_port,'red'))
    finally:
        s.close()

def scanner(target_host,target_ports):

    try:
        target_ip = gethostbyname(target_host)
        print('The Ip Address of the Host is %s ' % target_ip)

    except:
        print('Unknown host %s' %target_host)
        exit()

    try:
        target_name= gethostbyaddr(target_ip)
        print ('[+] Scan Results for ' + target_name[0])
    except:
        print ('[+] Scan Results for ' + target_ip)
    setdefaulttimeout(1)
    for target_port in target_ports:
        t = Thread(target=scan, args=(target_host, int(target_port)))
        t.start()

def main():
    parser= optparse.OptionParser('Usage of scanner: ' '-H <target host> -p <target port>') # prompts the message of how to use the scanner
    parser.add_option('-Z', dest='target_host', type = 'string', help='Specify the target host')
    parser.add_option('-p', dest='target_port', type = 'string', help='Specify the target ports seperated by commas (,)')
    (options, args) = parser.parse_args()
    target_host=options.target_host
    target_ports=str(options.target_port).split(',')

    if(target_host==None) | (target_ports[0]==None):
        print (parser.usage)
        exit(0)
    scanner(target_host,target_ports)

if __name__ == "__main__":
    main()
