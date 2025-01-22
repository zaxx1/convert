import re

# Fungsi untuk mengubah format dan menyimpan hasilnya
def convert_format(input_file, output_file):
    # Membaca data dari file 'data.txt'
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {input_file} tidak ditemukan.")
        return

    # Membuka file 'account.txt' untuk menulis hasil
    try:
        with open(output_file, 'w') as output_file:
            for line in lines:
                # Menghapus spasi ekstra di awal dan akhir baris
                line = line.strip()
                
                # Menentukan pola untuk menemukan email dan password
                # Pola ini mencoba menemukan email dan password yang dipisahkan oleh spasi atau karakter lain
                match = re.match(r'(\S+@\S+\.\S+)\s+(\S+)', line)
                
                if match:
                    email = match.group(1)  # Menyimpan bagian email
                    password = match.group(2)  # Menyimpan bagian password
                    output_file.write(f'{email},{password}\n')  # Menulis dalam format email,password
                else:
                    print(f"Tidak dapat memproses baris: {line}")
            print(f"Proses selesai. Hasil disimpan di {output_file.name}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menulis ke file: {e}")

# Menentukan nama file input dan output
input_file = 'data.txt'
output_file = 'account.txt'

# Memanggil fungsi untuk mengubah format dan menyimpan hasilnya
convert_format(input_file, output_file)
