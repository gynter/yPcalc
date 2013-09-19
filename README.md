------------------------------------------------------------------------
yPcalc - An IPv4 and IPv6 subnet calculator
========================================================================
------------------------------------------------------------------------

1.  Requirements
2.  Installation
3.  Usage
4.  License
5.  Support
6.  Authors

1. Requirements
---------------

- Python 2.7;
- Python `ipcalc` module.

2. Installation
---------------

- Download and install [ipcalc](https://pypi.python.org/pypi/ipcalc/)
Python module. I recommend to use the latest one from the
[GitHub](https://github.com/tehmaze/ipcalc/archive/master.zip) and
install it by running the setup script in command prompt:

        $ python setup.py install

- Download the latest release from 
<https://github.com/gynter/yPcalc/releases>
and extract the archive to the chosen destination directory.

    Development files can be browsed via web browser or can be optained 
    from a git repository <https://github.com/gynter/yPcalc>.

    *Note: You can also get the sources using the 
    [GIT](http://git-scm.com/book/en/Getting-Started-Installing-Git) and 
    cloning the `https://github.com/gynter/yPcalc.git` repository.*

- Install it by running the the setup script in command prompt:

        $ python setup.py install

*Note: You must have administrator/super user privileges
for the installation.*

3. Usage
--------

yPcalc is a command line software, therefore all actions are performed
in command prompt.

    $ ypcalc -h
    usage: ypcalc [-h] [-V] [-L] {show,check} ...

    yPcalc - An IPv4 and IPv6 subnet calculator.

    optional arguments:
      -h, --help     show this help message and exit
      -V, --version  show program's version number and exit
      -L, --license  show program's license end exit

    commands:
      {show,check}   see {command} -h for more help
        show         show the IP address information
        check        check if IP address exists in the network. Exits with code 1
                     if not found

It has two commands:

- `show` displays the information about the IP or network address;
- `check` performs a lookup to see if the IP address exists in the network.

See `ypcalc {command} -h` for command specific arguments.

IPv4 examples:
    
    $ ypcalc show 192.0.3.171/27
    Address:     192.0.3.171
    Netmask:     255.255.255.224 = 27
    Network:     192.0.3.160/27
    HostMin:     192.0.3.161
    HostMax:     192.0.3.190
    Broadcast:   192.0.3.191
    Hosts/Net:   32 CLASS C
    IPv6 repr:   2002:c000:03ab:0000:0000:0000:0000:0000
    PTR RR name: 171.3.0.192.in-addr.arpa
    IP version:  4

    $ ypcalc check 192.0.3.164 192.0.3.171/27
    ypcalc: info: IP 192.0.3.164 exists in network 192.0.3.171/27

    $ ypcalc check 192.0.3.192 192.0.3.171/27
    ypcalc: error: IP 192.0.3.192 does not exist in network 192.0.3.171/27


IPv6 examples:

    $ ypcalc show 2002:c000:022a::/29
    Address:     2002:c000:022a:0000:0000:0000:0000:0000
    Netmask:     ffff:fff8:0000:0000:0000:0000:0000:0000 = 29
    HostMin:     2002:c000:0000:0000:0000:0000:0000:0001
    HostMax:     2002:c007:ffff:ffff:ffff:ffff:ffff:fffe
    Hosts/Net:   633825300114114700748351602688 GEO-UNICAST
    IPv4 repr:   192.0.2.42
    PTR RR name: 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.a.2.2.0.0.0.0.c.2.0.0.2.ip6.arpa
    IP version:  6

    $ ypcalc check 2002:c006:022a:: 2002:c000:022a::/29
    ypcalc: info: IP 2002:c006:022a:: exists in network 2002:c000:022a::/29

    $ ypcalc check 2002:c009:022a:: 2002:c000:022a::/29
    ypcalc: error: IP 2002:c009:022a:: does not exist in network 2002:c000:022a::/29

When using `output filter` then only specific values are displayed,
without the caption prefix:

    $ ypcalc show --reverse --netmask 2002:c000:022a::/29
    ffff:fff8:0000:0000:0000:0000:0000:0000
    0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.a.2.2.0.0.0.0.c.2.0.0.2.ip6.arpa

The values are ordered as shown in `ypcalc show -h` regardless of the
sequence of the arguments.

4. License
----------

This software is licensed as described in the file `LICENSE.md`, which 
You should have received as part of this distribution. The terms are 
also available at 
<https://github.com/gynter/yPcalc/blob/master/LICENSE.md>.

5. Support
----------

Issue tracker can be found at 
<https://github.com/gynter/yPcalc/issues>.

6. Authors
----------

- Günter Kits (gynter@kits.ee)
