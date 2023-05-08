import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QInputDialog, QDialog
from PyQt5.QtGui import QIcon


# Create windows prompt
app = QApplication([])
password, ok = QInputDialog.getText(None, 'Password', 'Enter your password:')
if ok:
    with open('module/AlgoCI/userInputPending.noid', 'w') as f:
        f.write(password)
if not ok:
     app.exit()


class ENCRYPT_INPUTUSER():
# Define the substitution cipher
    CHAR = {
        'a': 'UDFM45', 'b': 'H21DGF', 'c': 'FDH56D', 'd': 'FGS546', 'e': 'JUK4JH',
        'f': 'ERG54S', 'g': 'T5H4FD', 'h': 'RG641G', 'i': 'RG4F4D', 'j': 'RT56F6',
        'k': 'VCBC3B', 'l': 'F8G9GF', 'm': 'FD4CJS', 'n': 'G423FG', 'o': 'F45GC2',
        'p': 'TH5DF5', 'q': 'CV4F6R', 'r': 'XF64TS', 's': 'X78DGT', 't': 'TH74SJ',
        'u': 'BCX6DF', 'v': 'FG65SD', 'w': '4KL45D', 'x': 'GFH3F2', 'y': 'GH56GF',
        'z': '45T1FG', '1': 'D4G23D', '2': 'GB56FG', '3': 'SF45GF', '4': 'P4FF12',
        '5': 'F6DFG1', '6': '56FG4G', '7': 'USGFDG', '8': 'FKHFDG', '9': 'IFGJH6',
        '0': '87H8G7', '@': 'G25GHF', '#': '45FGFH', '$': '75FG45', '*': '54GDH5',
        '(': '45F465', '.': 'HG56FG', ',': 'DF56H4', '-': 'F5JHFH', ' ': 'SGF4HF',
        '\\': '45GH45', '/': '56H45G'
    }


        # Read input from file
    with open('module/AlgoCI/userInputPending.noid', 'r') as f:
            user_input = f.readline().strip()

        # Encrypt the input using the substitution cipher
    encrypted_output = ''
    for char in user_input:
            encrypted_output += CHAR.get(char.lower(), char)

        # Write encrypted output to file
    with open('module/AlgoCI/encryptResult.noid', 'w') as f:
            f.write(encrypted_output)

    print('Encryption completed!')
