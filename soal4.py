dictionary_domain = dict()

fname = input("Masukkan nama file : ")

try:
    fhand = open(fname)
except:
    print("File tidak bisa dibuka")
    exit()

for line in fhand:
    words = line.split()

    if len(words) < 2 or words[0] != 'From':
        continue

    email = words[1]
    domain = email.split('@')[1]

    if domain not in dictionary_domain:
        dictionary_domain[domain] = 1
    else:
        dictionary_domain[domain] += 1

print(dictionary_domain)