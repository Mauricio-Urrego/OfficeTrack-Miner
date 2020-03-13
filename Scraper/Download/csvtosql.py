#<OfficeTrack Web Scraper>
#Copyright (C) <2020>  <Mauricio Urrego>
#Full licensing in included License.txt file

import sqlite3
import pandas
from pathsforscripts import dbconnectionpath, csvfilepath

conn = sqlite3.connect(dbconnectionpath)
curr = conn.cursor()

csvpath = csvfilepath

df = pandas.read_csv(csvpath)
df.to_sql('officetrack_staging', conn, if_exists='append', index=False)

#after any execute
conn.commit()
conn.close()
