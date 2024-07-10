def inputan(nim,nama):
    return nim,nama

data = inputan(input())
while True:
    kondisi = str(input('ingin tambah lagi? ya/tidak')).lower()
    if kondisi == 'ya':
        input()
    else:
        print(data(input))

