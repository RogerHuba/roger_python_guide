from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import sys
import os
import re
import shutil

def main():
    """Main function to run the CLI app."""
    console = Console()
    first = 'First'
    last = 'Last'
    while True:
        os.system('clear')
        console.print(f"\n1. First Name: {first}\n2. Last Name: {last}\n3. Full Name: {first} {last}\n4. Exit")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4'], default='4')

        if choice == '1':
            first = Prompt.ask("Please Enter your First Name:", default='First')

        elif choice == '2':
            last = Prompt.ask("Please Enter your Last Name:", default='Last')
        elif choice == '3':
            console.print(f'Your full name is {first} {last}')
        elif choice == 'q' or 'Q':
            do_exit('Thank you for using the menu')
        else:
            print('Try Again')


def do_exit(message):
    sys.exit(message)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        do_exit('Ctrl-C Detected')