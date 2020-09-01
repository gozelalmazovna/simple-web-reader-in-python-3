#import url library
import urllib.request , urllib.parse , urllib.error
#import regular expressions library
import re
#open url
fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in fhand:
    #decode UTF-8 to UNICODE and print every line
    print(line.decode().strip())
    #Search for links in HTML file
    new_link = re.findall('href="(.+)"', line.decode())
    #If no links continue
    if len(new_link) < 1: continue
    #If link was found proceed to opening and printing new HTML file
    fhand1 = urllib.request.urlopen(new_link[0])
    for line in fhand1:
        print(line.decode().strip())
