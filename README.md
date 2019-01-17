# aptworld
Hello world for packaging a python script in a .deb package, requires python3.6.

## How to run:
After installing the .deb file, it has an installation requirement for python3 (>=3.6.0). Once installed, it will place an aptworld.py file in /usr/local/bin/aptworld.py.  

Finally run 'python3 /usr/local/bin/aptworld.py'

## Assumptions:
The prompt asked me to parse /var/lib/dpkg/status and/or other files to find all packages a user explicitly installed.  You could also rely on the python subprocess module or pexpect to call apt-mark show manual to give you packages that were marked as manual. Since the prompt asked me to parse /var/lib/dpkg/status, I decided to also parse /var/log/installer/initial-status.gz and compare packages to get a list of packages that ONLY exist in /var/lib/dpkg/status.  This gives us a list of packages that have been installed by a user after a system has been installed.

## What To improve:
Save the results to a file instead of printing it to the screen

Write a GUI front-end with either py-qt or Kivy
