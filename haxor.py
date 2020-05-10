import random

teks = str(input('\nkata agan : '))
print('\n\n\033[91m Kata Kata Hacker Gaan \\/\033[32m')
alay = [' 🙂',' gan', ' gaaan','']
hasil= teks.split(' ')
for hitung, kata in enumerate(hasil):
  hasil[hitung] = kata+''+random.choice(alay)
print(*hasil)