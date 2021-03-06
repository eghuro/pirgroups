import csv
import arrow
import json

utc = arrow.utcnow()
local = utc.to('Europe/Prague')

with open('current.json', 'r') as jsn:
    cur = json.loads(jsn.read())

for item in cur:
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([item, cur[item]['pocet'],
                         cur[item]['zahajeni'], cur[item]['probihajici'],
                         local.format('YYYY-MM-DD')])
