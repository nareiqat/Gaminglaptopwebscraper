# it grab the html content
from urllib.request import urlopen as uReq
 
# It parse the html text
from bs4 import BeautifulSoup as soup
 
my_url = 'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=3&Category=363'
 
# Opening the connection and grabbing the page
uClient = uReq(my_url)
 
# store as read, coz it will dump after read
page_html = uClient.read()
 
# close connection
uClient.close()
 
# html parser
page_soup = soup(page_html, "html.parser")
 
# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})
 
filename = "products.csv"
 
f = open(filename, "w")
 
headers = "product_brand, product_name,product_price, product_shipping\n"
 
f.write(headers)
 
for container in containers:
    
    try:
        product_brand = container.find("div", "item-info").div.a.img["title"]
    except Exception as e:
        product_brand = "NA"
    else:
        pass
    finally:
        pass
 
    title_container = container.findAll("a", {"class": "item-title"})
 
    product_name = title_container[0].text
 
    shipping_container = container.findAll("li", {"class": "price-ship"})
 
    product_shipping = shipping_container[0].text.strip()

    price_container  = container.findAll("li", {"class":"price-current"})
 
    price = price_container[0].text.strip()

    # print("product_brand: " + product_brand)
    # print("product_name: " + product_name)
    # print("product_shipping: " + product_shipping)
 
    # replace "," in product name with "|"
    f.write(product_name.replace(",", "|") + "," + product_brand + "," + price + ","+ product_shipping + "\n")
     
f.close()