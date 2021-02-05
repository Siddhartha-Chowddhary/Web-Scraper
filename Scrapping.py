import requests
from bs4 import BeautifulSoup


result = requests.get("https://www.medicines.org.uk/emc/browse-medicines/")
print(result.status_code)
print(result.headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all("a")
print(links)
print("\n")

FILE_TYPE = '.pdf'
Number = int(0)


# for link in links:
#     if "SmPC" in link.text:
#         # print(link.attrs['href'])
#         Source = requests.get(f"https://www.medicines.org.uk{link.attrs['href']}")
#         print(f"https://www.medicines.org.uk{link.attrs['href']}")



for link in links:
    if "SmPC" in link.text:
        Number += 1
        # print(link.attrs['href'])
        Source = requests.get(f"https://www.medicines.org.uk{link.attrs['href']}").text
        # print(f"https://www.medicines.org.uk{link.attrs['href']}")
        soup = BeautifulSoup(Source, 'lxml')
        divs = soup.findAll("div", {"class": "smpc"})

        with open(f"./SMPC/MED_{Number}.txt", "w", encoding="utf-8") as f:
            for i in divs:
                f.write(i.text) 
                f.close()

            
Number = int(0)
for link in links:
    if "Patient Leaflet" in link.text:
        Number += 1
        # print(link.attrs['href'])
        PIL_Source = requests.get(f"https://www.medicines.org.uk{link.attrs['href']}").text
        PIL_soup = BeautifulSoup(PIL_Source, 'lxml')
        a = PIL_soup.findAll("a", {"class": "download"})
        
#         for i in a:
#             PIL_PDF_Source = requests.get(f"https://www.medicines.org.uk{i.attrs['href']}")
# #                 PIL_PDF_soup = BeautifulSoup(PIL_PDF_Source, 'lxml')
#             print(PIL_PDF_Source.content)
        with open(f"./PIL/MED_{Number}.pdf", "wb") as f:
            for i in a:
                PIL_PDF_Source = requests.get(f"https://www.medicines.org.uk{i.attrs['href']}")
#                 PIL_PDF_soup = BeautifulSoup(PIL_PDF_Source, 'lxml')
                f.write(PIL_PDF_Source.content) 
                f.close()

#         for i in a:
#             print(i.text)
            
            