# Essentials API
Made by Zgn

Since the package is not released to the public, if you want to use it before it releases, follow the steps below.

## How to setup (local)
1 - Download the latest zip file released from the releases page

2 - Extract the file into a folder into your desktop

3 - Open a command prompt in the folder and run ¨pip install -e .¨

4 - You can now use essentials package by putting essentials.py into your folder where you have your project on with ¨import essentials¨


### Functions
essentials.string.after("Google.com", ".") - returns "com"

essentials.string.before("Google.com", ".") - returns "Google"

essentials.file.read("text.txt") - returns text file as a str type

essentials.file.write("text.txt", "text") - writes/overwrites a text file

essentials.file.append("text.txt", "text") - appends items to a file

essentials.file.look_for("text.txt", "item") - looks for string, returns True if found

essentials.text.default() - Organizes the sentence given --> "hello this is a test " >>> "Hello this is a test"

essentials.text.title()  - Capitalizes every word in the sentence given --> "hello this is a test " >>> "Hello This Is A Test"

essentials.roundify(2.5) - Returns the int value of "3"

essentials.templates.discord_py() - Creates a discord py template in the folder that the program was ran

essentials.exit() - Quits the program
