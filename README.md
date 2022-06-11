## How to run the script.
Open CMD in the root directory and run main.exe, this will open the executable in a loop.
```Example: C:\Users\fungus\Desktop>main.exe```
Running the script directly from file explorer will NOT work.

## How to stop the script
Simply close the window or process Ctrl-C to exit the process.

# Is this detectable?
No, not by VAC. However, you can still be game banned from Overwatch from enough reports or community server custom Anti-Cheats or admins. This script is protected only against VAC. 

# Does it work?
Yes, it pulls memory from the CSGO.exe though the python process, which is not detectable nor will be detectable by VAC. This is because python is a interpreter, meaning it doesn't have any certain signatures nor code. The only possible way of detection is accessing certain variables in the CSGO process protected directly, such as patch tables. This is ensured not to happen.

It simply detects when the player is on the ground and jumps that very same tick.
