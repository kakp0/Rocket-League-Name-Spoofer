# Requirements
Ensure you have Python and mitmproxy correctly installed and added to your systems PATH!!
Also make sure you have corrrectly set up an SSL certificate for mitm and have all installed all the required modules (mitmproxy, json, and re) using pip

# How To Run:
1) Open RL Name Spoofer.py and *CHANGE* both the CURRENT_NAME and NEW_NAME variables to what you want!
2) Open CMD and launch mitmproxy running the script with the command `mitmdump -s "C:\CHANGE\ME\TO\THE\FILE\PATH\OF\RL Name Spoofer.py"` 
**(Leave this running the entire time you are playing, as all your internet traffic flows through this proxy. So closing the proxy means essentially closing your internet connection...)**
3) Press "Windows+i" to open your internet settings
4) Under "Manual proxy setup" select "Edit" for "Use a proxy server"
5) Set the Proxy IP address to `127.0.0.1` and the port to `8080` (This will route all your traffic through mitmproxy)
6) Press "Save"
7) Open Rocket League and enjoy B)
**8) When you're done, turn off the proxy you set up in steps 3-6. You can now safely close mitmproxy (in CMD)**

# Help
If you run into any issues setting this up, paste your error messages and what you've done so far into Gemini, ChatGPT, etc... They'll be able to help you a lot faster and with more specificity than I can. 

If that still dosent work feel free to message me @kakpo on discord and I'll get back to you when I can.

**NOTE: If you compile this into an exe and re-sell it to skids on RL cheat servers, I legally reserve the right to come to your house and beat you over the head with a heavy rock :)**
