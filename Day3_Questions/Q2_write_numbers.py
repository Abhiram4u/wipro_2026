def write_numbers_to_file(filename):
    try:
        with open(filename,'w') as file:
            for i in range(1,101):
                file.write(str(i)+'\n')
            print("numbers written to file")
    except FileNotFoundError:
        print("Error: file not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print("unexpected error",e)