# 1. Converteer het decimale getal 45 naar binaire vorm.
dec_45 = 45
bin_45 = bin(dec_45)[2:]  # Verwijder '0b'
print(f"45 in binair: {bin_45}")

# 2. Zet binaire 1010101 om naar decimaal.
bin_1010101 = "1010101"
dec_from_bin = int(bin_1010101, 2)
print(f"1010101 in decimaal: {dec_from_bin}")

# 3. Tel binaire 10111 en 1101 op en druk het resultaat in binaire vorm.
bin_10111 = "10111"
bin_1101 = "1101"
bin_sum = bin(int(bin_10111, 2) + int(bin_1101, 2))[2:]
print(f"Som van 10111 en 1101: {bin_sum}")

# 4. Zet 255 om in hexadecimale vorm.
dec_255 = 255
hex_255 = hex(dec_255)[2:].upper()  # Verwijder '0x'
print(f"255 in hex: {hex_255}")

# 5. Converteer hex 2A naar decimaal.
hex_2A = "2A"
dec_from_hex_2A = int(hex_2A, 16)
print(f"2A in decimaal: {dec_from_hex_2A}")

# 6. Tel hex C4 en 3A op en druk het resultaat in hexadecimale vorm.
hex_C4 = "C4"
hex_3A = "3A"
hex_sum = hex(int(hex_C4, 16) + int(hex_3A, 16))[2:].upper()
print(f"Som van C4 en 3A: {hex_sum}")

# 7. Converteer binaire 1101 naar decimaal.
bin_1101 = "1101"
dec_from_bin_1101 = int(bin_1101, 2)
print(f"1101 in decimaal: {dec_from_bin_1101}")

# 8. Converteer hex F0 naar decimaal.
hex_F0 = "F0"
dec_from_hex_F0 = int(hex_F0, 16)
print(f"F0 in decimaal: {dec_from_hex_F0}")

# 9. Tel de decimale getallen 123 en 456 bij elkaar op.
dec_123 = 123
dec_456 = 456
dec_sum = dec_123 + dec_456
print(f"Som van 123 en 456: {dec_sum}")

# 10. Converteer 157 naar binair en vervolgens naar hexadecimaal.
dec_157 = 157
bin_157 = bin(dec_157)[2:]
hex_157 = hex(dec_157)[2:].upper()
print(f"157 in binair: {bin_157}, in hex: {hex_157}")

# 11. Converteer binaire 11101101 naar decimaal en vervolgens naar hexadecimaal.
bin_11101101 = "11101101"
dec_from_bin_11101101 = int(bin_11101101, 2)
hex_from_bin_11101101 = hex(dec_from_bin_11101101)[2:].upper()
print(f"11101101 in decimaal: {dec_from_bin_11101101}, in hex: {hex_from_bin_11101101}")

# 12. Converteer hex AB4 naar decimaal en vervolgens naar binair.
hex_AB4 = "AB4"
dec_from_hex_AB4 = int(hex_AB4, 16)
bin_from_hex_AB4 = bin(dec_from_hex_AB4)[2:]
print(f"AB4 in decimaal: {dec_from_hex_AB4}, in binair: {bin_from_hex_AB4}")
