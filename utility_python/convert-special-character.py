# sample code for quote example
from urllib.parse import quote

bu=["R&D","Beauty and Beast","Product & Templates"]
for x in bu:
  print(x +"=>" +quote(x))