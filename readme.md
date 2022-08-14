# CLI Chatter
![CLIChatterLogo](https://user-images.githubusercontent.com/95228665/184546091-49f79865-a75c-4187-8db4-025d3dfe27db.png)

CLI Chatter is a Python3 based chat software designed for simple use between 10 people *(or less)*.

## Installation ⚙️

1. Fork/Clone/Download this repo

    `git clone https://github.com/p-i-c-o/CLIChatter`

2. Navigate to the directory

    `cd CLIChatter`
    
3. Run the server script

    `python3 server.py`
    
4. Run the client script     (seperate terminal required)

    `python3 client.py`


## Details 🔎

##### Server Script
The server script serves as a communiations manager between all of the people currently on the client script. Everytime the script is run, it saves all messages to the LOG.txt file and adds a date on the top.

##### Client Script
The client script serves as an interface for the user to talk with other users on the same server, it requires the user to enter the IP Address of the desired server. It color-codes the different users connected in order to prevent confusion.



### Mini Warning ⚠️
When using the Client script, if you are interrupted by someone else in the middle of writing a message, do not write it again, just finish the message and press enter, it will take what you wrote.
