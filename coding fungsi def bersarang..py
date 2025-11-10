# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:01:50 2025

@author: Muhammad Zaky Maulana Haryanto
"""

def run_ordinal_program():  
    """
    Fungsi utama yang membungkus seluruh logika program.
    """
    
    def get_ordinal_tuple(number):
        """
        Fungsi ini "bersarang" di dalam run_ordinal_program.
        Fungsi ini hanya bisa diakses dari dalam fungsi luarnya.
        """
        
        if number % 100 in [11, 12, 13]:
            suffix = 'th'
        else:
            last_digit = number % 10
            if last_digit == 1:
                suffix = 'st'
            elif last_digit == 2:
                suffix = 'nd'
            elif last_digit == 3:
                suffix = 'rd'
            else:
                suffix = 'th'
        
        return (number, suffix)
    print("Ordinal Number")
    print("ketik 0 untuk mengentikan program")

    while True:
        try:
            angka_input = int(input("masukkan angka: "))
            
            hasil_tuple = get_ordinal_tuple(angka_input)
            
            print(hasil_tuple)
            
            if angka_input == 0:
                print("terima kasih telah menggunakan program saya")
                break 
                
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka integer.")

run_ordinal_program()