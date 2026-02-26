import zipfile

def zip_file():
    file_name = input("Enter file name to zip: ")
    zip_name = "compressed.zip"

    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(file_name)

    print("File zipped successfully!")

def unzip_file():
    zip_name = input("Enter zip file name: ")

    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall()

    print("File unzipped successfully!")

while True:
    print("\n1. Zip File")
    print("2. Unzip File")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        zip_file()
    elif choice == '2':
        unzip_file()
    elif choice == '3':
        break
    else:
        print("Invalid choice!")
