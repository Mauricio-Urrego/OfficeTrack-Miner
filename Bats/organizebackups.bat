copy C:\Users\Aliece\github\OfficeTrack-Scraper\Scraper\Download\Data.doc "C:\Users\Aliece\github\OfficeTrack-Scraper\Scraper\Download\data.html"

cd C:\Users\Aliece\github\OfficeTrack-Scraper\Scraper\Download\

python C:\Users\Aliece\github\OfficeTrack-Scraper\Scraper\Download\htmltocsv.py

copy test0.csv "C:\Users\Aliece\github\OfficeTrack-Scraper\db\csvbackups\otdata-%date:~10,4%%date:~7,2%%date:~4,2%-%time:~0,2%%time:~3,2%.csv"

python C:\Users\Aliece\github\OfficeTrack-Scraper\Scraper\Download\csvtosql.py
