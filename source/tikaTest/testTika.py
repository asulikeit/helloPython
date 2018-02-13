# -*- coding: utf-8 -*-
'''
Created on 2018. 2. 13.

@author: SDS
'''

import json
import tika
tika.TikaClientOnly = True
from tika import parser

if __name__ == '__main__':
    pass

# filename = "NLP-overview.pdf"
filename = "SCAN_spyns.pdf"
parsed = parser.from_file(filename, 'http://192.168.0.199:9998/tika')
content = json.dumps(parsed['content'])
print(content)