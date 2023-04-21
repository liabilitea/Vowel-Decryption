# Vowel-Decryption
***
## Description

This Python project decrypts encrypted characters or statements into their equivalent vowel values, which are the following:

+ '*' = a
+ '&' = e
+ '#' = i
+ '+' = o
+ '!' = u

Furthermore, this code utilizes a dictionary to define the substitutes of the characters. 

## How To Use / Run 

1. Install Python on your computer to run the code. You can download its latest version here: https://www.python.org/downloads/
2. Copy the code from the repository. 
3. Open an IDE and paste the code.
    + If you don't have an IDE, you can use any text editor from your computer and paste the code. 
4. Save the file with a .py extension.
5. Run the code.
    + For text-editor users, open a command prompt or terminal window and locate the folder where the Python file was saved and enter the command provided below by typing it in the command-line interface. After typing the command, press the Enter key to execute.
    
  ```
  python 'file_name'.py
  ```
6. It will ask you to enter an encrypted message. Press Enter after inputting your message.
7. The decrypted text will be displayed. 

## Example Output

  ```
  Enter an encrypted text to decrypt: h&ll+ w+rld
  Decrypted Text: hello world
  ```
  
  ## Customization
  
  You can define your substitutes by using the dictionary function, *'char_substitute'*. Below is an example of different key-value pairs defined in the same dictionary.
  
  ```
  char_substitute = {'@': 'a', '%': 'e', '(': 'i', ')': 'o', '>': 'u'}
  ```
  
  
  
