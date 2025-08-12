import nmap

def scan(ip, port='22'):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, ports=port)
    if nm.all_hosts():
        print(f'Host encontrado! {ip}' )
        for host in nm.all_hosts():
            host_ip = host
            #host_state = nm[host_ip].state()
            #port_state = nm[host_ip]['tcp'][int(port)]['state']
            return host_ip
    else:
        print(f'Host não encontrado! IP: {ip}')
