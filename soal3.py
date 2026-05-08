dictionary_email = dict()

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

    if email not in dictionary_email:
        dictionary_email[email] = 1
    else:
        dictionary_email[email] += 1

print(dictionary_email)