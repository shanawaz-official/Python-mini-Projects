import pyshorteners as pyshrt

url=input("Enter URL:-")
shrt=pyshrt.Shortener()
shrturl=shrt.tinyurl.short(url)

print(shrtur)