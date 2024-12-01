def read():
    
    while True:
        try:
            file_name = input('Enter the file name you want to open: ')
            
            if not file_name:
                raise ValueError("The file name cann't be empty.")
            
            with open(file_name, 'r') as file:
                content = file.read()
                print('File content:')
                print(content)
                
            return file_name, content
        
        except FileNotFoundError:
            print("File not found. Try again.")
        except ValueError as e:
            print(f"Error: {e}. Enter a valid name.")
        except Exception as e:
            print(f"Unexcepted error occured: {e}. Try again.")
            
def write():
    try:
        new_file_name = input('Enter name for new file to write to: ')

        if not new_file_name:
            raise ValueError("The file name cann't be empty.")
        
        content = input("Enter content to write to file: ")
        with open(new_file_name, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to file {new_file_name}.")
        
    except ValueError as e:
        print(f"Error: {e}. File creation failed.")
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        print("Writting to file is complated.")
            
file_name, content = read()

choose = input("Do you want to write to a file? (y/n): ").lower()

if choose == 'y':
    take_new_file = input(f"Do you want to write to the same({file_name}) file? (y/n): ").lower()
    if take_new_file == 'y':
        try:
            new_content = input('Enter new content to write to a file: ')
            with open(file_name, 'w') as file:
                file.write(new_content)
            print(f"Content successfully written to file {file_name}")
        except Exception as e:
            print(f"An error occurred while writing to the file")
        finally:
            print(f"File {file_name} has been closed.")
    else:
        write()