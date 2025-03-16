import os
import zipfile
import shutil

def rename_files(dir_path):
    for filename in os.listdir(dir_path):  # 遍历 test 文件夹
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):  # 确保是文件
            name, ext = os.path.splitext(filename)  # 分离文件名和扩展名
            if ext == "":  # 无扩展名的文件
                new_name = f"{filename}.in"
                os.rename(file_path, os.path.join(dir_path, new_name))
                print(f"Renamed: {filename} -> {new_name}")
            elif ext == ".a":  # 扩展名为 .a 的文件
                new_name = f"{name}.out"
                os.rename(file_path, os.path.join(dir_path, new_name))
                print(f"Renamed: {filename} -> {new_name}")

def process_zip():
    for filename in os.listdir():
        if filename.endswith("$linux.zip"):  # 找到符合条件的 zip 文件
            zip_path = filename
            extract_path = filename.replace("$linux.zip", "")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)  # 解压文件
            
            test_folder = os.path.join(extract_path, "tests")
            if os.path.exists(test_folder):
                rename_files(test_folder)  # 执行改名操作
                new_zip_path = extract_path + ".zip"
                shutil.make_archive(extract_path, 'zip', test_folder)  # 重新打包
                shutil.rmtree(extract_path)  # 删除解压文件夹
                os.remove(zip_path)  # 删除原始 zip 文件
                print(f"Processed: {zip_path} -> {new_zip_path}")

if __name__ == "__main__":
    process_zip()

