
import nmap

class Network(object):
    def __init__(self):
        ip = input('Please enter IP: ')
        self.ip = ip

    def NetScanner(self):
        if len(self.ip) == 0:
            print('Please enter a valid IP')
        else:
            network = self.ip + '/24'

        print('Scanning please wait...')

        nam = nmap.PortScanner()
        nam.scan(hosts = network, arguments = '-sn')
        host_list = [(x, nam[x]['status']['status']) for x in nam.all_hosts()]
        for host, ststus in host_list:
            print(f'Host {host_list}')


if __name__ == '__main__':
    D = Network()
    D.NetScanner()
