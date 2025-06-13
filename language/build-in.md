**Python Modules**
===

Here are explanations and examples for some commonly used ones:

### 1. **`_future__`** - Enables features that will be available in future Python versions.
```python
from __future__ import print_function
print("Hello, future!")  # This ensures compatibility across versions.
```

### 2. **`getpass`** - Securely gets user input without showing it.
```python
import getpass
password = getpass.getpass("Enter your password: ")
print("Password entered!")  # The input won't be visible while typing.
```

### 3. **`glob`** - Finds files matching a pattern.
```python
import glob
files = glob.glob("*.txt")  # Lists all `.txt` files in the current directory.
print(files)
```

### 4. **`gzip`** - Compresses and decompresses files in Gzip format.
```python
import gzip

text = b"Hello, this is compressed!"
with gzip.open("example.gz", "wb") as f:
    f.write(text)

with gzip.open("example.gz", "rb") as f:
    print(f.read())  # Decompresses and prints the content.
```

### 5. **`random`** - Generates random numbers.
```python
import random
print(random.randint(1, 100))  # Generates a random integer between 1 and 100.
```

### 6. **`subprocess`** - Runs system commands.
```python
import subprocess
output = subprocess.run(["echo", "Hello, world!"], capture_output=True, text=True)
print(output.stdout)  # Prints the result from the command.
```

Great! Here are explanations and examples for more Python modules:

### 7. **`secrets`** - Generates cryptographically strong random numbers.
```python
import secrets
print(secrets.token_hex(16))  # Generates a 16-byte secure hex token.
```

### 8. **`select`** - Monitors I/O operations for readiness.
```python
import select
import socket

s = socket.socket()
s.bind(("localhost", 12345))
s.listen(5)

print("Waiting for a connection...")
ready_sockets, _, _ = select.select([s], [], [], 10)  # Waits for 10 seconds
if ready_sockets:
    print("A connection is ready to be accepted!")
```

### 9. **`sqlite3`** - Works with SQLite databases.
```python
import sqlite3

conn = sqlite3.connect(":memory:")  # Creates an in-memory database
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # Fetches all records from the table.
```

### 10. **`smtplib`** - Sends emails using SMTP.
```python
import smtplib

server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login("your_email@example.com", "your_password")
server.sendmail("your_email@example.com", "recipient@example.com", "Hello, this is a test email!")
server.quit()
```
(*Replace credentials with actual values when using!*)

### 11. **`threading`** - Manages multiple threads.
```python
import threading

def print_message():
    print("Thread running!")

thread = threading.Thread(target=print_message)
thread.start()
thread.join()  # Waits for the thread to finish.
```

### 12. **`zipfile`** - Works with `.zip` archives.
```python
import zipfile

with zipfile.ZipFile("example.zip", "w") as z:
    z.write("test.txt")  # Adds `test.txt` to the zip archive.

with zipfile.ZipFile("example.zip", "r") as z:
    print(z.namelist())  # Lists files inside the zip archive.
```


### 13. **`uuid`** - Generates unique identifiers.
```python
import uuid
print(uuid.uuid4())  # Generates a random unique identifier.
```

### 14. **`hashlib`** - Computes hash values.
```python
import hashlib
data = "Hello, world!".encode()
hashed = hashlib.sha256(data).hexdigest()
print(hashed)  # Prints SHA-256 hash of the string.
```

### 15. **`pickle`** - Serializes and deserializes Python objects.
```python
import pickle
data = {"name": "Alice", "age": 25}

# Save to a file
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Load from a file
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
print(loaded_data)  # Prints the original dictionary.
```

### 16. **`json`** - Works with JSON data.
```python
import json
data = {"name": "Bob", "age": 30}

# Convert to JSON string
json_str = json.dumps(data)
print(json_str)

# Convert back to dictionary
parsed_data = json.loads(json_str)
print(parsed_data["name"])
```

### 17. **`xml.etree.ElementTree`** - Parses XML data.
```python
import xml.etree.ElementTree as ET

xml_data = "<user><name>Alice</name><age>25</age></user>"
root = ET.fromstring(xml_data)
print(root.find("name").text)  # Prints 'Alice'.
```

### 18. **`socket`** - Enables network communication.
```python
import socket

s = socket.socket()
s.connect(("example.com", 80))
s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
print(s.recv(1024))  # Receives data from the server.
s.close()
```

### 19. **`email`** - Constructs emails in Python.
```python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg["From"] = "you@example.com"
msg["To"] = "recipient@example.com"
msg["Subject"] = "Hello"
msg.attach(MIMEText("This is an email message.", "plain"))

print(msg.as_string())  # Prints the email structure.
```

### 20. **`threading.Timer`** - Delays execution.
```python
import threading

def say_hello():
    print("Hello, after 5 seconds!")

timer = threading.Timer(5, say_hello)
timer.start()  # Runs function after 5 seconds.
```

Absolutely! Here are more Python modules explained with examples:

### 21. **`math`** - Performs mathematical operations.
```python
import math
print(math.sqrt(25))  # Square root
print(math.pi)  # Value of Pi
print(math.sin(math.radians(30)))  # Sine of 30 degrees
```

### 22. **`re`** - Works with regular expressions.
```python
import re
text = "The price is $50."
match = re.search(r"\$\d+", text)  # Finds the first occurrence of a dollar amount
print(match.group())  # Prints "$50"
```

### 23. **`itertools`** - Provides efficient looping tools.
```python
import itertools
for item in itertools.permutations([1, 2, 3]):
    print(item)  # Prints all possible orders of [1, 2, 3]
```

### 24. **`datetime`** - Handles date and time.
```python
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Formats the current date and time
```

### 25. **`tkinter`** - Creates simple GUI applications.
```python
import tkinter as tk

root = tk.Tk()
root.title("Hello, Tkinter!")

label = tk.Label(root, text="Welcome to my app!")
label.pack()

root.mainloop()  # Runs the app
```

### 26. **`threading`** - Enables parallel execution.
```python
import threading

def greet():
    print("Hello from a thread!")

thread = threading.Thread(target=greet)
thread.start()
thread.join()
```

### 27. **`time`** - Works with time-based operations.
```python
import time
print("Waiting for 3 seconds...")
time.sleep(3)  # Delays execution for 3 seconds
print("Done!")
```

### 28. **`os`** - Interacts with the operating system.
```python
import os
print(os.getcwd())  # Prints the current working directory
print(os.listdir("."))  # Lists files in the current folder
```

### 29. **`sys`** - Provides system-related functions.
```python
import sys
print(sys.platform)  # Prints the operating system name
print(sys.argv)  # Lists command-line arguments passed to the script
```

### 30. **`shutil`** - Handles file operations.
```python
import shutil
shutil.copy("source.txt", "destination.txt")  # Copies a file
```

### 31. **`functools`** - Provides higher-order functions.
```python
import functools

@functools.lru_cache(maxsize=100)
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

print(factorial(5))  # Efficient caching of function calls.
```

### 32. **`statistics`** - Performs statistical calculations.
```python
import statistics
data = [10, 20, 30, 40, 50]
print(statistics.mean(data))  # Average value
print(statistics.median(data))  # Middle value
```

### 33. **`csv`** - Handles CSV files.
```python
import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # Reads each row from the CSV file.
```

### 34. **`argparse`** - Parses command-line arguments.
```python
import argparse

parser = argparse.ArgumentParser(description="Example parser")
parser.add_argument("--name", type=str, help="Your name")
args = parser.parse_args()
print(f"Hello, {args.name}!")  # Runs via command line with: python script.py --name Alice
```

### 35. **`calendar`** - Works with dates and calendars.
```python
import calendar
print(calendar.month(2025, 6))  # Prints the calendar for June 2025.
```

### 36. **`pprint`** - Pretty-prints data structures.
```python
import pprint
data = {"name": "Alice", "details": {"age": 25, "city": "New York"}}
pprint.pprint(data, width=40)  # Displays data neatly formatted.
```

### 37. **`traceback`** - Handles error tracebacks.
```python
import traceback

try:
    1 / 0
except Exception:
    print(traceback.format_exc())  # Prints the full error traceback.
```

### 38. **`enum`** - Defines enumerations.
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)  # Outputs: Color.RED
print(Color.RED.name, Color.RED.value)  # Prints 'RED' and '1'.
```

### 39. **`difflib`** - Compares sequences.
```python
import difflib

text1 = "Hello, world!"
text2 = "Hello, Python!"

diff = difflib.ndiff(text1.split(), text2.split())
print("\n".join(diff))  # Shows differences between texts.
```

### 40. **`heapq`** - Implements priority queues.
```python
import heapq

numbers = [4, 1, 7, 3, 8]
heapq.heapify(numbers)
print(heapq.heappop(numbers))  # Pops the smallest value (1).
```

Absolutely! Here are even more Python modules explained with examples:

### 41. **`tempfile`** - Creates temporary files and directories.
```python
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b"Hello, temp file!")
    print(f"Temporary file created: {temp_file.name}")
```

### 42. **`unicodedata`** - Handles Unicode characters.
```python
import unicodedata
print(unicodedata.name("€"))  # Prints the official name of the Euro symbol.
```

### 43. **`sysconfig`** - Retrieves system configuration information.
```python
import sysconfig
print(sysconfig.get_platform())  # Prints the platform name.
```

### 44. **`tabnanny`** - Detects inconsistent indentation in Python files.
```python
import tabnanny
tabnanny.check("script.py")  # Checks a script for indentation issues.
```

### 45. **`zipimport`** - Imports modules from a ZIP archive.
```python
import zipimport

# Assuming `my_module.py` exists inside `modules.zip`
importer = zipimport.zipimporter("modules.zip")
module = importer.load_module("my_module")

print(module)  # Loads the module from the ZIP archive.
```

### 46. **`sched`** - Schedules tasks.
```python
import sched, time

scheduler = sched.scheduler(time.time, time.sleep)

def task():
    print("Scheduled task executed!")

scheduler.enter(5, 1, task)  # Runs after 5 seconds.
scheduler.run()
```

### 47. **`pydoc`** - Generates Python documentation.
```python
import pydoc
help(pydoc)  # Prints documentation about pydoc itself.
```

### 48. **`platform`** - Gathers system information.
```python
import platform
print(platform.system(), platform.release())  # Prints OS name and version.
```

### 49. **`colorsys`** - Converts between color formats.
```python
import colorsys
r, g, b = colorsys.hsv_to_rgb(0.5, 1.0, 1.0)
print(f"RGB color: {r}, {g}, {b}")  # Converts HSV to RGB format.
```

### 50. **`tokenize`** - Reads Python source code tokens.
```python
import tokenize
from io import BytesIO

code = b"print('Hello, Python!')"
for token in tokenize.tokenize(BytesIO(code).readline):
    print(token)  # Displays each token from the Python code.
```


### 51. **`hmac`** – Generates cryptographic HMAC (Hash-based Message Authentication Code).
```python
import hmac
import hashlib

key = b"secret_key"
message = b"Hello, security!"
hmac_hash = hmac.new(key, message, hashlib.sha256).hexdigest()
print(hmac_hash)  # Secure hash of the message.
```

### 52. **`xmlrpc.client`** – Implements XML-RPC client functionality.
```python
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://example.com:8000")
print(proxy.system.listMethods())  # Lists available remote methods.
```

### 53. **`fnmatch`** – Matches file patterns using Unix-style wildcards.
```python
import fnmatch
files = ["data.txt", "notes.doc", "image.png", "backup.txt"]
filtered = [f for f in files if fnmatch.fnmatch(f, "*.txt")]
print(filtered)  # Filters out only `.txt` files.
```

### 54. **`imaplib`** – Handles IMAP email access.
```python
import imaplib

mail = imaplib.IMAP4_SSL("imap.example.com")
mail.login("your_email@example.com", "your_password")
mail.select("inbox")
status, emails = mail.search(None, "ALL")
print("Emails:", emails)
```
(*Replace credentials when testing!*)

### 55. **`uuid`** – Generates universally unique identifiers (UUIDs).
```python
import uuid
print(uuid.uuid4())  # Creates a random unique identifier.
```

### 56. **`trace`** – Traces program execution.
```python
import trace

tracer = trace.Trace(count=True, trace=True)
tracer.run('print("Tracing this script!")')
```

### 57. **`webbrowser`** – Opens web pages from Python.
```python
import webbrowser
webbrowser.open("https://www.python.org")  # Opens Python's official website.
```

### 58. **`winreg`** – Reads and modifies Windows registry keys.
```python
import winreg

with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion") as key:
    value, _ = winreg.QueryValueEx(key, "ProgramFilesDir")
    print("Program Files Directory:", value)
```

### 59. **`winsound`** – Plays sound in Windows.
```python
import winsound
winsound.Beep(1000, 500)  # Beeps at 1000 Hz for 500 milliseconds.
```

### 60. **`subprocess`** – Executes system commands.
```python
import subprocess
result = subprocess.run(["echo", "Hello, subprocess!"], capture_output=True, text=True)
print(result.stdout)  # Displays command output.
```


### 61. **`argparse`** – Parses command-line arguments.
```python
import argparse

parser = argparse.ArgumentParser(description="Example argument parser")
parser.add_argument("--name", type=str, help="Your name")
args = parser.parse_args()
print(f"Hello, {args.name}!")  # Run via command line: python script.py --name Alice
```

### 62. **`difflib`** – Compares sequences and highlights differences.
```python
import difflib

text1 = "Hello, world!"
text2 = "Hello, Python!"

diff = difflib.ndiff(text1.split(), text2.split())
print("\n".join(diff))  # Shows text differences.
```

### 63. **`py_compile`** – Compiles Python code into `.pyc` files.
```python
import py_compile
py_compile.compile("script.py")  # Compiles 'script.py' into a bytecode `.pyc` file.
```

### 64. **`queue`** – Implements a queue for handling tasks.
```python
import queue

q = queue.Queue()
q.put("Task 1")
q.put("Task 2")
print(q.get())  # Retrieves the first task.
```

### 65. **`shlex`** – Parses shell-style syntax.
```python
import shlex
command = "echo 'Hello, Python'"
tokens = shlex.split(command)
print(tokens)  # Outputs: ['echo', 'Hello, Python']
```

### 66. **`shelve`** – Stores Python objects persistently.
```python
import shelve

with shelve.open("mydata") as db:
    db["name"] = "Alice"
    db["age"] = 25

with shelve.open("mydata") as db:
    print(db["name"], db["age"])  # Retrieves stored data.
```

### 67. **`calendar`** – Displays and manipulates dates.
```python
import calendar
print(calendar.month(2025, 6))  # Prints June 2025's calendar.
```

### 68. **`socketserver`** – Creates a simple server.
```python
import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(b"Hello, Client!")

server = socketserver.TCPServer(("localhost", 9999), MyHandler)
server.serve_forever()
```

### 69. **`cProfile`** – Profiles Python code for performance analysis.
```python
import cProfile

def slow_function():
    for _ in range(1000000):
        pass

cProfile.run("slow_function()")  # Shows performance metrics.
```

### 70. **`tarfile`** – Works with `.tar.gz` archives.
```python
import tarfile

# Create a tar archive
with tarfile.open("example.tar.gz", "w:gz") as tar:
    tar.add("test.txt")

# Extract files
with tarfile.open("example.tar.gz", "r:gz") as tar:
    tar.extractall("output_directory")
```

Absolutely! Here are even more useful Python modules with explanations and examples:

### 71. **`weakref`** – Creates weak references to objects (useful for memory optimization).
```python
import weakref

class Example:
    pass

obj = Example()
weak_ref = weakref.ref(obj)
print(weak_ref())  # Access the object
```

### 72. **`random`** – Generates random numbers.
```python
import random
print(random.randint(1, 100))  # Random integer between 1 and 100
print(random.choice(["apple", "banana", "cherry"]))  # Random choice
```

### 73. **`ssl`** – Enables secure networking via SSL/TLS.
```python
import ssl
context = ssl.create_default_context()
print(context.protocol)  # Shows SSL protocol being used
```

### 74. **`codecs`** – Handles various encodings.
```python
import codecs
text = "Hello, world!"
encoded = codecs.encode(text, "rot_13")  # Applies ROT13 encoding
print(encoded)
```

### 75. **`zipapp`** – Packages Python applications into `.pyz` archives.
```python
import zipapp
zipapp.create_archive("my_script", "my_app.pyz")  # Converts script folder into an executable archive
```

### 76. **`textwrap`** – Formats text neatly.
```python
import textwrap
text = "This is a long piece of text that needs wrapping."
print(textwrap.fill(text, width=20))  # Wraps text at 20 characters
```

### 77. **`reprlib`** – Creates limited string representations of objects.
```python
import reprlib
data = ["apple"] * 100
print(reprlib.repr(data))  # Truncates long object representation
```

### 78. **`csv.DictReader`** – Reads CSV files into dictionaries.
```python
import csv

with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # Prints each row as a dictionary
```

### 79. **`ntpath`** – Handles Windows path operations.
```python
import ntpath
print(ntpath.basename("C:\\Users\\file.txt"))  # Extracts the filename
```

### 80. **`urllib`** – Fetches URLs in Python.
```python
import urllib.request
response = urllib.request.urlopen("https://www.python.org")
print(response.read()[:100])  # Fetches first 100 bytes from the page
```

### 81. **`logging`** – Handles log messages and debugging.
```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an info log.")
logging.warning("This is a warning log.")
logging.error("This is an error log.")
```

### 82. **`inspect`** – Retrieves information about live objects.
```python
import inspect

def example_function():
    pass

print(inspect.getsource(example_function))  # Shows function source code
```

### 83. **`filecmp`** – Compares files and directories.
```python
import filecmp

print(filecmp.cmp("file1.txt", "file2.txt"))  # True if files are identical
```

### 84. **`mimetypes`** – Determines file types.
```python
import mimetypes

print(mimetypes.guess_type("example.jpg"))  # Outputs ('image/jpeg', None)
```

### 85. **`json.tool`** – Formats JSON output in the command line.
```bash
echo '{"name": "Alice", "age": 25}' | python -m json.tool
```

### 86. **`errno`** – Lists error codes used in Python.
```python
import errno

print(errno.ENOENT)  # Error code for "No such file or directory"
print(errno.errorcode[errno.ENOENT])  # Retrieves error name
```

### 87. **`msvcrt`** – Provides Windows console utilities.
```python
import msvcrt

print("Press a key...")
key = msvcrt.getch()
print(f"You pressed: {key.decode()}")
```

### 88. **`pdb`** – Debugs Python scripts.
```python
import pdb

def buggy_function():
    a = 5
    pdb.set_trace()  # Debugging starts here
    b = a + 10
    return b

buggy_function()
```

### 89. **`traceback`** – Formats and prints errors.
```python
import traceback

try:
    1 / 0
except ZeroDivisionError:
    print(traceback.format_exc())  # Prints the full error traceback
```

### 90. **`weakref.finalize`** – Ensures cleanup actions when an object is deleted.
```python
import weakref

class Example:
    pass

obj = Example()
weakref.finalize(obj, lambda: print("Object deleted"))
del obj  # Triggers the cleanup function
```


### 91. **`typing`** – Provides type hints for Python code.
```python
from typing import List

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

print(add_numbers([1, 2, 3]))  # Outputs: 6
```

### 92. **`xml.dom.minidom`** – Parses and modifies XML data.
```python
import xml.dom.minidom

xml_string = "<root><message>Hello, XML!</message></root>"
dom = xml.dom.minidom.parseString(xml_string)
print(dom.toprettyxml())  # Prints formatted XML output
```

### 93. **`base64`** – Encodes and decodes data using Base64.
```python
import base64

encoded = base64.b64encode(b"Hello, world!")
print(encoded)  # Encoded output
print(base64.b64decode(encoded))  # Decodes it back
```

### 94. **`wave`** – Works with WAV audio files.
```python
import wave

with wave.open("example.wav", "rb") as wav_file:
    print(f"Channels: {wav_file.getnchannels()}, Sample rate: {wav_file.getframerate()}")
```

### 95. **`uuid.uuid1`** – Generates a UUID based on current time and system info.
```python
import uuid

print(uuid.uuid1())  # Creates a UUID based on timestamp and system info
```

### 96. **`timeit`** – Measures execution time of small snippets.
```python
import timeit

execution_time = timeit.timeit("sum(range(1000))", number=10000)
print(f"Execution time: {execution_time} seconds")
```

### 97. **`html.parser`** – Parses HTML pages.
```python
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Found start tag: {tag}")

parser = MyHTMLParser()
parser.feed("<html><body><h1>Hello</h1></body></html>")
```

### 98. **`turtle`** – Creates simple graphics with Python.
```python
import turtle

turtle.forward(100)  # Moves forward by 100 pixels
turtle.right(90)  # Turns right 90 degrees
turtle.forward(100)
turtle.done()  # Ends the turtle drawing session
```

### 99. **`pydoc`** – Generates Python documentation dynamically.
```python
import pydoc
print(pydoc.render_doc("str"))  # Displays documentation for strings
```

### 100. **`enum.Enum`** – Defines and works with enumerations.
```python
from enum import Enum

class Status(Enum):
    SUCCESS = 1
    FAILURE = 2
    PENDING = 3

print(Status.SUCCESS.name, Status.SUCCESS.value)  # Outputs: SUCCESS 1
```

### 101. **`heapq`** – Implements a priority queue.
```python
import heapq

numbers = [4, 1, 7, 3, 8]
heapq.heapify(numbers)
print(heapq.heappop(numbers))  # Pops the smallest value (1).
```

### 102. **`contextvars`** – Manages context-specific variables.
```python
import contextvars

var = contextvars.ContextVar("example_var")
var.set("Hello, Context!")

print(var.get())  # Outputs: Hello, Context!
```

### 103. **`cmd`** – Builds command-line applications.
```python
import cmd

class MyShell(cmd.Cmd):
    prompt = "> "

    def do_greet(self, line):
        print("Hello, " + line)

MyShell().cmdloop()
```

### 104. **`pty`** – Simulates pseudo-terminal devices (Linux).
```python
import pty
import os

pid, fd = pty.fork()
if pid == 0:  # Child process
    os.execvp("ls", ["ls", "-l"])  # Executes 'ls -l'
```

### 105. **`zipfile`** – Compresses and extracts ZIP files.
```python
import zipfile

with zipfile.ZipFile("example.zip", "w") as zipf:
    zipf.write("test.txt")

with zipfile.ZipFile("example.zip", "r") as zipf:
    zipf.extractall("extracted_files")
```

### 106. **`tarfile`** – Works with TAR archives.
```python
import tarfile

# Creating a tar archive
with tarfile.open("example.tar.gz", "w:gz") as tar:
    tar.add("test.txt")

# Extracting from a tar archive
with tarfile.open("example.tar.gz", "r:gz") as tar:
    tar.extractall("output_directory")
```

### 107. **`difflib.SequenceMatcher`** – Measures string similarity.
```python
import difflib

text1 = "Hello, world!"
text2 = "Hello, Python!"

similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
print(f"Similarity: {similarity:.2f}")  # Prints similarity score between two texts.
```

### 108. **`ssl.SSLContext`** – Manages SSL connections.
```python
import ssl
context = ssl.create_default_context()
print(context.protocol)  # Displays SSL protocol used.
```

### 109. **`pydoc.render_doc`** – Generates documentation for Python objects.
```python
import pydoc
print(pydoc.render_doc(str))  # Displays documentation for Python strings.
```

### 110. **`ipaddress`** – Handles IPv4 and IPv6 addresses.
```python
import ipaddress

ip = ipaddress.ip_address("192.168.1.1")
print(ip.is_private)  # Checks if it's a private IP address.
```


### 111. **`array`** – Creates array-based storage for efficient memory use.
```python
import array

arr = array.array("i", [1, 2, 3, 4])
print(arr)  # Outputs: array('i', [1, 2, 3, 4])
```

### 112. **`time.strftime`** – Formats date and time.
```python
import time

print(time.strftime("%Y-%m-%d %H:%M:%S"))  # Outputs current time in a formatted string
```

### 113. **`mailbox`** – Reads and processes email mailboxes.
```python
import mailbox

mbox = mailbox.mbox("emails.mbox")
for message in mbox:
    print(message["subject"])  # Displays email subjects
```

### 114. **`html.entities`** – Works with HTML character entities.
```python
import html

encoded = html.escape("<html>Data</html>")
print(encoded)  # Outputs: &lt;html&gt;Data&lt;/html&gt;
```

### 115. **`math.gcd`** – Finds greatest common divisor.
```python
import math

print(math.gcd(48, 18))  # Outputs: 6 (GCD of 48 and 18)
```

### 116. **`smtpd`** – Implements a simple SMTP email server.
```python
import smtpd
import asyncore

server = smtpd.SMTPServer(("localhost", 1025), None)
asyncore.loop()
```

### 117. **`tkinter.Toplevel`** – Creates additional GUI windows.
```python
import tkinter as tk

root = tk.Tk()
new_window = tk.Toplevel(root)
tk.Label(new_window, text="New Window!").pack()
root.mainloop()
```

### 118. **`pydoc.help`** – Fetches documentation for modules interactively.
```python
import pydoc

help("math")  # Displays documentation for the `math` module
```

### 119. **`contextlib.suppress`** – Suppresses exceptions in a block of code.
```python
import contextlib

with contextlib.suppress(ZeroDivisionError):
    print(1 / 0)  # Won't raise an error, just silently ignores it
```

### 120. **`warnings`** – Controls and filters warning messages.
```python
import warnings

warnings.warn("This is a warning!", UserWarning)
```


### 121. **`stringprep`** – Prepares Unicode strings for network protocols.
```python
import stringprep

print(stringprep.in_table_a1("example"))  # Checks if "example" contains prohibited Unicode characters.
```

### 122. **`sunau`** – Works with Sun AU audio files.
```python
import sunau

with sunau.open("example.au", "rb") as audio:
    print(f"Channels: {audio.getnchannels()}, Sample rate: {audio.getframerate()}")
```

### 123. **`uuid.uuid5`** – Generates a UUID based on a name and SHA-1 hashing.
```python
import uuid

namespace = uuid.NAMESPACE_DNS
print(uuid.uuid5(namespace, "example.com"))  # Creates a deterministic UUID based on a domain name.
```

### 124. **`difflib.get_close_matches`** – Finds similar words.
```python
import difflib

words = ["apple", "banana", "cherry", "grape"]
print(difflib.get_close_matches("aple", words))  # Finds closest word matches.
```

### 125. **`getopt`** – Parses command-line options.
```python
import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
print(opts, args)  # Processes arguments like `python script.py --help`
```

### 126. **`hashlib.pbkdf2_hmac`** – Hashes passwords securely.
```python
import hashlib

salt = b"random_salt"
hashed_password = hashlib.pbkdf2_hmac("sha256", b"password123", salt, 100000)
print(hashed_password)
```

### 127. **`sched.scheduler`** – Schedules tasks.
```python
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def task():
    print("Task executed!")

scheduler.enter(5, 1, task)  # Runs task after 5 seconds.
scheduler.run()
```

### 128. **`trace.Trace`** – Traces Python execution.
```python
import trace

tracer = trace.Trace(count=True, trace=True)
tracer.run('print("Tracing execution!")')
```

### 129. **`xml.sax`** – Parses XML documents using SAX.
```python
import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print(f"Start tag: {name}")

xml.sax.parseString("<root><item>Hello</item></root>", MyHandler())
```

### 130. **`wave.open`** – Manipulates WAV files.
```python
import wave

with wave.open("example.wav", "rb") as wav_file:
    print(f"Channels: {wav_file.getnchannels()}, Sample rate: {wav_file.getframerate()}")
```

### 131. **`fileinput`** – Reads multiple files line by line.
```python
import fileinput

for line in fileinput.input(files=["file1.txt", "file2.txt"]):
    print(line.strip())  # Processes each line from multiple files
```

### 132. **`nturl2path`** – Converts URLs to Windows file paths.
```python
import nturl2path

url = "file:///C:/Users/Example/file.txt"
print(nturl2path.url2pathname(url))  # Converts URL to a local file path
```

### 133. **`dis`** – Disassembles Python bytecode.
```python
import dis

def example():
    return 42

print(dis.dis(example))  # Prints the bytecode instructions for the function
```

### 134. **`codeop`** – Compiles Python source code dynamically.
```python
import codeop

compiled = codeop.compile_command("print('Hello, Codeop!')")
exec(compiled)  # Executes the compiled Python command
```

### 135. **`marshal`** – Serializes Python objects in a fast, low-level way.
```python
import marshal

data = {"name": "Alice", "age": 30}
serialized = marshal.dumps(data)
deserialized = marshal.loads(serialized)
print(deserialized)  # Outputs: {'name': 'Alice', 'age': 30}
```

### 136. **`token`** – Defines Python token types.
```python
import token

print(token.tok_name[token.PLUS])  # Outputs: PLUS (symbol for '+')
```

### 137. **`tracemalloc`** – Tracks memory usage of a Python program.
```python
import tracemalloc

tracemalloc.start()
data = [x ** 2 for x in range(10000)]
snapshot = tracemalloc.take_snapshot()
print(snapshot.statistics("lineno"))  # Displays memory usage per line
```

### 138. **`site`** – Retrieves site-specific Python information.
```python
import site

print(site.getsitepackages())  # Lists all Python site-packages directories
```

### 139. **`tty`** – Provides terminal control functions (Unix-based).
```python
import tty, sys

tty.setcbreak(sys.stdin.fileno())  # Sets terminal mode for immediate input
```

### 140. **`xml.etree.ElementTree`** – Parses and modifies XML structures.
```python
import xml.etree.ElementTree as ET

xml_string = "<user><name>Alice</name><age>25</age></user>"
root = ET.fromstring(xml_string)
print(root.find("name").text)  # Outputs: Alice
```


### 141. **`webbrowser.open_new_tab`** – Opens a new browser tab.
```python
import webbrowser

webbrowser.open_new_tab("https://www.python.org")  # Opens Python's website in a new tab
```

### 142. **`rlcompleter`** – Enables tab-completion in interactive mode.
```python
import rlcompleter
import readline

readline.parse_and_bind("tab: complete")  # Enables autocompletion for Python commands
```

### 143. **`platform.processor`** – Retrieves processor information.
```python
import platform

print(platform.processor())  # Outputs CPU type
```

### 144. **`time.perf_counter`** – Measures precise execution timing.
```python
import time

start = time.perf_counter()
sum(range(1000000))  # Dummy computation
end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")
```

### 145. **`unicodedata.normalize`** – Normalizes Unicode characters.
```python
import unicodedata

text = "Café"
normalized = unicodedata.normalize("NFD", text)
print(normalized)  # Separates accent marks
```

### 146. **`colorsys.rgb_to_hsv`** – Converts RGB color values to HSV.
```python
import colorsys

h, s, v = colorsys.rgb_to_hsv(255, 0, 0)
print(f"HSV Color: {h:.2f}, {s:.2f}, {v:.2f}")  # Converts red color
```

### 147. **`json.load`** – Reads JSON data from a file.
```python
import json

with open("data.json", "r") as f:
    data = json.load(f)
print(data)  # Outputs parsed JSON data
```

### 148. **`sqlite3.connect`** – Creates and interacts with an SQLite database.
```python
import sqlite3

conn = sqlite3.connect(":memory:")  # Creates an in-memory database
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # Fetches all records
```

### 149. **`gzip.compress`** – Compresses data using Gzip.
```python
import gzip

data = b"Hello, compressed world!"
compressed = gzip.compress(data)
print(compressed)  # Outputs compressed binary data
```

### 150. **`csv.DictWriter`** – Writes dictionary data into a CSV file.
```python
import csv

data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)

print("CSV file written successfully!")
```

### 151. **`fcntl`** – Performs file control operations (Linux/Unix).
```python
import fcntl
import os

fd = os.open("example.txt", os.O_RDWR)
fcntl.flock(fd, fcntl.LOCK_EX)  # Locks the file for exclusive access
print("File locked!")
```

### 152. **`bz2`** – Compresses data using Bzip2.
```python
import bz2

data = b"Hello, Bzip2!"
compressed = bz2.compress(data)
print(compressed)  # Outputs compressed binary data
```

### 153. **`sched`** – Runs scheduled tasks.
```python
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def task():
    print("Task executed!")

scheduler.enter(3, 1, task)  # Runs task in 3 seconds
scheduler.run()
```

### 154. **`tabnanny`** – Detects inconsistent indentation in Python files.
```python
import tabnanny

tabnanny.check("script.py")  # Checks for bad indentation in 'script.py'
```

### 155. **`html.unescape`** – Converts HTML entities to text.
```python
import html

escaped_text = "&lt;p&gt;Hello!&lt;/p&gt;"
print(html.unescape(escaped_text))  # Outputs: <p>Hello!</p>
```

### 156. **`urllib.parse`** – Parses and manipulates URLs.
```python
import urllib.parse

url = "https://www.example.com/?search=python&lang=en"
parsed = urllib.parse.urlparse(url)
print(parsed.query)  # Extracts the query parameters
```

### 157. **`pydoc.render_doc`** – Generates module documentation dynamically.
```python
import pydoc

print(pydoc.render_doc("os"))  # Displays documentation for the `os` module
```

### 158. **`zipfile.ZipFile.extractall`** – Extracts all files from a ZIP archive.
```python
import zipfile

with zipfile.ZipFile("example.zip", "r") as zipf:
    zipf.extractall("extracted_files")  # Extracts contents into 'extracted_files' directory
```

### 159. **`statistics.median_grouped`** – Calculates the grouped median.
```python
import statistics

data = [10, 20, 30, 40, 50]
print(statistics.median_grouped(data))  # Outputs the grouped median
```

### 160. **`wave.open.writeframesraw`** – Writes raw audio frames to a WAV file.
```python
import wave

with wave.open("example.wav", "wb") as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(44100)
    wav_file.writeframesraw(b"\x00\x01\x02\x03")  # Writes raw data
```


### 161. **`grp`** – Works with Unix group database (Linux).
```python
import grp

group_info = grp.getgrnam("sudo")  # Retrieves info about the 'sudo' group
print(group_info)
```

### 162. **`pwd`** – Retrieves Unix user account details (Linux).
```python
import pwd

user_info = pwd.getpwnam("username")  # Replace 'username' with an actual user
print(user_info)
```

### 163. **`resource`** – Manages system resource limits (Linux).
```python
import resource

soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print(f"Max open files: Soft limit={soft}, Hard limit={hard}")
```

### 164. **`socket.gethostname`** – Gets the computer's hostname.
```python
import socket

print(socket.gethostname())  # Outputs the current machine name
```

### 165. **`ssl.wrap_socket`** – Wraps a socket in SSL/TLS for secure communication.
```python
import ssl
import socket

sock = socket.socket()
wrapped_sock = ssl.wrap_socket(sock)
print("SSL socket created!")
```

### 166. **`traceback.print_exc`** – Prints full error traceback details.
```python
import traceback

try:
    1 / 0
except Exception:
    traceback.print_exc()  # Prints detailed error information
```

### 167. **`string.ascii_lowercase`** – Accesses lowercase alphabet characters.
```python
import string

print(string.ascii_lowercase)  # Outputs: abcdefghijklmnopqrstuvwxyz
```

### 168. **`uuid.NAMESPACE_URL`** – Creates a deterministic UUID based on a URL.
```python
import uuid

print(uuid.uuid5(uuid.NAMESPACE_URL, "https://www.example.com"))  # Creates a UUID
```

### 169. **`gzip.open`** – Reads and writes Gzip-compressed files.
```python
import gzip

with gzip.open("example.gz", "wt") as f:
    f.write("Hello, Gzip!")

with gzip.open("example.gz", "rt") as f:
    print(f.read())  # Reads the compressed file
```

### 170. **`random.choices`** – Selects random elements with weights.
```python
import random

options = ["apple", "banana", "cherry"]
weights = [0.1, 0.6, 0.3]
print(random.choices(options, weights=weights, k=5))  # Generates weighted random choices
```


### 171. **`tokenize`** – Reads and tokenizes Python source code.
```python
import tokenize
from io import BytesIO

code = b"print('Hello, Python!')"
for token in tokenize.tokenize(BytesIO(code).readline):
    print(token)  # Displays each token from the Python code
```

### 172. **`math.factorial`** – Computes the factorial of a number.
```python
import math

print(math.factorial(5))  # Outputs: 120 (5!)
```

### 173. **`shutil.move`** – Moves files between locations.
```python
import shutil

shutil.move("source.txt", "destination.txt")  # Moves the file
```

### 174. **`xml.dom.pulldom`** – Parses large XML files efficiently.
```python
import xml.dom.pulldom

doc = xml.dom.pulldom.parseString("<root><item>Hello</item></root>")
for event, node in doc:
    if event == "START_ELEMENT" and node.tagName == "item":
        print("Found item:", node.toxml())
```

### 175. **`email.mime.multipart`** – Creates multipart emails.
```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg["From"] = "you@example.com"
msg["To"] = "recipient@example.com"
msg["Subject"] = "Multipart Email"

msg.attach(MIMEText("Hello, this is a multipart email.", "plain"))
print(msg.as_string())  # Prints formatted email structure
```

### 176. **`zipfile.ZipFile.writestr`** – Writes data into a ZIP archive without an actual file.
```python
import zipfile

with zipfile.ZipFile("example.zip", "w") as zipf:
    zipf.writestr("greeting.txt", "Hello, ZIP!")  # Stores text directly inside the ZIP
```

### 177. **`subprocess.Popen`** – Runs system commands dynamically.
```python
import subprocess

process = subprocess.Popen(["echo", "Hello, subprocess!"], stdout=subprocess.PIPE)
output, _ = process.communicate()
print(output.decode())  # Outputs: Hello, subprocess!
```

### 178. **`ssl.create_default_context`** – Establishes an SSL/TLS context.
```python
import ssl

context = ssl.create_default_context()
print(context.options)  # Displays current SSL options
```

### 179. **`statistics.mode`** – Finds the most frequent value in a dataset.
```python
import statistics

data = [2, 3, 2, 4, 2, 5]
print(statistics.mode(data))  # Outputs: 2 (most common value)
```

### 180. **`ipaddress.IPv4Network`** – Works with IP networks.
```python
import ipaddress

network = ipaddress.IPv4Network("192.168.1.0/24")
for ip in network:
    print(ip)  # Lists all IPs in the network
```


### 181. **`os.path.exists`** – Checks if a file or directory exists.
```python
import os

print(os.path.exists("test.txt"))  # Outputs True if the file exists, False otherwise
```

### 182. **`errno.errorcode`** – Maps error codes to their names.
```python
import errno

print(errno.errorcode[errno.EPERM])  # Outputs 'EPERM' (Error for permission denied)
```

### 183. **`http.server`** – Runs a simple web server.
```python
import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler
server = socketserver.TCPServer(("localhost", 8080), handler)

print("Serving on http://localhost:8080")
server.serve_forever()
```

### 184. **`pdb.set_trace`** – Starts an interactive debugger.
```python
import pdb

def test_function():
    a = 5
    pdb.set_trace()  # Starts debugger here
    b = a * 2
    return b

test_function()
```

### 185. **`contextlib.redirect_stdout`** – Redirects standard output.
```python
import contextlib

with open("output.txt", "w") as f:
    with contextlib.redirect_stdout(f):
        print("This gets written to output.txt instead of appearing in console")
```

### 186. **`argparse.ArgumentParser.add_argument`** – Adds a command-line argument.
```python
import argparse

parser = argparse.ArgumentParser(description="Demo argument parser")
parser.add_argument("--name", type=str, help="Your name")
args = parser.parse_args()
print(f"Hello, {args.name}!")  # Run: python script.py --name Alice
```

### 187. **`email.mime.text.MIMEText`** – Creates simple email messages.
```python
from email.mime.text import MIMEText

msg = MIMEText("Hello, Email!")
msg["Subject"] = "Python Email Test"
msg["From"] = "you@example.com"
msg["To"] = "recipient@example.com"

print(msg.as_string())  # Prints the formatted email
```

### 188. **`shlex.quote`** – Safely formats command-line arguments.
```python
import shlex

text = "Hello & goodbye"
safe_text = shlex.quote(text)
print(safe_text)  # Outputs: 'Hello & goodbye' (safe for shell commands)
```

### 189. **`subprocess.run`** – Runs external commands.
```python
import subprocess

output = subprocess.run(["echo", "Hello, subprocess!"], capture_output=True, text=True)
print(output.stdout)  # Outputs: Hello, subprocess!
```

### 190. **`socket.getaddrinfo`** – Resolves hostnames to IP addresses.
```python
import socket

print(socket.getaddrinfo("example.com", None))  # Displays IP resolution details
```


### 191. **`xmlrpc.server`** – Implements an XML-RPC server.
```python
from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(x, y):
    return x + y

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add_numbers, "add")
print("Serving XML-RPC on port 8000...")
server.serve_forever()
```

### 192. **`select.poll`** – Monitors multiple I/O file descriptors for events.
```python
import select

poller = select.poll()
print(poller)  # Creates a poll object
```

### 193. **`queue.LifoQueue`** – Implements a last-in, first-out (LIFO) queue.
```python
import queue

stack = queue.LifoQueue()
stack.put("First")
stack.put("Second")
print(stack.get())  # Outputs: "Second" (Last in, first out)
```

### 194. **`difflib.Differ`** – Compares sequences line by line.
```python
import difflib

text1 = ["Hello", "world"]
text2 = ["Hello", "Python"]

differ = difflib.Differ()
print("\n".join(differ.compare(text1, text2)))  # Outputs detailed differences
```

### 195. **`tracemalloc.get_traced_memory`** – Tracks memory usage in Python.
```python
import tracemalloc

tracemalloc.start()
data = [x ** 2 for x in range(10000)]
print(tracemalloc.get_traced_memory())  # Outputs memory consumption
```

### 196. **`argparse.Namespace`** – Stores parsed command-line arguments.
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")
args = parser.parse_args()
print(args.name)  # Outputs command-line argument value
```

### 197. **`os.urandom`** – Generates cryptographically secure random bytes.
```python
import os

random_bytes = os.urandom(16)
print(random_bytes)  # Outputs a secure random byte sequence
```

### 198. **`subprocess.DEVNULL`** – Silences command output.
```python
import subprocess

subprocess.run(["echo", "Hello"], stdout=subprocess.DEVNULL)  # No output displayed
```

### 199. **`zipfile.is_zipfile`** – Checks if a file is a valid ZIP archive.
```python
import zipfile

print(zipfile.is_zipfile("example.zip"))  # Outputs True if valid ZIP file
```

### 200. **`ssl.get_default_verify_paths`** – Lists SSL verification paths.
```python
import ssl

print(ssl.get_default_verify_paths())  # Displays default SSL paths
```


### 201. **`tarfile.add`** – Adds files to a tar archive.
```python
import tarfile

with tarfile.open("example.tar.gz", "w:gz") as tar:
    tar.add("test.txt")  # Adds 'test.txt' to the archive
```

### 202. **`pydoc.help`** – Displays Python documentation interactively.
```python
import pydoc

help("math")  # Shows documentation for the 'math' module
```

### 203. **`base64.b64decode`** – Decodes Base64-encoded data.
```python
import base64

encoded = base64.b64encode(b"Hello, Base64!")
print(base64.b64decode(encoded))  # Outputs: b'Hello, Base64!'
```

### 204. **`hashlib.sha512`** – Generates a SHA-512 hash.
```python
import hashlib

data = b"secure_password"
hashed = hashlib.sha512(data).hexdigest()
print(hashed)  # Outputs the SHA-512 hash of the input
```

### 205. **`shutil.copytree`** – Recursively copies a directory.
```python
import shutil

shutil.copytree("source_folder", "destination_folder")  # Copies all contents
```

### 206. **`contextlib.suppress`** – Suppresses specific exceptions.
```python
import contextlib

with contextlib.suppress(ZeroDivisionError):
    print(1 / 0)  # Won't cause an error
```

### 207. **`xml.etree.ElementTree.dump`** – Prints XML structure.
```python
import xml.etree.ElementTree as ET

xml_data = "<user><name>Alice</name></user>"
root = ET.fromstring(xml_data)
ET.dump(root)  # Outputs the XML structure in a formatted way
```

### 208. **`subprocess.PIPE`** – Captures command output.
```python
import subprocess

process = subprocess.run(["echo", "Hello"], stdout=subprocess.PIPE, text=True)
print(process.stdout)  # Outputs: Hello
```

### 209. **`threading.Event`** – Synchronizes threads.
```python
import threading

event = threading.Event()

def worker():
    print("Waiting for event...")
    event.wait()
    print("Event received!")

thread = threading.Thread(target=worker)
thread.start()

event.set()  # Triggers the event
```

### 210. **`itertools.accumulate`** – Performs cumulative calculations.
```python
import itertools

data = [1, 2, 3, 4]
print(list(itertools.accumulate(data)))  # Outputs: [1, 3, 6, 10] (running sum)
```

### 211. **`functools.partial`** – Creates a partially applied function.
```python
import functools

def multiply(x, y):
    return x * y

double = functools.partial(multiply, 2)
print(double(5))  # Outputs: 10 (2 * 5)
```

### 212. **`calendar.isleap`** – Checks if a year is a leap year.
```python
import calendar

print(calendar.isleap(2024))  # Outputs: True (2024 is a leap year)
```

### 213. **`decimal.Decimal`** – Handles precise floating-point arithmetic.
```python
import decimal

num = decimal.Decimal("0.1") + decimal.Decimal("0.2")
print(num)  # Outputs: 0.3 (without floating-point rounding issues)
```

### 214. **`os.walk`** – Recursively lists files in directories.
```python
import os

for root, dirs, files in os.walk("."):
    print("Directory:", root)
    for file in files:
        print("File:", file)
```

### 215. **`itertools.combinations`** – Finds unique combinations of elements.
```python
import itertools

items = [1, 2, 3]
print(list(itertools.combinations(items, 2)))  # Outputs: [(1, 2), (1, 3), (2, 3)]
```

### 216. **`argparse.ArgumentParser.parse_args`** – Parses command-line arguments dynamically.
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()
print(args.verbose)  # Outputs True/False based on command-line input
```

### 217. **`collections.Counter`** – Counts occurrences in lists.
```python
import collections

data = ["apple", "banana", "apple", "cherry", "banana"]
counter = collections.Counter(data)
print(counter)  # Outputs: {'apple': 2, 'banana': 2, 'cherry': 1}
```

### 218. **`sqlite3.Row`** – Uses dictionary-style access for database rows.
```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
conn.commit()

cursor.execute("SELECT * FROM users")
row = cursor.fetchone()
print(row["name"])  # Outputs: Alice
```

### 219. **`threading.Timer`** – Delays execution of a function.
```python
import threading

def delayed_task():
    print("Task executed after delay!")

timer = threading.Timer(5, delayed_task)  # Executes after 5 seconds
timer.start()
```

### 220. **`email.mime.image.MIMEImage`** – Embeds images in emails.
```python
from email.mime.image import MIMEImage

with open("example.png", "rb") as img_file:
    img = MIMEImage(img_file.read())

print(img)  # Outputs MIME image structure
```




### 221. **`contextlib.closing`** – Ensures cleanup of resources when closing.
```python
import contextlib
import socket

with contextlib.closing(socket.socket()) as s:
    print("Socket will close automatically!")
```

### 222. **`http.client`** – Sends HTTP requests.
```python
import http.client

conn = http.client.HTTPConnection("www.example.com")
conn.request("GET", "/")
response = conn.getresponse()
print(response.status, response.reason)  # Outputs HTTP status code
```

### 223. **`xmlrpc.client.ServerProxy`** – Calls remote XML-RPC services.
```python
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://example.com:8000")
print(proxy.system.listMethods())  # Lists available remote methods
```

### 224. **`filecmp.dircmp`** – Compares directories for differences.
```python
import filecmp

comparison = filecmp.dircmp("dir1", "dir2")
comparison.report()  # Prints comparison results
```

### 225. **`uuid.NAMESPACE_DNS`** – Generates a deterministic UUID based on domain names.
```python
import uuid

print(uuid.uuid5(uuid.NAMESPACE_DNS, "example.com"))  # Creates a UUID
```

### 226. **`calendar.monthcalendar`** – Returns a matrix representing a month's calendar.
```python
import calendar

print(calendar.monthcalendar(2025, 6))  # Outputs June 2025's calendar structure
```

### 227. **`math.isclose`** – Checks if two numbers are close to each other.
```python
import math

print(math.isclose(0.1 + 0.2, 0.3))  # Handles floating-point precision issues
```

### 228. **`shutil.disk_usage`** – Retrieves system disk usage.
```python
import shutil

usage = shutil.disk_usage("/")
print(f"Total: {usage.total}, Used: {usage.used}, Free: {usage.free}")
```

### 229. **`sqlite3.connect`** – Interacts with SQLite databases.
```python
import sqlite3

conn = sqlite3.connect(":memory:")  # Creates an in-memory database
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # Fetches all records
```

### 230. **`threading.Lock`** – Manages thread-safe operations.
```python
import threading

lock = threading.Lock()

def critical_section():
    with lock:
        print("Safe execution within a thread lock!")

thread1 = threading.Thread(target=critical_section)
thread2 = threading.Thread(target=critical_section)
thread1.start()
thread2.start()
```


### 231. **`errno.EACCES`** – Represents "Permission denied" error code.
```python
import errno

print(errno.EACCES)  # Outputs standard error code for permission issues
```

### 232. **`pdb.run`** – Runs Python code inside the debugger.
```python
import pdb

pdb.run('print("Debugging this execution!")')  # Starts interactive debugging session
```

### 233. **`zipfile.ZipFile.testzip`** – Verifies integrity of a ZIP archive.
```python
import zipfile

with zipfile.ZipFile("example.zip", "r") as zipf:
    print(zipf.testzip())  # Outputs any corrupt file names in the ZIP archive
```

### 234. **`functools.cache`** – Caches function results to improve performance.
```python
import functools

@functools.cache
def compute(x):
    print("Computing...")
    return x ** 2

print(compute(5))  # Caches the computation
print(compute(5))  # Uses cached result
```

### 235. **`calendar.weekday`** – Determines the day of the week for a specific date.
```python
import calendar

print(calendar.weekday(2025, 6, 13))  # Outputs: Day index (0=Monday, 6=Sunday)
```

### 236. **`random.sample`** – Selects unique random elements.
```python
import random

data = [1, 2, 3, 4, 5]
print(random.sample(data, 3))  # Outputs three unique random numbers
```

### 237. **`shutil.which`** – Locates the full path of an executable file.
```python
import shutil

print(shutil.which("python"))  # Outputs path to Python executable
```

### 238. **`itertools.product`** – Computes Cartesian product of input sets.
```python
import itertools

lists = [[1, 2], ["A", "B"]]
print(list(itertools.product(*lists)))  # Outputs all possible combinations
```

### 239. **`traceback.extract_tb`** – Extracts formatted traceback details.
```python
import traceback

try:
    1 / 0
except ZeroDivisionError as e:
    print(traceback.extract_tb(e.__traceback__))  # Retrieves detailed error information
```

### 240. **`ssl.PROTOCOL_TLSv1_2`** – Enforces TLS 1.2 encryption.
```python
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
print(context.protocol)  # Confirms use of TLSv1.2
```


### 241. **`statistics.stdev`** – Calculates standard deviation.
```python
import statistics

data = [10, 20, 30, 40, 50]
print(statistics.stdev(data))  # Outputs: 15.81 (standard deviation)
```

### 242. **`shutil.rmtree`** – Deletes a directory and all its contents.
```python
import shutil

shutil.rmtree("target_folder")  # Recursively deletes the entire folder
```

### 243. **`socket.AF_INET`** – Defines IPv4 socket communication.
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created with IPv4 support")
```

### 244. **`ssl.SSLContext.load_cert_chain`** – Loads SSL certificates for secure connections.
```python
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")  # Load certificate
```

### 245. **`subprocess.call`** – Executes a command synchronously.
```python
import subprocess

subprocess.call(["echo", "Hello, subprocess!"])  # Runs the command
```

### 246. **`calendar.setfirstweekday`** – Changes the starting weekday.
```python
import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.monthcalendar(2025, 6))  # Displays June 2025 with Sunday as first day
```

### 247. **`uuid.uuid3`** – Generates a UUID using MD5 hashing.
```python
import uuid

namespace = uuid.NAMESPACE_DNS
print(uuid.uuid3(namespace, "example.com"))  # Creates a deterministic UUID
```

### 248. **`contextlib.nested`** – Manages multiple context managers (for Python 2, deprecated).
```python
import contextlib

with contextlib.ExitStack() as stack:
    f1 = stack.enter_context(open("file1.txt"))
    f2 = stack.enter_context(open("file2.txt"))
    print("Multiple files opened safely")
```

### 249. **`hashlib.blake2b`** – Generates BLAKE2b hash (fast, secure hashing).
```python
import hashlib

data = b"super_secure_password"
hashed = hashlib.blake2b(data).hexdigest()
print(hashed)  # Outputs a secure hash
```

### 250. **`pydoc.cli`** – Runs Python documentation tool via command line.
```bash
python -m pydoc math  # Displays documentation for the `math` module
```


### 251. **`smtplib.SMTP_SSL`** – Sends emails securely using SMTP over SSL.
```python
import smtplib

server = smtplib.SMTP_SSL("smtp.example.com", 465)
server.login("your_email@example.com", "your_password")
server.sendmail("your_email@example.com", "recipient@example.com", "Secure email test!")
server.quit()
```

### 252. **`fcntl.flock`** – Locks files for exclusive access (Unix/Linux).
```python
import fcntl
import os

fd = os.open("example.txt", os.O_RDWR)
fcntl.flock(fd, fcntl.LOCK_EX)  # Locks the file
print("File locked for exclusive access!")
```

### 253. **`pstats.Stats`** – Analyzes performance profiling data.
```python
import pstats

stats = pstats.Stats("profiling_data.prof")
stats.strip_dirs().sort_stats("time").print_stats(10)  # Displays top 10 time-consuming functions
```

### 254. **`imghdr.what`** – Determines the format of an image file.
```python
import imghdr

print(imghdr.what("example.jpg"))  # Outputs: jpeg (or other detected image type)
```

### 255. **`contextlib.ExitStack`** – Manages multiple resources safely.
```python
import contextlib

with contextlib.ExitStack() as stack:
    f1 = stack.enter_context(open("file1.txt"))
    f2 = stack.enter_context(open("file2.txt"))
    print("Multiple files opened safely!")
```

### 256. **`os.getlogin`** – Retrieves the current system username.
```python
import os

print(os.getlogin())  # Outputs the logged-in username
```

### 257. **`socket.gethostbyname`** – Resolves a hostname to an IP address.
```python
import socket

print(socket.gethostbyname("example.com"))  # Outputs the IP address
```

### 258. **`ssl.CERT_REQUIRED`** – Enforces strict certificate validation.
```python
import ssl

context = ssl.create_default_context()
context.verify_mode = ssl.CERT_REQUIRED
print("SSL context configured for strict validation!")
```

### 259. **`pathlib.Path.mkdir`** – Creates directories dynamically.
```python
from pathlib import Path

Path("new_directory").mkdir(parents=True, exist_ok=True)
print("Directory created!")
```

### 260. **`html.escape`** – Converts characters to HTML-safe entities.
```python
import html

print(html.escape("<Hello & Goodbye>"))  # Outputs: &lt;Hello &amp; Goodbye&gt;
```



### 261. **`contextlib.nullcontext`** – A no-op context manager.
```python
import contextlib

with contextlib.nullcontext():
    print("No special handling here!")  # Acts like an empty `with` block
```

### 262. **`socket.SOCK_DGRAM`** – Defines UDP socket communication.
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Created a UDP socket")
```

### 263. **`shutil.chown`** – Changes file owner and group (Unix).
```python
import shutil

shutil.chown("example.txt", user="new_user", group="new_group")  # Changes owner
```

### 264. **`functools.reduce`** – Applies a function cumulatively to a sequence.
```python
import functools

numbers = [1, 2, 3, 4]
product = functools.reduce(lambda x, y: x * y, numbers)
print(product)  # Outputs: 24 (1 × 2 × 3 × 4)
```

### 265. **`statistics.quantiles`** – Computes quantiles of a dataset.
```python
import statistics

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(statistics.quantiles(data, n=4))  # Outputs quartiles
```

### 266. **`calendar.yeardayscalendar`** – Retrieves a year’s calendar structure.
```python
import calendar

print(calendar.yeardayscalendar(2025, width=3))  # Outputs the full year calendar as structured data
```

### 267. **`subprocess.getoutput`** – Runs a shell command and gets output.
```python
import subprocess

output = subprocess.getoutput("echo Hello, subprocess!")
print(output)  # Outputs: Hello, subprocess!
```

### 268. **`pathlib.Path.resolve`** – Gets the absolute path of a file.
```python
from pathlib import Path

path = Path("example.txt")
print(path.resolve())  # Outputs full path
```

### 269. **`json.JSONDecodeError`** – Handles JSON decoding errors.
```python
import json

try:
    json.loads("{invalid_json}")
except json.JSONDecodeError as e:
    print(f"JSON error: {e}")
```

### 270. **`email.mime.audio.MIMEAudio`** – Embeds audio files into an email.
```python
from email.mime.audio import MIMEAudio

with open("example.wav", "rb") as audio_file:
    audio = MIMEAudio(audio_file.read(), _subtype="wav")

print(audio)  # Outputs MIME structure for an audio file
```


### 271. **`imaplib.IMAP4_SSL`** – Connects securely to an IMAP email server.
```python
import imaplib

mail = imaplib.IMAP4_SSL("imap.example.com")
mail.login("your_email@example.com", "your_password")
mail.select("inbox")
status, emails = mail.search(None, "ALL")
print("Emails:", emails)
```

### 272. **`math.dist`** – Calculates the Euclidean distance between two points.
```python
import math

point1 = (1, 2)
point2 = (4, 6)
print(math.dist(point1, point2))  # Outputs: 5.0
```

### 273. **`socket.getfqdn`** – Returns the fully qualified domain name of the current host.
```python
import socket

print(socket.getfqdn())  # Outputs full domain name of local machine
```

### 274. **`zipfile.ZipFile.getinfo`** – Retrieves metadata about a file inside a ZIP archive.
```python
import zipfile

with zipfile.ZipFile("example.zip", "r") as zipf:
    info = zipf.getinfo("file.txt")
    print(info.file_size, info.compress_size)  # Displays file sizes
```

### 275. **`traceback.format_exception_only`** – Extracts exception message formatting.
```python
import traceback

try:
    1 / 0
except ZeroDivisionError as e:
    print(traceback.format_exception_only(type(e), e))  # Extracts just the error message
```

### 276. **`subprocess.check_output`** – Runs a command and retrieves the output.
```python
import subprocess

output = subprocess.check_output(["echo", "Hello, subprocess!"], text=True)
print(output.strip())  # Outputs: Hello, subprocess!
```

### 277. **`ssl.ALPN_PROTOCOLS`** – Lists supported Application Layer Protocol Negotiation (ALPN) protocols.
```python
import ssl

context = ssl.create_default_context()
print(context.alpn_protocols)  # Lists ALPN protocols used in the SSL session
```

### 278. **`pstats.dump_stats`** – Saves profiling results to a file.
```python
import pstats

stats = pstats.Stats("profiling_data.prof")
stats.dump_stats("output.prof")  # Saves profiling data to a file
```

### 279. **`pathlib.Path.is_symlink`** – Checks if a file is a symbolic link.
```python
from pathlib import Path

path = Path("example_link.txt")
print(path.is_symlink())  # Outputs True/False
```

### 280. **`random.uniform`** – Generates a random floating-point number.
```python
import random

print(random.uniform(1, 10))  # Outputs a float between 1 and 10
```

### 281. **`calendar.month_name`** – Retrieves month names dynamically.
```python
import calendar

print(list(calendar.month_name)[1:])  # Outputs: ['January', 'February', ..., 'December']
```

### 282. **`xml.etree.ElementTree.iterparse`** – Efficiently processes large XML files.
```python
import xml.etree.ElementTree as ET

for event, elem in ET.iterparse("large_file.xml"):
    print(event, elem.tag)  # Outputs event type and tag name as XML is read
```

### 283. **`ssl.HAS_TLSv1_3`** – Checks if TLS 1.3 is supported.
```python
import ssl

print(ssl.HAS_TLSv1_3)  # Outputs: True if TLS 1.3 is available
```

### 284. **`json.dumps(indent=4)`** – Formats JSON output with indentation.
```python
import json

data = {"name": "Alice", "age": 25, "city": "New York"}
print(json.dumps(data, indent=4))  # Pretty-prints JSON with 4-space indentation
```

### 285. **`random.shuffle`** – Shuffles a list randomly.
```python
import random

items = ["apple", "banana", "cherry"]
random.shuffle(items)
print(items)  # Outputs shuffled list order
```

### 286. **`time.time_ns`** – Retrieves time in nanoseconds.
```python
import time

print(time.time_ns())  # Outputs current time in nanoseconds
```

### 287. **`pathlib.Path.iterdir`** – Iterates over files in a directory.
```python
from pathlib import Path

for file in Path(".").iterdir():
    print(file)  # Outputs each file in the current directory
```

### 288. **`statistics.pstdev`** – Calculates population standard deviation.
```python
import statistics

data = [10, 20, 30, 40, 50]
print(statistics.pstdev(data))  # Outputs: 14.14 (population standard deviation)
```

### 289. **`shutil.get_terminal_size`** – Retrieves terminal width and height.
```python
import shutil

print(shutil.get_terminal_size())  # Outputs terminal size in columns and rows
```

### 290. **`subprocess.Popen.communicate`** – Captures input and output in a subprocess.
```python
import subprocess

process = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
output, _ = process.communicate("Hello, subprocess!\n")
print(output.strip())  # Outputs: Hello, subprocess!
```


### 291. **`pathlib.Path.is_file`** – Checks if a path is a file.
```python
from pathlib import Path

path = Path("example.txt")
print(path.is_file())  # Outputs True if it's a file, False otherwise
```

### 292. **`subprocess.run(check=True)`** – Raises an exception if a command fails.
```python
import subprocess

subprocess.run(["ls", "non_existent_file"], check=True)  # Will raise an exception if the file doesn't exist
```

### 293. **`random.choices`** – Selects random elements with weights.
```python
import random

options = ["apple", "banana", "cherry"]
weights = [0.1, 0.6, 0.3]
print(random.choices(options, weights=weights, k=5))  # Generates weighted random choices
```

### 294. **`contextlib.suppress`** – Silently handles exceptions.
```python
import contextlib

with contextlib.suppress(ZeroDivisionError):
    print(1 / 0)  # No error will be raised
```

### 295. **`email.mime.multipart.MIMEMultipart`** – Creates multipart emails.
```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg["From"] = "you@example.com"
msg["To"] = "recipient@example.com"
msg["Subject"] = "Multipart Email"

msg.attach(MIMEText("Hello, this is a multipart email.", "plain"))
print(msg.as_string())  # Prints formatted email structure
```

### 296. **`math.prod`** – Computes the product of a sequence.
```python
import math

numbers = [2, 3, 4]
print(math.prod(numbers))  # Outputs: 24 (2 * 3 * 4)
```

### 297. **`shutil.copyfileobj`** – Copies file objects efficiently.
```python
import shutil

with open("source.txt", "rb") as src, open("destination.txt", "wb") as dest:
    shutil.copyfileobj(src, dest)
```

### 298. **`zipfile.ZipFile.extract`** – Extracts a specific file from a ZIP archive.
```python
import zipfile

with zipfile.ZipFile("example.zip", "r") as zipf:
    zipf.extract("file.txt", "output_directory")  # Extracts only 'file.txt'
```

### 299. **`time.monotonic`** – Measures time that cannot go backward.
```python
import time

start = time.monotonic()
time.sleep(1)
end = time.monotonic()
print(f"Elapsed time: {end - start:.2f} seconds")
```

### 300. **`ssl.get_server_certificate`** – Retrieves a server's SSL certificate.
```python
import ssl

cert = ssl.get_server_certificate(("www.python.org", 443))
print(cert)  # Displays the SSL certificate
```




