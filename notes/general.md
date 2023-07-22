# Notes:

### JSON - JavaScript Object Notation format for exchanging data between computers
- currently used by all langages (hence is language agnostic)

use sys.exit() to TERMINATE PROGRAM!!

cannot/ Do not know how to import files/libraries with _underscore in the filename eg : file_001

when runnig a file directly it will automatically/under the hood, assing '__main__' to the special hidden vairable '__name__'
'__name__' is a special variable in python  => Value is automatically set by python under the hood to be '__main__' when you run the file from the command line by calling 'python filename.py' !
Therefore having this IF statement in a file makes it so that anything there is only called when calling the file directly in the commandline
if __name__== "__main__":
Usefull for making functions importable but file itself runnable

# Importing weird filenames with leading 0's or uderscores:
- Use importlib:
import importlib
- define the import:
impoerted_module = importlib.import_module("0tricky_filename")
