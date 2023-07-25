# Lecture Outline: Python Automation + DevOps

## 1. Introduction to Python Automation and DevOps (15 minutes)

"Welcome everyone. Today, we will discuss an important subject in software development: Automation and DevOps, specifically through the lens of Python programming.

> ASK: Why Python is the primary automation language?

- Readability and simplicity: Python emphasizes code readability and uses a clean syntax, which makes it easier to understand and write. Its design philosophy encourages clear and concise code, reducing the learning curve for beginners and allowing for rapid development.
  
- Large and active community: Python has a vibrant and supportive community of developers who contribute to its ecosystem by creating libraries, frameworks, and tools. This extensive community support means that developers can find solutions to their automation needs quickly and efficiently.
  
- Extensive libraries and frameworks: Python provides a wide range of libraries and frameworks that simplify automation tasks. For example, popular libraries like Selenium, Beautiful Soup, and Requests enable web automation, data extraction, and HTTP requests, respectively. These libraries, along with many others, make it easy to automate various aspects of software development, system administration, and data processing. 
  
- Cross-platform compatibility: Python is a highly portable language, capable of running on various platforms such as Windows, macOS, and Linux. This cross-platform compatibility makes it suitable for automating tasks on different operating systems, allowing automation scripts to be easily shared and executed across multiple environments.
  
- Integration capabilities: Python can seamlessly integrate with other languages and technologies, making it a versatile choice for automation. It has robust support for interfacing with external systems through APIs, databases, and web services. Additionally, Python can be embedded within larger software systems and can be extended with modules written in other languages.
  
- Data processing and analysis: Python has gained significant popularity in the data science and machine learning domains. Its extensive libraries, such as NumPy, Pandas, and scikit-learn, provide powerful tools for data manipulation, analysis, and modeling. This makes Python an ideal choice for automating data-related tasks, including data extraction, cleansing, transformation, and visualization.
  
- Industry adoption and job market: Python's widespread adoption in various industries, including software development, scientific research, web development, and system administration, has contributed to its prominence as an automation language. The demand for Python automation skills in the job market is high, which further encourages developers to choose Python as their primary language for automation.

> ASK: What is the Importance of Automation

- Automation refers to the process of making systems or processes operate automatically. This can be automating repetitive tasks, like creating folders, moving files, etc., to more complex processes, like deployment of software across different platforms.

> ASK: What is this thing called DevOps?

- Key principles and practices of DevOps include:

- Automation: DevOps promotes the automation of repetitive tasks, such as building, testing, and deploying software. Automation helps eliminate manual errors, accelerates the delivery process, and ensures consistency in environments.

- Continuous Integration and Continuous Delivery (CI/CD): CI/CD is a fundamental practice in DevOps. It involves integrating code changes frequently, running automated tests, and continuously delivering software to production environments. This enables faster feedback cycles, reduces risks, and allows for rapid iteration and deployment of new features.

- Infrastructure as Code (IaC): Infrastructure as Code is the practice of managing infrastructure and configuration through machine-readable definition files. It allows teams to treat infrastructure provisioning, deployment, and configuration as code, enabling version control, automation, and reproducibility of infrastructure changes.

- Collaboration and Communication: DevOps emphasizes effective collaboration and communication between development teams, operations teams, and other stakeholders involved in the software delivery process. This includes breaking down silos, encouraging cross-functional teams, and sharing knowledge and responsibilities.

- Monitoring and Feedback: DevOps advocates for proactive monitoring of applications and infrastructure, collecting and analyzing metrics, logs, and user feedback. Monitoring helps detect issues, identify performance bottlenecks, and drive continuous improvement.

- Agile and Lean Practices: DevOps aligns with agile and lean principles by promoting iterative development, customer-centricity, and continuous improvement. It emphasizes shorter development cycles, small incremental changes, and rapid feedback to quickly respond to evolving business needs.

In short, Python is a versatile language and is widely used in both automation and DevOps, due to its simplicity and wide range of libraries and modules. DevOps is the liason between software developers and operations.

Today, we will delve into some of these tools and learn how we can utilize Python for Automation and DevOps.

Do you have any questions before we proceed?"

**Anticipated Questions:**

1. **Why is automation important in software development?**

   *Automation is crucial in software development because it helps save time by reducing repetitive tasks, helps find bugs and issues earlier in the development cycle, increases productivity, and, in turn, reduces costs. It also helps in ensuring that the software product is of the highest quality.*

2. **Why is Python a good choice for automation and DevOps?**

   *Python is a high-level, interpreted language that has a clear, readable syntax and is easy to learn, which makes it a popular choice for automation scripts. Python also has a large standard library and additional modules that support a wide range of automation tasks. The fact that Python is widely used means there's a large community and plenty of resources for learning and troubleshooting.*

3. **What is the connection between DevOps and automation?**

   *DevOps is all about improving the software development process, and automation is a key way to achieve that. Automation in the context of DevOps could be used for automating infrastructure setup, software testing, deployment, and monitoring, among other things. By automating these processes, teams can develop, test, and release software more quickly and reliably.*

## High-level Overview of the os, re, and shutil Python Modules

1. **`os` Module:**

- The `os` module in Python is like a Swiss Army knife for interacting with the operating system. It allows you to perform a wide variety of tasks, including working with files and directories, retrieving system information, and managing processes.

- In the context of automation, it's like having a toolbox for dealing with the file system. Need to create a new directory (a new drawer in the cabinet)? Use `os.mkdir()`. Want to list all the files in a directory (all the files in a drawer)? Use `os.listdir()`. Want to construct file paths in a way that's compatible with the current operating system (like knowing whether to turn left or right in the maze that is your file system)? Use `os.path.join()`. It also helps in extracting the file extension which can be handy when you're categorizing or filtering files based on their types with `os.path.splitext()`.

- In terms of DevOps, it's extremely handy for setting up environments, managing logs, automating tests, and doing just about anything else that involves interacting with the operating system.

2. **`shutil` Module:**

- The `shutil` (or shell utility) module is like a moving company for your files and directories. It can move, copy, and delete entire folders. Need to archive a project (pack up your house)? Use `shutil.make_archive()`. Need to move a folder to a new location (move your house to a new address)? Use `shutil.move()`.

- In the context of automation, `shutil` can help in creating backups, moving around log files, organizing directories, and more. It's like the moving crew, able to haul around heavy directories without breaking a sweat.

- In DevOps, it can be used for automating backups, setting up environments, moving around logs, and more.

3. **`re` Module:**

- This is one you all may be familiary with that you learned on your own.
  
- `re` stands for Regular Expression, a powerful tool for manipulating text. You can think of the `re` module as a metal detector that's able to find specific patterns in a sea of text. Need to find all the email addresses in a document? Or maybe you need to find specific log entries? The `re` module can do that and much more.

- In automation, this is incredibly useful for text processing tasks, such as parsing logs, processing data, validating inputs, and so on. It's like the Sherlock Holmes of your Python toolbox, able to pick up on the smallest clues and see patterns that are not immediately obvious.

- In the DevOps world, `re` can be used for a wide variety of tasks, like parsing logs, manipulating configuration files, or filtering command output.

**In summary**, `os`, `re`, and `shutil` are like the toolbox, detective, and moving crew of Python's standard library. They're incredibly powerful tools for automation and DevOps, making it easier to interact with the operating system, process text, and manage files and directories.

## 2. Designing and Implementing a CLI App using Python and Rich (15 min)

- CLI (Command Line Interface) apps are powerful tools that allow users to interact with your program through commands typed into a terminal or command prompt. Designing and implementing a CLI app requires careful planning to ensure the app is intuitive and easy to use.

- Python, with its rich set of libraries and simplicity, makes it an ideal language for creating CLI apps. When designing a CLI app in Python, the following factors should be considered:

1. **User Interaction**: How will the user interact with your app? What commands will they need to type? What kind of feedback will they get?

1. **Error Handling**: How will your app handle errors, such as incorrect user input or failed operations?

1. **Functionality**: What tasks will your app perform? How can you design your code to be modular and easy to maintain or expand upon?

- Wireframe anyone?  To add colors, styles, and other text formatting capabilities to our CLI, we are use the Python library `rich`. This is not the only thing out there. 

- Think of `rich` like an artist's paint set for your CLI app. Normally, your CLI app can only print out plain text - like a sketch. But with `rich`, you can add colors, bold or italic styles, and even complex layouts like tables or lists - essentially, you're adding paint to your sketch and turning it into a vibrant painting.

- You will spend some time in the docs today. https://rich.readthedocs.io/en/stable/introduction.html
> NOTE: Rich required Python 3.7 and above
Let's use `rich` to build a simple CLI app.

**Demo Code:**
- Create Virtual Environment
- pip install rich
- run a pip freeze > requirements.txt

```python
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Instantiate a console object
# The "console" refers to a text-based user interface (TUI) for displaying richly formatted and styled text in the terminal.
console = Console()

# Greet the user
# Note the open / closing (almost like HTML)
console.print("Hello, [bold green]User[/bold green]!")

# Ask user's name
# We could do a simple input statement here and it will work.
# But watch what happens when I press Enter. No user input.
name = input('What is your name?')
# Switch to this one after doing the initial display
name = Prompt.ask("What is your name?")

# Display a message to the user
console.print(f"Nice to meet you, [bold blue]{name}[/bold blue]!")

# Create a table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Name", style="dim", width=20)
table.add_column("Age")
table.add_column("Country")

# Add rows to the table
table.add_row("John Doe", "30", "USA")
table.add_row("Jane Doe", "25", "Canada")
table.add_row(name, Prompt.ask("What is your age?"), Prompt.ask("What is your country?"))

# Display the table
console.print(table)
```

In this script, we use `rich` to add colors and styles to our text, and to create a table with multiple columns and rows. The `Prompt.ask` method allows us to take input from the user.

The `rich` library provides a simple and expressive syntax for adding color and style to your text. You can change the color of the text, make it bold, underline it, and much more.

Let's take a look at some examples:

1. **Colors:** To change the color of the text, you can use square brackets to enclose the name of the color and the text you want to colorize:

   ```python
   console.print("[red]Hello, World![/red]")  # Prints "Hello, World!" in red
   ```

   `rich` supports a wide variety of colors, including `red`, `green`, `blue`, `cyan`, `magenta`, `yellow`, and `black`.

2. **Styles:** You can make text bold, italic, underline, or strikethrough:

   ```python
   console.print("[bold]Hello, World![/bold]")         # Prints "Hello, World!" in bold
   console.print("[italic]Hello, World![/italic]")     # Prints "Hello, World!" in italic
   console.print("[underline]Hello, World![/underline]") # Prints "Hello, World!" with an underline
   console.print("[strikethrough]Hello, World![/strikethrough]") # Prints "Hello, World!" with a strikethrough
   ```

   Styles can be combined with colors:

   ```python
   console.print("[bold red]Hello, World![/bold red]")  # Prints "Hello, World!" in bold red
   ```

3. **Nested Styles:** You can nest styles within each other. The innermost style takes precedence:

   ```python
   console.print("[red]Hello, [bold]World![/bold][/red]")  # Prints "Hello, " in red, and "World!" in bold red
   ```

4. **Closing Tags:** Remember to close your tags with `[/]`. This tells `rich` where the style or color should end:

   ```python
   console.print("[red]Hello, World![/red] This is not red.")  # Only "Hello, World!" is red
   ```

This is a brief overview of the color and style syntax of `rich`. There are many more features and nuances you can discover by reading the `rich` documentation.

# Hour 2 - `os`, `shutil`, and `re` modules:
## `os` Module

- Create a os_demo file.
https://docs.python.org/3/library/os.html

Here is a Python script that demonstrates the usage of `os.mkdir()`, `os.listdir()`, `os.path.join()`, and `os.path.splitext()`:

```python
import os
blank = '\n'

# Create a new directory
os.mkdir('test_dir')
print('Directory created.')

# rerun the file again and look for the already exists error.
# How can we fix this:
# This will work because we are in the directory with the folder. If not we would have to specify the path.
if os.path.exists('test_dir'):
    print('Folder already Exists!', blank)
else:
    os.mkdir('test_dir')
    print('Directory created.', blank)

# List files and directories in the current directory
print('List of files/directories:')
print(os.listdir('.'), blank)

# Join path components for the new file in the created directory
file_path = os.path.join('test_dir', 'test_file.txt')
print(f'Constructed file path: {file_path}', blank)

# Create a new file in the created directory
with open(file_path, 'w') as file:
    file.write('Hello, World!')

# List files and directories in the created directory
print('List of files/directories in test_dir:')
print(os.listdir('test_dir'), blank)

# Split the file path into root and extension
root, ext = os.path.splitext(file_path)
print(f'Root of the file path: {root}')
print(f'Extension of the file path: {ext}')
```

Here's what each part of the script does:

1. `os.mkdir('test_dir')` creates a new directory named "test_dir".
2. `os.listdir('.')` lists all the files and directories in the current directory.
3. `os.path.join('test_dir', 'test_file.txt')` constructs a filepath by joining the directory "test_dir" and the file "test_file.txt".
4. The `with open(file_path, 'w') as file:` block creates a new file at the filepath we just constructed and writes "Hello, World!" to it.
5. `os.listdir('test_dir')` lists all the files and directories in "test_dir", which will include the file we just created.
6. `os.path.splitext(file_path)` splits the filepath into the root (the part before the extension) and the extension (the part after the dot).

## `shutil` Module

### Here is a demonstration of `shutil.move()` function

The `shutil.move()` function in Python is used to recursively move a file or directory (source) to another location (destination) and return the destination. If the destination is a directory, then the source is moved inside the directory. If the destination already exists but is not a directory, it may be overwritten depending on the platform.

```python
import os
import shutil
from rich.console import Console

console = Console()

# Create a source directory and a file inside it
# Note the use of mkdirs and not mkdir here.
# Use ChatGPT to show us the difference.
os.makedirs('src_directory', exist_ok=True)
with open('src_directory/src_file.txt', 'w') as f:
    f.write('This is a demo file')

# Create a destination directory
os.makedirs('dst_directory', exist_ok=True)

# Print contents of the directories before the move
console.print("Before move operation")
console.print("Contents of source directory:", os.listdir('src_directory'))
console.print("Contents of destination directory:", os.listdir('dst_directory'))

# Use shutil.move() to move the file
shutil.move('src_directory/src_file.txt', 'dst_directory')

# Print contents of the directories after the move
console.print("After move operation")
console.print("Contents of source directory:", os.listdir('src_directory'))
console.print("Contents of destination directory:", os.listdir('dst_directory'))
```

When you run this script, it creates a file in a source directory, moves that file to a destination directory using `shutil.move()`, and then prints out the contents of both directories before and after the move operation. This demonstrates the basic usage of `shutil.move()` in a file system operation, which is a common task in automation scripts.

### Here's a demonstration of other common `shutil` operations:

```python
import os
import shutil
from rich_demo.console import Console

console = Console()

# Let's create a source directory and a few files inside it
os.makedirs('src_dir', exist_ok=True)
with open('src_dir/file1.txt', 'w') as f:
    f.write('This is file1')
with open('src_dir/file2.txt', 'w') as f:
    f.write('This is file2')

# Create a destination directory
os.makedirs('dst_dir', exist_ok=True)

# Print contents of the directories before copy operation
console.print("Before copy operation")
console.print("Contents of source directory:", os.listdir('src_dir'))
console.print("Contents of destination directory:", os.listdir('dst_dir'))

# Use shutil.copy2() to copy file1.txt to dst_dir, preserving file metadata
shutil.copy2('src_dir/file1.txt', 'dst_dir')

# Print contents of the directories after copy operation
console.print("After copy operation")
console.print("Contents of source directory:", os.listdir('src_dir'))
console.print("Contents of destination directory:", os.listdir('dst_dir'))

# Use shutil.copytree() to copy entire directory
shutil.copytree('src_dir', 'dst_dir_copy', dirs_exist_ok=True)

# Print out the contents of src_dir and dst_dir_copy
console.print("After copytree operation")
console.print("Contents of source directory:", os.listdir('src_dir'))
console.print("Contents of copied directory:", os.listdir('dst_dir_copy'))

# Use shutil.rmtree() to remove a directory and all its contents
shutil.rmtree('dst_dir_copy')

# Check if dst_dir_copy still exists
if not os.path.exists('dst_dir_copy'):
    console.print("The directory 'dst_dir_copy' was successfully removed", style="green")
```

In this script:

- `shutil.copy2()` is used to copy a file from the source directory to the destination directory, preserving the file's metadata such as timestamps.
- `shutil.copytree()` is used to copy an entire directory and its contents to a new location.
- `shutil.rmtree()` is used to remove a directory and all its contents.

Please remember that `shutil` functions can overwrite files and directories without warning, so use them with care. Also, remember that these operations can fail due to a variety of reasons (file doesn't exist, no permissions, etc.), so in a real script you'd want to handle those exceptions appropriately.

## `re` Module

The `re` module in Python is used for working with regular expressions. Regular expressions are a powerful tool for various kinds of string manipulation. They are a domain-specific language (DSL) that is present as a library in most modern programming languages, not just Python.

In the context of DevOps, `re` can be useful for many tasks such as parsing log files, manipulating configuration files, validating user inputs or string patterns, etc.

Here's a simple demo code to illustrate how `re` works:

```python
import re

# Example log line
log_line = '2023-05-21 10:00:00,001 [main] ERROR org.example.MyApp - Something went wrong!'

# Match date and time
match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}', log_line)
if match:
    print(f'Date and Time: {match.group()}')  # 2023-05-21 10:00:00,001

# Extract log level
match = re.search(r'INFO|ERROR|WARN|DEBUG', log_line)
if match:
    print(f'Log Level: {match.group()}')  # ERROR

# Extract error message
match = re.search(r' - (.*)', log_line)
if match:
    print(f'Error Message: {match.group(1)}')  # Something went wrong!
```

In this example, we have a log line and we're using regular expressions to extract the date and time, the log level, and the error message from the log. This can be very useful in DevOps for parsing and extracting information from logs.
