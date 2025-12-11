# Praktikum-Teori-Graf-2025

| Name           | NRP        | Kelas     |
| ---            | ---        | ----------|
| Aloysius deDeo Darmo Susanto | 5025221174 | D |
| Bima Novrifa Ananditya | 5025241194 | D |
| Syah Amin Zikri | 5025241197 | D |

## Praktikum 1 (Knigh's Tour)

Program ini menyelesaikan Knight’s Tour pada papan 8×8 dengan Algoritma Warnsdorff.
User dapat memilih titik awal dan program menghasilkan:
  - Papan hasil tour (angka 1–64)
  - Jenis tour → OPEN atau CLOSED
  - Visualisasi lintasan dalam bentuk gambar

### Cara Menjalankan Program
1. Install Python3 jika belum punya 
2. Install library matplotlib :
```
pip install matplotlib
```
3. Jalankan program

### Cara Penggunaan Program
Setelah program berjalan, pengguna akan diminta memasukkan:
  - Start X (0–7) → posisi kolom awal kuda
  - Start Y (0–7) → posisi baris awal kuda

### Output Program
1. Papan Knight’s Tour
Program menampilkan papan 8×8 berisi angka 1–64, di mana:
  - 1 = posisi langkah pertama
  - 64 = posisi langkah terakhir
urutan angka menunjukkan lintasan kuda

2. Status Tour
Program menentukan jenis tour:
`OPEN TOUR` → langkah terakhir tidak kembali ke posisi awal
`CLOSED TOUR` → langkah terakhir dapat loncat kembali ke posisi awal

## Praktikum 2
