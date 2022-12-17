import requests

file1 = open('dictionary.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
        url = 'http://google.com/'+line.strip()
        response = requests.get(url)
        if response.status_code == 200:
                print('Found adminpage!: ' + url)
                with open("working urls.txt", "w") as fp:
                        fp.writelines(url)
        else:
                print('Not working adminpage!: ' + url)

  
    
