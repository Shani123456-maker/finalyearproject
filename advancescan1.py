from socket import * #from socket import every thing
import optparse  #help us to prompt help options to the users
from threading import * # the code is going to be threaded

def main():
    parser= optparse.OptionParser('Usage of scanner: ' '-H <target host> -p <target port>') # prompts the message of how to use the scanner
    parser.add_option('-H', dest='target_host', type = 'string', help='Specify the target host')
    parser.add_option('-p', dest='target_port', type = 'string', help='Specify the target ports seperated by commas (,)')
    (options, args) = parser.parse_args()
    target_host=options.target_host
    target_port=str(options.target_port).split(',')

    if(target_host==None) | (target_port[0]==None):
        print (parser.usage)
        exit(0)

if __name__ == "__main__":
    main()
