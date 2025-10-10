# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 10:27:06 2025

@author: Muh Zaky Maulana Haryanto
"""

ulang = "y"

while (ulang.lower() == "y"):
    print("=== Program Hitung Jumlah Hari ===")
    
    bulan = int(input("Masukkan bulan (1-12): "))
    tahun = int(input("Masukkan tahun: "))

    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        print("Jumlah hari: 31")
    elif bulan in [4, 6, 9, 11]:
        print("Jumlah hari: 30")
    elif bulan == 2:
        if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
            print("Jumlah hari: 29 (tahun kabisat)")
        else:
            print("Jumlah hari: 28")
    else:
        print("Input bulan tidak valid!")

    ulang = input("Ingin menghitung lagi? (y/n): ")

print("Program selesai.")
