This project demonstrates a simple word-guessing game implemented using network programming in Python. The game is played between a server and a client over a local network.

Server-Side Implementation

The server is set up to listen for incoming connections on port 1060.
Upon establishing a connection, the server selects a random word from a predefined list and hides most of the letters in the word.
The client is prompted to guess the word by either submitting individual letters or attempting to guess the entire word.
The server provides feedback on each guess and tracks the number of chances remaining.
The game continues until the client guesses the word correctly or runs out of chances.

Client-Side Implementation

The client connects to the server and initiates the game by sending a start command.
The client receives the hidden word and interacts with the server to make guesses.
The client can submit guesses as individual letters or whole words and receives updates about the remaining chances and the game status.

