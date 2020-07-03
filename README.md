#OfficeTrack-Miner  
Author: Mauricio Urrego  
Github User: Mauricio-Urrego  
www.github.com/Mauricio-Urrego/OfficeTrack-Scraper
_______________________________

For scraping data from OfficeTrack and preparing it for an sqlite database.

Backups of data are automatically created and date-time marked in the YYYYDDMM-HHMM format.

Data is automatically appended to staging table for transformation in db or excel.

Place repo in a github folder under parent folder user name. In this case user is "Aliece". Change all paths to reflect your system's username in the two paths and credentials files. The first file is located under "Scraper" and the second is located under "Scraper/Download".

Change officetrack user and password and company name also in the two path and credentials files.

Make sure to check over selenium scripts for any unnecessary commands different in production.

Lastly make sure to change paths in the three .bat files.

The three .bat files can be task scheduled. OfficeTrackYesterday.bat can be run in the morning followed by organizebackups.bat shortly afterwards. OfficetrackToday.bat can be run in the afternoon followed by organizebackups.bat shortly afterwards. Make sure to give at least 10-15 minutes between runs to ensure appropriate download is staged and ready to be manipulated.

Once both .bats are run then and only then can the excel odbc connection be refreshed.

The odbc connector is required for querying from sqlite database and reflecting changes in excel.

Excel formulas must also be updated to reflect new source.

Requires ODBC Connector for Excel transformations
Good open source option (download and github repo):
http://www.ch-werner.de/sqliteodbc/
https://github.com/softace/sqliteodbc

Dependencies and libraries:
Google Chrome
ChromeDriver
Python
sqlite3
pandas
selenium
odbc driver (for transformations)
Windows 10 Task Scheduler (or OS equivalent)

I recommend git and pip for source code and library management.
