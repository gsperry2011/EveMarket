def LXMLScraper(itemtypeid1, itemtypeid2, regionid):
    from lxml import html  # Used to parse XML
    import requests

    itemtypeid1 = 34
    itemtypeid2 = 35
    regionid = 10000002

    webpage = requests.get('http://api.eve-central.com/api/marketstat?typeid=%i&typeid=%i&regionlimit=%i' % (
    itemtypeid1, itemtypeid2, regionid))

    if webpage.status_code == 200:
        data = html.fromstring(webpage.content)
        for item in data.iter('type'):

            # print node attribute id value.
            itemid = (item.get("id"))
            print(itemid)

            buy_dict = {node.tag: node.text for node in item.xpath("buy/*")}
            sell_dict = {node.tag: node.text for node in item.xpath("sell/*")}

            print buy_dict
            print sell_dict

    #Fail if page unavaliable
    else:
            print "Webpage unavaliable"
            Webpage.raise_for_status()
