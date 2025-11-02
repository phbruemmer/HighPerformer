**1. Setup for computer startup**
- Clone this repository `git clone https://github.com/phbruemmer/HighPerformer.git`
- Now checkout the `BLOCKED.json` file.
  - You'll find a structure like that:
  
    ```json
    {
      "BLOCKED_APPLICATIONS": [
        "FunnyGame.exe",
        "Browser.exe",
        "Virus.exe",
      ],
      "BLOCKED_WEBSITES": []
    }
    ```

  
- Press `WIN + r` to open up the run dialog box and enter `shell:startup`
  - This should open your Explorer at `C:\Users\<Your Username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
    where you can find shortcuts to autostart scripts or applications.
- Add a new short cut and enter the path of the `main.pyw` script.
  - To make sure everything works, execute the shortcut and open up a process you added to the `BLOCKED_APPLICATIONS` in the `BLOCKED.json` file.
 
---

**2. How to block an application?**
- The most important and easiest step to block a process, is to find out what the application you want to block is called.
  Sometimes the process has a different name, so make sure you actually added the correct process to the `BLOCKED_APPLICATIONS`.
- The easiest way (in my opinion) is to use the `process_lookup.py` script (not in the repo atm.).
  - Execute the application you want to block and then start the script.
  - Now, the first thing you see is a full list of all running processes on your computer.
    You can either search for your process manually, or try and search it via the input field.
- When you found the process you want to block, simply add it to the `BLOCKED_APPLICATIONS` list
  in the `BLOCKED.json` file and restart the `main.py` (with terminal) or `main.pyw` (without terminal) file .
