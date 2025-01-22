import re

# Membaca data dari file 'data.txt'
with open('data.txt', 'r') as file:
    lines = file.readlines()

# Membuka file 'account.txt' untuk menulis hasil
with open('account.txt', 'w') as output_file:
    for line in lines:
        # Menentukan pola untuk menemukan email dan password
        match = re.match(r'(\S+)@(\S+)\s+(\S+)', line.strip())
        if match:
            email = match.group(0)  # Menyusun email
            password = match.group(3)  # Menyusun password
            output_file.write(f'{email},{password}\n')  # Menyimpan hasil dalam format email,password
