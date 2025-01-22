import re
import time

# Fungsi untuk mengubah format dan menyimpan hasilnya
def convert_format(input_file, output_file):
    # Membaca data dari file 'data.txt'
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        print(f"File {input_file} berhasil dibaca.")
    except FileNotFoundError:
        print(f"File {input_file} tidak ditemukan.")
        return

    # Membuka file 'account.txt' untuk menulis hasil
    try:
        with open(output_file, 'w') as output_file:
            for line in lines:
                # Menghapus spasi ekstra di awal dan akhir baris
                line = line.strip()

                # Debug: Mencetak setiap baris yang sedang diproses
                print(f"Memproses baris: {line}")

                # Mengabaikan baris yang berisi token, private key, wallet address, atau points
                if re.search(r'(Token:|Wallet Private Key:|Wallet Address:|Points:)', line):
                    print(f"Baris diabaikan: {line}")
                    continue  # Skip baris ini dan lanjutkan ke baris berikutnya
                
                # Menentukan pola regex untuk menemukan email dan password dalam berbagai format
                email_password_match = re.match(r'.*Email:\s*(\S+@\S+\.\S+)\s*Password:\s*(\S+)', line)
                
                # Jika ditemukan email dan password dalam baris tersebut
                if email_password_match:
                    email = email_password_match.group(1)  # Menyimpan email
                    password = email_password_match.group(2)  # Menyimpan password
                    
                    # Menulis dalam format email,password ke file output
                    output_file.write(f'{email},{password}\n')  
                    
                    # Menambahkan delay untuk memisahkan proses lebih jelas
                    time.sleep(1)  # Delay selama 1 detik
                    
                    # Debug: Menampilkan hasil yang disimpan
                    print(f"Menulis ke file: {email},{password}")
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
