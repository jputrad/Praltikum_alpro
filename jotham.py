file1 = open("file1.txt")
file2 = open("file2.txt")

i = 1

while True:
    line1 = file1.readline()
    line2 = file2.readline()

    # berhenti kalau dua-duanya sudah habis
    if not line1 and not line2:
        break

    # hilangkan enter dan handle kalau salah satu kosong
    line1 = line1.strip() if line1 else "(kosong)"
    line2 = line2.strip() if line2 else "(kosong)"

    # bandingkan
    if line1 != line2:
        print("Baris ke-", i)
        print("File1:", line1)
        print("File2:", line2)
        print()

    i += 1

file1.close()
file2.close()