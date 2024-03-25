# Essentials API
Made by Zgn

Since the package is not released to the public, if you want to use it before it releases, follow the steps below.

## How to setup (local)
1 - Download the latest zip file released from the releases page

2 - Extract the file into a folder into your desktop

3 - Open a command prompt in the folder and run ¨pip install -e .¨

4 - You can now use essentials package by putting essentials.py into your folder where you have your project on with ¨import essentials¨


### Functions
string.after("Google.com", ".") - returns "com"

string.before("Google.com", ".") - returns "Google"

file.read("text.txt") - returns text file as a str type

file.readlines("text.txt) - returns text file as a list type

file.write("text.txt", "text") - writes/overwrites a text file

file.append("text.txt", "text") - appends items to a file

file.look_for("text.txt", "item") - looks for string, returns True if found

text.default() - Organizes the sentence given --> "hello this is a test " >>> "Hello this is a test"

text.title()  - Capitalizes every word in the sentence given --> "hello this is a test " >>> "Hello This Is A Test"

roundify(2.5) - Returns the int value of "3"

templates.discord_py() - Creates a discord py template in the folder that the program was ran

exit() - Quits the program
