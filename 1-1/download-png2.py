import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as file:
    file.write(mem)
    print("저장되었습니다...!")