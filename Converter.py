import xml.etree.cElementTree as e


def createXML(response):
    count = 0
    for key in response:
        count += 1
        r = e.Element("Employee")
        e.SubElement(r, "id").text = str(key["id"])
        e.SubElement(r, "name").text = key["name"]
        e.SubElement(r, "username").text = key["username"]
        e.SubElement(r, "email").text = key["email"]
        e.SubElement(r, "phone").text = key["phone"]
        e.SubElement(r, "website").text = key["website"]
        Address = e.SubElement(r, "address")
        e.SubElement(Address, "Street").text = str(key["address"]["street"])
        e.SubElement(Address, "Suite").text = str(key["address"]["suite"])
        e.SubElement(Address, "City").text = str(key["address"]["city"])
        e.SubElement(Address, "Zipcode").text = str(key["address"]["zipcode"])
        Geo = e.SubElement(Address, "geo")
        e.SubElement(Geo, "Latitude").text = str(key["address"]["geo"]["lat"])
        e.SubElement(Geo, "Longitude").text = str(key["address"]["geo"]["lng"])
        Company = e.SubElement(r, "company")
        e.SubElement(Company, "Name").text = key["company"]["name"]
        e.SubElement(Company, "Slogan").text = key["company"]["catchPhrase"]
        e.SubElement(Company, "Job").text = key["company"]["bs"]
        xml = e.ElementTree(r)
        # ct = datetime.datetime.now().isoformat()
        # name = 'employee_'+str(ct)+'.xml'
        name = 'd:\\xmls\\employee_' + str(count) + '.xml'
        xml.write(name)
