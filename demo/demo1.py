from pyco import *
import time

# Clear the log file
Logger.ClearLog()
# Log everything into the log file
Logger.SetLogLevel(Logger.Levels.ALL)

PrintMessage("This is an error message.", prefix="ERROR")
PrintMessage("This is a warning message.", prefix="WARNING")
PrintMessage("This is a success message.", prefix="SUCCESS")
PrintMessage("This is an info message.", prefix="INFO")
PrintMessage("This is a generic message.")
PrintMessage("This is a message with a custom prefix.", prefix="Custom Prefix")
PrintMessage("This is a message with a custom color.", messageColor=Color.Fore.BRIGHT_CYAN)
PrintMessage("You can combine custom prefixes and colors.", prefix="Example", prefixColor=Color.Fore.BRIGHT_MAGENTA)
PrintMessage("You can even override preset message colors.", prefix="ERROR", prefixColor=Color.Fore.BRIGHT_GREEN)
PrintMessage("You can set the colors for the message and prefix separately.", prefix="Example", messageColor=Color.Fore.RED, prefixColor=Color.Fore.YELLOW)
PrintMessage("For even more customizability, you can choose whether to color only the prefix,", prefix="INFO", prefixColor=Color.Fore.BRIGHT_BLUE)
PrintMessage("Or the brackets as well.", prefix="INFO", prefixColor=Color.Fore.BRIGHT_BLUE, colorBrackets=True)
PrintMessage("This message has been logged in the log file.", prefix="INFO", forceLog=True)

# Create an instance of the progress bar
ProgressBar = ProgressBar(prefix="Example progress bar", length=50)
# Update the progress bar every 100 milliseconds, 100 times
for item in range(101):
    ProgressBar.Update(item)
    time.sleep(0.1)

UserInput("This is an input prompt. ")
UserInput("The prompts can be colored. ", Color.Fore.BRIGHT_YELLOW)
UserInput("As well as the user's input. ", Color.Fore.BRIGHT_GREEN, Color.Fore.CYAN)
UserInput("Press enter to exit the program. ")