#!/usr/bin/python3
import time
import os.path

from jwcrypto.jwk import JWK, JWKSet

keyid = int(time.time())
keyset = JWKSet()
rsasig = JWK(generate='RSA', size=2048, use='sig',
             kid='%s-sig' % keyid)
keyset.add(rsasig)
rsasig = JWK(generate='RSA', size=2048, use='enc',
             kid='%s-enc' % keyid)
keyset.add(rsasig)

with open('/etc/ipsilon/openidc.key', 'w') as m:
    m.write(keyset.export())

