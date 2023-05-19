import streamlit as riki
riki.title("Menghitung Luas dan Keliling Bujursangkar")
riki.write('Menghitung Luas Bujursangkar')

Sisi1 = riki.number_input ('Masukan Nilai Sisi 1', 0.)
Sisi2 = riki.number_input ('Masukan Nilai Sisi 2', 0.)
Luas = riki.button ('Hitung Luas Bujursangkar')

if Luas :
   luas = Sisi1 * Sisi2
   riki.write ('Luas Bujursangkar Adalah = ', luas, 'Betulll :)')
   riki.success (f'Luas Bujursangkar Adalah = {luas}')

riki.write('Menghitung Keliling Bujursangkar')
sisi1Keliling = riki.number_input ('Masukan Nilai Sisi', 0.)
Keliling = riki.button ('Hitung Keliling Bujursangkar')

if Keliling :
   keliling = sisi1Keliling * 4
   riki.write ('Keliling Bujursangkar Adalah = ', keliling, 'Betulll :)')
   riki.success (f'Keliling Bujursangkar Adalah = {keliling}')

#Lingkaran
riki.title('Menghitung Luas dan Keliling Lingkaran')
riki.write('Menghitung Luas Lingkaran')
ruji = riki.number_input('Masukan Nilai Jari-jari Lingkaran',0.)
luasLingkaram = riki.button('Hitung Luas Lingkaran')

if luasLingkaram :
   luaslingkaran = 3.14 * ruji * ruji
   riki.write('Luas Lingkaran Adalah = ', luaslingkaran,'Betulll:V')
   riki.success (f'Luas Lingkaran Adalah = {luaslingkaran}')
        
riki.write('Menghitung Keliling Lingkaran')
diameter = riki.number_input ('Masukan Nilai Diameter Lingkaran', 0.)
Diameter = riki.button('Hitung Keliling Lingkaran')

if Diameter :
   diameterLingkaran = 3.14 * diameter
   riki.write('Keliling Lingkaran Adalah = ', diameterLingkaran, 'Betulll :)')
   riki.success (f'Keliling Lingkaran Adalah = {diameterLingkaran}')

#Arus Listrik
riki.title('Menghitung Arus Listrik')
tegangan = riki.number_input('Masukan Nilai Tegangan', 0.)
resistor = riki.number_input('Masukam Nilai Resistor', 0.)
arus = riki.button('Hitung Arus Listrik')

if arus :
   Arus = tegangan / resistor
   riki.write('Arus Listrik Adalah = ', Arus, 'Betulll:v')
   riki.success (f'Arus Listrik Adalah = {Arus}')

#Kecepatan Rata-rata
riki.title('Menghitung Kecepatan Rata-rata')
jarak = riki.number_input('Masukkan Nilai Jarak', 0.)
waktu = riki.number_input('Masukkan Nilai Waktu', 0.)
Kecepatan = riki.button('Hitung Kecepatan Rata-rata')

if Kecepatan :
   kec = jarak / waktu
   riki.write('Kecepatan Rata-rata Adalah =', kec, 'Betulll :)')
   riki.success (f'Kecepatan Rata-rata Adalah = {kec}')
