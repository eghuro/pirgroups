import csv
import arrow

def log(data, file):
    utc = arrow.utcnow()
    local = utc.to('Europe/Prague')
    with open(file, 'a') as csvfile:
        writer = csv.writer(csvfile)
        for item in data:
            writer.writerow([item['jmeno'], item['pocet'],
                             item['zahajeni'], item['probihajici'],
                             local.format('YYYY-MM-DD')])
            yield item
