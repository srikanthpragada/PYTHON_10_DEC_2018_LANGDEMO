from bs4 import BeautifulSoup

file = open(r"e:\classroom\python\dec10\contacts.xml", "rt")
bs = BeautifulSoup(file.read(), 'xml')
file.close()

for c in bs.find_all("contact"):
    st = ""
    for n, v in c.attrs.items():
        st += f"{n}:{v}" + ","

    print(st.strip(","))
