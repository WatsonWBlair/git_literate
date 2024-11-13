Q: When running pytest for a code challenge, I'm getting unexpected results or errors. What should I check?

A: Before running pytest, it's essential to check your current directory (path) to ensure that you are in the correct location for the specific code challenge. Running pytest from an incorrect path may cause errors or unexpected results because the test files or modules may not be found. To verify your location, you can use the pwd command (on macOS/Linux) or cd and dir commands (on Windows) to navigate to the correct directory. Once confirmed, you can run pytest to test your code accurately.

Q: When getting error using "sudo make init" on MacOs, I am getting env error. What should I do?
A: Essentially make file has this commands $(shell python3 -m venv env)
    $(shell source env/bin/activate)
    $(shell pip3 install -r requirements.txt). So on your terminal just execute this three command. (Make sure writing sudo before every command).
    sudo python3 -m venv env
    sudo source env/bin/activate
    sudo pip3 install -r requirements.txt
    
