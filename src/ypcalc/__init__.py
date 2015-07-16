#!/usr/bin/env python
# -*- coding: utf-8 -*-
__LICENSE__ = """
yPcalc - An IPv4 and IPv6 subnet calculator.

Copyright (c) 2013 Günter Kits

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation files 
(the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS 
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN 
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""

import sys
from os.path import basename
from copy import copy
import argparse

__PROGRAM__ = "yPcalc"
__VERSION__ = "1.0.0"
__DESCRIPTION__ = "An IPv4 and IPv6 subnet calculator."
__EXECUTABLE__ = basename(sys.argv[0])


def exit(msg='', code=0):
    if msg:
        if code:
            print >>sys.stderr, "%s: error: %s" % (__EXECUTABLE__, msg)
        else:
            print "%s: info: %s" % (__EXECUTABLE__, msg)
    sys.exit(code)


try:
    from ipcalc import IP, Network
except ImportError:
    exit("failed to load ipcalc module, please see the documentation", 1)


class LicenseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print __LICENSE__
        exit(code=1)


def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def get_network(network_addr):
    if not network_addr:
        print exit("no network IP address defined", 1)
    try:
        return Network(network_addr)
    except ValueError as e:
        print exit(e, 1)

def repr_addr(addr, args):
    if args.bin:
        addr = addr.bin()
        if len(addr) == 32 and not args.nosep:
            addr = '.'.join(split_len(addr, 8))
        elif len(addr) == 128 and not args.nosep:
            addr = '.'.join(split_len(addr, 16))
    elif args.hex:
        addr = addr.hex()
        if len(addr) == 8 and not args.nosep:
            addr = ':'.join(split_len(addr, 2))
        elif len(addr) == 32 and not args.nosep:
            addr = ':'.join(split_len(addr, 4))
    return addr

def _(caption, value, args, short=False, addr=False):
    raddr = ""
    if addr:
        if isinstance(addr, bool):
            raddr = repr_addr(value, args)
        else:
            raddr = repr_addr(addr, args)
    if short:
        return raddr if addr else value
    if caption:
        caption = ':'.join([caption, ''])
        if args.bin or args.hex:
            return "%s%s%s" % (caption.ljust(13), str(value).ljust(50),
                               raddr)
        return "%s%s" % (caption.ljust(13), str(value))

def command_show(args):
    fields = ['address', 'netmask', 'network', 'min', 'max', 'broadcast',
              'hosts', 'info', 'ipv4', 'ipv6', 'reverse', 'ipversion']

    n = get_network(args.netaddr)
    short = any(args.__dict__.get(x, False) for x in fields)

    filters = [
        ('Address', n, IP(str(n)), 0),
        ('Netmask', "%s = %s" % (n.netmask(), n.mask), n.netmask(), 0),
        ('Network', "%s/%s" % (n.network(), n.mask), n.network(), 0),
        ('HostMin', n.host_first(), True, 0),
        ('HostMax', n.host_last(), True, 0),
        ('Broadcast', n.broadcast(), True, 4),
        ('Hosts/Net', n.size() if short else "%s %s" % (n.size(), n.info()), False, 0),
        ('', n.info(), False, 0),
        ('IPv4 repr', n.to_ipv4(), True, 6),
        ('IPv6 repr', n.to_ipv6(args.type), True, 4),
        ('PTR RR name', n.to_reverse(), False, 0),
        ('IP version', n.version(), False, 0)
    ]

    for idx, f in enumerate(fields):
        d = filters[idx]
        o = _(d[0], d[1], args, short, d[2])
        if o and ((n.version() == d[3]) or not d[3]) and (args.__dict__.get(f, False) and short or not short):
            print o

def command_check(args):
    network = get_network(args.netaddr)
    # ipcalc module seems to have a bug/feature somewhere, so we need
    # to get the real network, where the netaddr resides.
    network = get_network("%s/%s" % (network.network(), network.mask))
    try:
        if network.has_key(args.addr):
            exit("IP %s exists in network %s" % (args.addr, args.netaddr))
    except ValueError as e:
        print exit(e, 1)
    exit("IP %s does not exist in network %s" % (args.addr, args.netaddr), 1)


def run():
    parser_desc = "%s - %s" % (__PROGRAM__, __DESCRIPTION__)

    # Main arguments.
    p_ap = argparse.ArgumentParser(add_help=False)
    p_ap.add_argument('-V', '--version', action='version',
                      version='%s %s' % (__PROGRAM__, __VERSION__,))
    p_ap.add_argument('-L', '--license', action=LicenseAction, nargs=0,
                      help="show program's license end exit")

    # Main parser.
    p = argparse.ArgumentParser(description=parser_desc, parents=[p_ap])

    # Common arguments for commands.
    c_ap = argparse.ArgumentParser(add_help=False)
    c_ap_g = c_ap.add_argument_group(title='output representation',
                                     description='display the IP \
addresses in different format')
    c_ap_g.add_argument('--bin', action='store_true', default=False,
                        help='binary representation of the IP addresses')
    c_ap_g.add_argument('--hex', action='store_true', default=False,
                        help='hexadecimal representation of the IP \
addresses')
    c_ap_g.add_argument('--nosep', action='store_true', default=False,
                   help='do not add separator (dot for IPv4 and colon \
for IPv6) when displayng the address in different representation')

    # Sub-parsers/commands.
    sp = p.add_subparsers(title='commands', help='see {command} -h for \
more help')
    
    # Show command and arguments.
    desc = "show the IP address information"
    c = sp.add_parser('show', parents=[p_ap, c_ap], description=desc,
                      help=desc)
    a = c.add_argument_group(title='output filter',
                             description='show only certain short info, \
ordered as defined below')
    a.add_argument('--address', action='store_true', default=False,
                   help='show IP address')
    a.add_argument('--netmask', action='store_true', default=False,
                   help='show network mask address')
    a.add_argument('--network', action='store_true', default=False,
                   help='show network address (IPv4 only)')
    a.add_argument('--min', action='store_true', default=False,
                   help='show the first useable IP address of the network')
    a.add_argument('--max', action='store_true', default=False,
                   help='show the last useable IP address of the network')
    a.add_argument('--broadcast', action='store_true', default=False,
                   help='show broadcast address (IPv4 only)')
    a.add_argument('--hosts', action='store_true', default=False,
                   help='show the count of the hosts in network')
    a.add_argument('--info', action='store_true', default=False,
                   help='show IANA allocation information for the IP \
address')
    a.add_argument('--ipv4', action='store_true', default=False,
                   help='show the IPv4 IP address representation of an \
IPv6 address. Works for IPv4-compat, IPv4-mapped, and 6-to-4 addresses')
    a.add_argument('--ipv6', action='store_true', default=False,
                   help='show the IPv6 IP address representation an IPv4 \
address. See --type option.')
    a.add_argument('--reverse', action='store_true', default=False,
                   help='show the DNS RR name field of PTR record')
    c.add_argument('netaddr', metavar='netaddr', action='store',
                        help='an IP address or a network (with IP or CIDR \
netmask)')
    a.add_argument('--ipversion', action='store_true', default=False,
                   help='show the IP version')
    c.add_argument('--type', action='store', default='6-to-4',
                   choices=['6-to-4', 'compat', 'mapped'],
                   help='address type for IPv6 representation \
(default: 6-to-4)')
    c.set_defaults(func=command_show)

    # Check command and arguments.
    desc = "check if IP address exists in the network. Exits with code \
1 if not found"
    c = sp.add_parser('check', parents=[p_ap], description=desc,
                      help=desc)
    c.add_argument('addr', metavar='addr', action='store',
                   help='an IP address')
    c.add_argument('netaddr', metavar='netaddr', action='store', 
                   help='a network (with IP or CIDR netmask)')
    c.set_defaults(func=command_check)

    # Parse the arguments and call the command.
    args = p.parse_args()
    if args.func:
        args.func(args)

if __name__ == '__main__':
    run()
