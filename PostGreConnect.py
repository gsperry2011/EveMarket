from lxml import html  # Used to parse XML
import requests #used to service API request

itemtypeid1 = 34
itemtypeid2 = 35
regionid = 10000002

webpage = requests.get('http://api.eve-central.com/api/marketstat?typeid=%i&typeid=%i&regionlimit=%i' % (
itemtypeid1, itemtypeid2, regionid))

if webpage.status_code == 200:
    data = html.fromstring(webpage.content)
    for item in data.iter('type'):


        buy_dict = {node.tag: node.text for node in item.xpath("buy/*")}
        sell_dict = {node.tag: node.text for node in item.xpath("sell/*")}

        #Variables for output
        itemid = (item.get("id"))
        buymin = buy_dict['min']
        buymax = buy_dict['max']
        buymedian = buy_dict['median']
        buyvolume = buy_dict['volume']
        buyaverage = buy_dict['avg']

#Fail if api webpage unavaliable
else:
        print "Webpage unavaliable"
        Webpage.raise_for_status()


#############################################################################


import psycopg2

connection = psycopg2.connect(database='evemarketdata', user='postgres', password='black3car')

#open a cursor to perform DB operations
cursor = connection.cursor()

#create new table
cursor.execute("CREATE TABLE arkonor (itemid integer primary key, min integer, max integer, median integer, volume integer, average integer);")

#Insert row data into DB table
cursor.execute("""INSERT INTO arkonor (typeid, min, max, median, volume, average)
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
     ('itemid', 'buymin', 'buymax', 'buymedian', 'buyvolume', 'buyaverage'))


#Commits all changes does with cursor
#connection.commit()
