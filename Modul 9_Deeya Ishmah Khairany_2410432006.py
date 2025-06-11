import time
import os
from termcolor import colored

lebar_bendera = 30
tinggi_bendera = 12
tinggi_tiang = 16

tabel_gerak = [0, 1, 2, 1, 0, -1, -2, -1]
len_gerak = len(tabel_gerak)

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def bendera(frame_num):
    bersihkan_layar()
    for y in range(tinggi_tiang):
        # Tiang warna kuning
        line = colored('|', 'yellow')
        if y < tinggi_bendera:
            for x in range(lebar_bendera):
                wave = tabel_gerak[(y + frame_num) % len_gerak]
                pos = x + wave
                # warna merah
                if y < tinggi_bendera // 2:
                    if 0 <= pos < lebar_bendera:
                        line += colored(' ', 'white', 'on_red')
                    else:
                        line += ' '
                else:
                    # warna putih
                    if 0 <= pos < lebar_bendera:
                        line += colored(' ', 'grey', 'on_white')
                    else:
                        line += ' '
        else:
            line += ' ' * lebar_bendera
        print(line)

def main():
    frame = 0
    while True:
        bendera(frame)
        time.sleep(0.1)
        frame += 1

main()
