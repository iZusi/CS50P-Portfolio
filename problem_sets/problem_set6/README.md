### Problem Set 6 - Week 6 (File I/O)

- [lines.py](./lines.py):  This program expects one command-line argument, the name or path of a Python file, and calculates and outputs the count of non-comment and non-blank lines in that file. If any of the specified conditions are not met, such as incorrect arguments or the absence of a ".py" file, the program exits using 'sys.exit.'
  
- [pizza.py](./pizza.py):  This program expects one command-line argument, a Pinocchio-format CSV file's name or path. It generates and displays an ASCII art table using the 'tabulate' library's grid format. If the user fails to provide a single command-line argument, specifies a file without a ".csv" extension, or if the file doesn't exist, the program exits using 'sys.exit.'
  
- [scourgify.py](./scourgify.py):  This program expects two command-line arguments: an existing CSV input file with 'name' and 'house' columns and a new CSV output file with 'first,' 'last,' and 'house' columns. It converts the input to the specified output by splitting each name into first and last names. However, if the user doesn't provide exactly two command-line arguments or the input file can't be read, the program exits with an error message using 'sys.exit.'
  
- [shirt.py](./shirt.py):  This program expects two specific command-line arguments: the input image (JPEG or PNG) in 'sys.argv[1]' and the output image (JPEG or PNG) in 'sys.argv[2].' It overlays 'shirt.png' onto the input image after resizing and cropping it to match the same size. The result is saved as the output. The program exits using 'sys.exit' if any of the following conditions are not met: the user does not provide precisely two command-line arguments, the input and output file names don't end with '.jpg,' '.jpeg,' or '.png' (case-insensitive), the input and output file extensions don't match, or the specified input file does not exist.
  
