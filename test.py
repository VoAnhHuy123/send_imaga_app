import zipfile
path = 'D:\\vscode\\python\\send_file_app\\'
def unzip_file(path): 
    extract_zip = zipfile.ZipFile(path, "r")
    extract_zip.extractall(path)
unzip_file(path + "images.zip")