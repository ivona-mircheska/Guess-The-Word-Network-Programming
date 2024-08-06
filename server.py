import socket
import random
import time

s = socket.socket()
port = 1060
server = '127.0.0.1'
timeout = 60
s.settimeout(timeout)
s.bind((server,port))
print("Server listening at: ",s.getsockname())

s.listen(1)
connection,address = s.accept()
message = 'ok'.encode()
connection.send(message)

data = connection.recv(1024).decode()
print(data)
print("Got connection from: ", str(address))
message = "Connected to server".encode()
connection.send(message)
words = ["Elephant","Cactus","Bicycle","Volcano","Waterfall","Rainbow","Kangaroo","Cupcake","Avocado","Jellyfish",
         "Sunflower","Dragonfly","Seahorse","Lightning","Firecracker","Snowflake","Dog","Mirror","Honeybee","Octopus"]
random_word = random.choice(words)
print("The word is:",random_word)
chances = 6
guessed_letters = set()
hidden_word = [random_word[0]] + ["_"] * (len(random_word) - 2) + [random_word[-1]]

for i in range(1, len(random_word) - 1):
    if random_word[i] == random_word[0].lower() or random_word[i] == random_word[-1]:
        hidden_word[i] = random_word[i]

hidden_word = "".join(hidden_word)
print("Hidden word:", hidden_word)
message1 = "Input start to begin the game!".encode()
connection.send(message1)
s.settimeout(timeout)

try:
     data = connection.recv(1024).decode()   
except socket.timeout:
        print("Timeout for receiving")

if data == 'start':
    message = "The game begins".encode()
    connection.send(message)
    print("Game has started")
    length = len(hidden_word)
    l = str(length).encode()
    connection.send(l)
    message2=connection.recv(1024).decode()
    
    print("Client said:",message2)
    time.sleep(2)

    for i in range(0,len(hidden_word)):
        connection.send(hidden_word[i].encode())
        time.sleep(0.5)

    while chances>0:
        message = f"Guessed letters: {', '.join(guessed_letters)}. Word: {hidden_word}"
        connection.send(message.encode())
        data = connection.recv(1024).decode()
        if data=='l':
            try:
                letter = connection.recv(1024).decode()
            except socket.timeout:
                print("Timeout for receiving")
            print('I received letter:',letter)
            if letter in guessed_letters:
                message = connection.send('You already guessed that letter! Try again.'.encode())
                continue
            elif len(letter) != 1 or not letter.isalpha() or letter in hidden_word:
                connection.send('Invalid guess.'.encode())
                continue
            else:
                connection.send('Valid input'.encode())
                for i, l in enumerate(random_word):
                    if l == letter:
                        hidden_word = hidden_word[:i] + letter + hidden_word[i + 1:]
                hidden_word = "".join(hidden_word)
                for k in range(0, len(hidden_word)):
                    connection.send(hidden_word[k].encode())
                    time.sleep(1)
                if letter not in random_word:
                    chances = chances-1
               
                if hidden_word==random_word:
                    time.sleep(2)
                    message2 = "0"
                    data = connection.send(message2.encode())
                    chances = 0
                    connection.close()
                    time.sleep(2)
                else:
                    message3 = "1"
                    data = connection.send(message3.encode())
                    print("Sending guesses left")
                    guesses = connection.send(str(chances).encode())
                guessed_letters.add(letter)
                time.sleep(3)
        elif data == 'w':
            data3 = connection.recv(1024).decode()
            if data3 == random_word:
                message3 = "Congratulations you guessed the word!"
                data4 = connection.send(message3.encode())
                chances = 0
                connection.close()
            else:
                message4 = 'Wrong word'
                data5 = connection.send(message4.encode())
                chances = chances - 1
                print("Sending guesses left")
                guesses = connection.send(str(chances).encode())
                time.sleep(5)
    if chances==0:
       connection.close() 
       s.close()