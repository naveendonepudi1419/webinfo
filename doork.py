import socket
import os
import requests
import platform

def back():
    print()
    back = input('\033[92mDo you want to continue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        iseeverything()
    elif back[0].upper() == 'N':
        print('\033[92mRemember https://github.com/naveendonepudi1419')
        exit
    else:
        print('\033[92m?')
        exit

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def bill():
    clear()
    print("""\033[92m                                
             _     _        __       
__      _____| |__ (_)_ __  / _| ___  
\ \ /\ / / _ \ '_ \| | '_ \| |_ / _ \ 
 \ V  V /  __/ |_) | | | | |  _| (_) |
  \_/\_/ \___|_.__/|_|_| |_|_|  \___/ 
                                      

 Information Gathering tool for a Website or IP address""")
    print()

def banner():
    print("""\033[92m
 1) DNS Lookup                 12) Host DNS Finder
 2) Whois Lookup               13) Reserve IP Lookup
 3) GeoIP Lookup               14)Host Info Scanner (use WhatWeb)
 4) Subnet Lookup              15) About webinfo
 5) Port Scanner               16) Exit Out Of Here
 6) Page Links                 
                               
 7) HTTP Header                
 8) Host Finder                
 9) IP-Locator                  
 10) Find Shared DNS Servers
 11) Get naveen.txt""")
    print()

def iseeverything():
    try:
        what = input('\033[92mDo you want to collect information of a website or IP address? [website/IP]: ')
        if what[0].upper() == 'W':
            victim = input('Enter the website address: ')
            banner()
        elif what[0].upper() == 'I':
            victim = input('Enter the IP address (or domain to get IP address of that domain): ')
            victim = socket.gethostbyname(victim)
            print('The IP address of target is:',victim)
            banner()
        else:
            print('?')
            iseeverything()

        choose = input('What information would you like to collect? (1-20): ')

        if choose == '1':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+victim
            info = requests.get(dnslook)
            print('\033[91m',info.text)
            back()

        elif choose == '2':
            whois = 'https://api.hackertarget.com/whois/?q='+victim
            info = requests.get(whois)
            print('\033[91m',info.text)
            back()

        elif choose == '3':
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+victim
            info = requests.get(ipgeo)
            print('\033[91m',info.text)
            back()

        elif choose == '4':
            subnet = 'http://api.hackertarget.com/subnetcalc/?q='+victim
            info = requests.get(subnet)
            print('\033[91m',info.text)
            back()

        elif choose == '5':
            port = 'https://api.hackertarget.com/nmap/?q='+victim
            info = requests.get(port)
            print('\033[91m',info.text)
            back()

        elif choose == '6':
            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+victim
            info = requests.get(pagelink)
            print('\033[91m',info.text)
            back()


        elif choose == '7':
            header = 'https://api.hackertarget.com/httpheaders/?q='+victim
            info = requests.get(header)
            print('\033[91m',info.text)
            back()

        elif choose == '8':
            host = 'https://api.hackertarget.com/hostsearch/?q='+victim
            info = requests.get(host)
            print('\033[91m',info.text)
            back()

        elif choose == '9':
            iplt = 'https://ipinfo.io/'+victim+'/json'
            info = requests.get(iplt)
            print('\033[91m',info.text)
            back()

        elif choose == '10':
            shared = 'https://api.hackertarget.com/findshareddns/?q='+victim
            info = requests.get(shared)
            print('\033[91m',info.text)
            back()

        elif choose == '11':
            robots ='http://'+victim+'/robots.txt'
            info = requests.get(naveen)
            print('\033[91m',info.text)
            back()

        elif choose == '12':
            hostdns = 'https://api.hackertarget.com/mtr/?q='+victim
            info = requests.get(hostdns)
            print('\033[91m',info.text)
            back()

        elif choose == '13':
            reserve = 'https://api.hackertarget.com/reverseiplookup/?q='+victim
            info = requests.get(reserve)
            print('\033[91m',info.text)
            back()


        elif choose == '14':
            clear()
            os.system('whatweb -v '+victim)
            back()

        elif choose == '15':
            print("""\033[webinfo 1 - Information Gathering of a Website or IP address

AUTHOR: https://github.com/naveendonepudi1419
        https://twitter.com/DonepudiNaveen""")
            back()

        elif choose == '16':
            exit

        else:
            print('?')
            iseeverything()
            
    except socket.gaierror:
        print('Name or service unknown!\033[93m')
        print()
        iseeverything()
    except UnboundLocalError:
        print('The information you entered is incorrect')
        print()
        iseeverything()
    except requests.exceptions.ConnectionError:
        print('Your Internet Offline')
        exit
    except IndexError:
        print('?')
        print()
        iseeverything()

bill()
iseeverything()
