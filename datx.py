# -*- coding: utf-8 -*-  
"""
    :copyright: ©2018 by IPIP.net
"""

import struct
import os
import ipaddress

_unpack_V = lambda b: struct.unpack("<L", b)
_unpack_N = lambda b: struct.unpack(">L", b)
_unpack_C = lambda b: struct.unpack("B", b)

def bytes2long(a, b, c, d):
    return a << 24 | b << 16 | c << 8 | d

class City:
    
    data = b""
    indexSize = 0

    def __init__(self, name):
        file = open(name, "rb")
        self.data = file.read()
        file.close()
        self.indexSize = bytes2long(self.data[0], self.data[1], self.data[2], self.data[3])

    def find(self, ip):
        
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            return None

        low = 0
        mid = 0
        high = int((self.indexSize - 262144 - 262148) / 9) - 1
        pos = 0

        ips = ip.split(".")
        val = bytes2long(int(ips[0]), int(ips[1]), int(ips[2]), int(ips[3]))

        while (low <= high):
            mid = int((low + high) / 2)
            pos = mid * 9 + 262148
            start = 0
            if mid > 0 :
                pos1 = (mid - 1) * 9 + 262148
                start = self.data[pos1] << 24 | self.data[pos1+1] << 16 | self.data[pos1+2] << 8 | self.data[pos1+3]
                start = start + 1

            end = bytes2long(self.data[pos], self.data[pos+1], self.data[pos+2], self.data[pos+3])

            if val < start :
                high = mid - 1
            elif val > end:
                low = mid + 1
            else:
                b = 0;
                off = bytes2long(b, self.data[pos+6],self.data[pos+5],self.data[pos+4]);
                l = bytes2long(b, b, self.data[pos+7], self.data[pos+8]);

                pos = off - 262144 + self.indexSize;

                tmp = (self.data[pos:pos+l]).decode("utf-8")

                return tmp.split("\t")


def ip2long(ip):
    a = ip.split(".")
    return bytes2long(
        int(a[0]),
        int(a[1]),
        int(a[2]),
        int(a[3])
    )

class District:
    data = b""
    indexSize = 0

    def __init__(self, name):
        file = open(name, "rb")
        self.data = file.read()
        file.close()
        self.indexSize = bytes2long(self.data[0], self.data[1], self.data[2], self.data[3])

    def find(self, ip):
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            return None

        val = ip2long(ip)
        low = 0
        mid = 0
        pos = 0
        high = int((self.indexSize - 262148 - 262144) / 13) - 1
        
        while (low <= high) :
            mid = int((low + high) / 2)
            pos = mid * 13 + 262148

            start = bytes2long(
                self.data[pos],
                self.data[pos + 1],
                self.data[pos + 2],
                self.data[pos + 3]
            )

            end = bytes2long(
                self.data[pos + 4],
                self.data[pos + 5],
                self.data[pos + 6],
                self.data[pos + 7]
            )

            if val > end :
                low = mid + 1
            elif val < start:
                high = mid - 1
            else:
                off = bytes2long(
                    self.data[pos + 11],
                    self.data[pos + 10],
                    self.data[pos + 9],
                    self.data[pos + 8]
                )
                l = int(self.data[pos + 12])

                pos = off - 262144 + self.indexSize
                tmp = (self.data[pos:pos+l]).decode("utf-8")

                return tmp.split("\t")

class BaseStation(District):
    pass         