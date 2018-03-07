# -*- coding: utf-8 -*-  
"""
    :copyright: ©2018 by IPIP.net
"""

import os

from .util import bytes2long, ip2long, convert, verify_ipv4

class District:
    data = b""
    indexSize = 0

    def __init__(self, name):
        file = open(name, "rb")
        self.data = file.read()
        file.close()
        self.indexSize = bytes2long(self.data[0], self.data[1], self.data[2], self.data[3])

    def find(self, ip):
        if verify_ipv4(ip):
            return False

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