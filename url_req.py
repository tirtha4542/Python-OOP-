from urllib.request import urlopen
url = ""
obj  = urlopen(url)
data = obj.read()

image = open("image1.jpg",'wb')
image.write(data)
image.close()