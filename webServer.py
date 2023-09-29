# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)

  # Prepare a server socket
  serverSocket.bind(("", port))

  # Fill in start
  # Listen for incoming connections
  serverSocket.listen(1)
  # Fill in end

  while True:
    # Establish the connection

   # print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start - accept incoming connections
    # Fill in end

    try:
      message = connectionSocket.recv(1024).decode()  # Fill in start - receive data from client
      # Fill in end
      filename = message.split()[1]

      # opens the client requested file.
      # Fill in start
      f = open(filename[1:], 'rb')  # Open the file in binary mode
      # Fill in end

      # This variable can store the headers you want to send for any valid or invalid request.
      # What header should be sent for a response that is ok?
      # Fill in start
      response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nServer: MyServer\r\nConnection: close\r\n\r\n"
      # Fill in end

      # Read the content of the requested file
      file_content = f.read()

      # Concatenate the headers and content into a single response message
      response_message = response_headers.encode() + file_content

      # Send the response message to the client all at once
      connectionSocket.send(response_message)

      connectionSocket.close()  # closing the connection socket

    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      # Fill in start
      error_response = "HTTP/1.1 404 Not Found\r\nServer: MyServer\r\nConnection: close\r\n\r\n"
      connectionSocket.send(error_response.encode())  # Send the 404 response
      # Fill in end

      # Close client socket
      # Fill in start
      connectionSocket.close()  # Close the connection
      # Fill in end

  # Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop.
  # DO NOT DO THAT OR YOU'RE GONNA HAVE A BAD TIME.
  # serverSocket.close()
  # sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
