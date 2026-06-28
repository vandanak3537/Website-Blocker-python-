# Website Blocker using Python

## Overview

Website Blocker is a Python application that improves productivity by restricting access to distracting websites during specified working hours. It automatically modifies the Windows **hosts** file to block selected websites and restores access once the blocking period ends.

## Features

* Blocks selected websites during working hours.
* Automatically unblocks websites after working hours.
* Uses the Windows hosts file for website redirection.
* Time-based automation using Python.
* Lightweight and easy to customize.
* No external libraries required.

## Technologies Used

* Python
* datetime
* time
* File Handling

## Project Structure

```text
Website-Blocker/
│── website_blocker.py
│── README.md
```

## How It Works

1. Reads the current system time.
2. Checks whether the current time falls within the blocking schedule.
3. During working hours, redirects selected websites to `127.0.0.1` by updating the Windows hosts file.
4. Outside working hours, removes the blocked entries to restore normal website access.
5. Repeats the process at regular intervals.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vandanak3537/Website-Blocker.git
```

2. Navigate to the project directory:

```bash
cd Website-Blocker
```

3. Run the script as Administrator:

```bash
python website_blocker.py
```

## Configuration

Modify the `websites` list in the script to add or remove websites:

```python
websites = [
    "www.youtube.com",
    "youtube.com",
    "www.instagram.com",
    "instagram.com",
    "www.facebook.com",
    "facebook.com"
]
```

You can also change the blocking hours by editing the time condition in the code.

## Future Improvements

* Graphical User Interface (GUI)
* Password-protected settings
* Custom schedules
* Cross-platform support
* Activity logging

## Sample Output

```text
Working hours... Blocking websites.
Free time... Unblocking websites.
```

## License

This project is available under the MIT License.



