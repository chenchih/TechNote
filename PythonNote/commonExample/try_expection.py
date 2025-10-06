def readFile(filename):

    try:
        with open(filename, "r") as file:
            content= file.read()
    except FileNotFoundError:
        print('File not found!!! Help you create one....')
        with open("missingfile.txt", "w") as file:
            content= "Hello World"
            file.write(content)
    else:
        print("File Read successfully")
        return content
    finally:
        print("Closing FIle")
if __name__ == '__main__':
    filename= input('Your filename(ex test.txt): ')
    content= readFile(filename)
    print(content)
    
