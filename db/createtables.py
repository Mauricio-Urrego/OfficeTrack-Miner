#<OfficeTrack Web Scraper>
#Copyright (C) <2020>  <Mauricio Urrego>
#Full licensing in included License.txt file

import sqlite3

conn = sqlite3.connect(“HotwireOperations.db”)
curr = conn.cursor()

#create staging table
#cur.execute("DROP TABLE IF EXISTS officetrack_staging") #staging table can be dropped when connection is made between staging and more permanent table. This can be done at any time because of csv backups but for purposes of this conversation, omit dropping so that excel can do appropriate transformations perhaps through sql query.
curr.execute(“CREATE TABLE IF NOT EXISTS officetrack_staging (True_False text,Task_Number integer,task_type text,Customer text,Contractor text,Resources text,Description text,Start_Date text,Due_date text,Status text)”)

conn.commit()
conn.close()

#before conn close you can check table by running following
curr.execute("PRAGMA table_info('officetrack_staging')").fetchall()

#select all
curr.execute("SELECT * FROM officetrack_staging")
rows = curr.fetchall()
for row in rows:
    print(row)

#Examples below of relationship tables
-- projects table
CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY,
    name text NOT NULL,
    begin_date text,
    end_date text
);

-- tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY,
    name text NOT NULL,
    priority integer,
    project_id integer NOT NULL,
    status_id integer NOT NULL,
    begin_date text NOT NULL,
    end_date text NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
);
