import nmap
from util.loggin import log_info, log_error

def scan(ip, port='22'):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, ports=port)
    if nm.all_hosts():
        log_info(f"Host encontrado: {ip}")
        for host in nm.all_hosts():
            return host
    else:
        log_error(f"Host não encontrado: IP {ip}")
