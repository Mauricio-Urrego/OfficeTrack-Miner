#<OfficeTrack Web Scraper>
#Copyright (C) <2020>  <Mauricio Urrego>
#Full licensing in included License.txt file

import os
import pandas as pd
from pathsforscripts import htmlfilepath

htmlname = htmlfilepath
html = open(htmlname, 'r')
source_code = html.read()
tables = pd.read_html(source_code)

for i, table in enumerate(tables):
    table.to_csv('test{}.csv'.format(i),',')
