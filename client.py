import socket
import time

s = socket.socket()
port = 1060
server = '127.0.0.1'
timeout = 60

s.settimeout(timeout)
s.connect((server,port))
message = s.recv(1024).decode()


print("Guess the word!")
print("You have 6 chances to guess the word.")
print("Each time you guess a wrong letter or wrong word you lose a chance.")

if message.lower().strip()=='ok':
    message = "Client connecting..."
    s.send(message.encode())
    data = s.recv(1024).decode()
    print(data)
    data = s.recv(1024).decode()
    print(data)
    message = input("Input: ")
    if message=='start':
        data = s.send(message.encode())   
        data2 = s.recv(1024).decode()
        print(data2)
        data3 = s.recv(1024).decode()
        length = int(data3)
        message = "Give me the hidden word".encode()
        message2 = s.send(message)
        word = []

        for i in range(0,length):
            word.append(s.recv(1024).decode())
        hidden_word= "".join(word)

        while True:
            data1 = s.recv(1024).decode()
            print(data1)
            data = input("Enter l(letter) or w(word):")
            message = s.send(data.encode())
            if data=='l':
                word_new1 = []
                letter = input("Guess a letter: ")
                data4 = s.send(letter.encode())
                data6 = s.recv(1024).decode()
                print(data6)
                if data6=='Valid input':
                    for i in range(0,length):
                        try:
                            data = s.recv(1024).decode()
                        except socket.timeout:   
                            print('Timeout') 
                        word_new1.append(data)
                    hidden_word_new = "".join(word_new1)
                    m = s.recv(1024).decode()
                    if m=="0":
                        print("Congratulations you guessed the word!")
                        break
                    else:
                        print("Continue guessing")
                        guesses_left = s.recv(1024).decode()
                        print("Guesses left: ",guesses_left)
                        if guesses_left=="0":
                            print("Game over!")
                            break
                else:
                    continue    
            elif data=='w':
                word = input('Guess a word: ')
                message4 = s.send(word.encode())
                data4 = s.recv(1024).decode()
                print(data4)
                if str(data4) == "Congratulations you guessed the word!":
                    break
                else:
                    print("Continue guessing")
                    guesses_left = s.recv(1024).decode()
                    print("Guesses left: ",guesses_left)
                    if guesses_left=="0":
                        print("Game over!")
                        break
                                
            
                



