<h1>Nmap NSE Scripts</h1>

This repository will eventually hold a list of useful Nmap NSE Scripts that I have either found, modified, or created myself. I will leave links to the original NSE script


<h1>How To Add an Nmap NSE Script</h1>

<h3>Install New Scripts</h3>


<h3>Add An NSE Script Manually Using Wget</h3>

1. sudo wget -O /usr/share/nmap/scripts/SCRIPT_NAME.nse https://svn.nmap.org/nmap/scripts/SCRIPT_NAME.nse
2. nmap --script-updatedb
3. sudo updatedb #You might have to run this, depending where you get the script from

<h3>Add An NSE Script Manually</h3>

1. sudo nano /usr/share/nmap/scripts/SCRIPT_NAME.nse
2. nmap --script-updatedb
3. sudo updatedb

<h1>Example Of NSE Script Running</h1>

<img width="1898" height="809" alt="dirscan-plus-nse-script-running" src="https://github.com/user-attachments/assets/6a40cc61-aca3-4f3f-a73d-1fb034fde2eb" />
