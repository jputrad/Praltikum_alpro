filename = input("nama file: ")
handle = open(filename)

for line in handle:
    parts = line.strip().split("||")

    # skip kalau format salah
    if len(parts) < 2:
        continue

    soal = parts[0].strip()
    jawaban_benar = parts[1].strip().lower()

    print(soal)
    jawab = input("Jawab: ").lower()

    if jawab == jawaban_benar:
        print("Jawaban benar!\n")
    else:
        print("Jawaban salah!\n")

handle.close()