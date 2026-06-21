# Syntecxhub Port Scanner

## Project Overview

This project is a multithreaded TCP Port Scanner developed in Python as part of the Syntecxhub Cybersecurity Internship Program.

The scanner checks whether TCP ports on a target host are open or closed and saves the results to a log file.

## Features

* Scan a target host using TCP sockets
* Scan a custom range of ports
* Multithreaded scanning for improved performance
* Detect open and closed ports
* Log scan results to a file
* Handle exceptions and connection errors

## Technologies Used

* Python 3
* Socket Programming
* Threading

## How to Run

1. Open a terminal.
2. Navigate to the project directory.

```bash
cd Syntecxhub_Port_Scanner
```

3. Run the scanner.

```bash
python3 port_scanner.py
```

4. Enter:

   * Target IP address or hostname
   * Start port
   * End port

## Example

Target Host:

```text
localhost
```

Port Range:

```text
20 - 100
```

## Output

The program displays the scan results on the screen and saves them in:

```text
scan_results.txt
```

## Learning Outcomes

Through this project, I learned:

* TCP networking fundamentals
* Socket programming in Python
* Multithreading using Python threads
* Exception handling
* Logging and file operations
* Basic cybersecurity reconnaissance concepts

## Author

PeterTheSalem

Cybersecurity Student | SOC Analyst Aspirant
