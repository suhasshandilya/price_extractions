from bs4 import BeautifulSoup
import webbrowser
import urllib2
# Get the product search query from user and parse the page source of the search result from flipkart website
product = raw_input("Enter product name: ")
product = product.replace(' ', '+')
print "entering search"
content1 = urllib2.urlopen('http://www.flipkart.com/search?otracker=start&q='+product).read()
print "Finished search"
content2= urllib2.urlopen('http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='+product).read()
print "finished amazon search"
3content3= urllib2.urlopen('http://www.snapdeal.com/search?keyword='+product).read()
print "Done with snapdeal search"
soupf = BeautifulSoup(content1)
soupa = BeautifulSoup(content2)
soups = BeautifulSoup(content3)

# Parse the page source of the matched product and find the seller-name
link = soupf.find_all("div", class_="pu-title fk-font-13")[0].find_all('a')[0].get('href')
link = "https://www.flipkart.com%s" % link
qseller_info = urllib2.urlopen(link).read()
link_soup = BeautifulSoup(seller_info)
price = link_soup.find_all("span", class_="selling-price omniture-field")[0].string.strip()
print price

#parse Amazon's source
link2 = soupa.find_all("div",class_="a-row a-spacing-mini")[0].find_all('a')[0].get('href')
link2= "https://www.amazon.in%s" % link2
print "XYZ"
seller2_info = urllib2.urlopen(link2).read()
print "123"
link2_soup = BeautifulSoup(seller2_info)
#print link2_soup
price2 = link2_soup.find_all("span", class_="a-size-medium a-color-price")[0].string.strip(),link2_soup.find_all(class_="a-link-normal s-access-detail-page a-text-normal")[0].string.strip()
print price2

#parse snapdeal's source
#link3 = soups.find_all("div", class_="comp comp-header reset-padding")[0].find_all('a')[0].get('href')
#ink3 = "https://www.snapdeal.com%s" %link3
#seller3_info = urllib2.urlopen(link3).read()
#link3_soup = BeautifulSoup(seller3_info) 
#price3 = link3_soup.find_al("span", class_="accountBtn rippleWhite")[0].string.strip()
#print price3

#to sort the prices
sort = sorted(price1,price2)
print sort[0]
