__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'
# Imported Modules:
import os
import shutil
import zipfile

cache_directory = 'cache'
cache_path = os.getcwd() + '\\cache'
zip_path = os.getcwd() + '\\data.zip'

# 1.
def clean_cache():
    if os.path.isdir(cache_directory):
        shutil.rmtree(cache_directory)
        os.mkdir(cache_directory)
        print('Cache cleared')
    else:
        os.mkdir(cache_directory)
        print('Cache directory created')

# 2.
def cache_zip(zip_path, cache_path):
    clean_cache()
    with zipfile.ZipFile(zip_path, 'r') as data:
        data.extractall(cache_path)
    print('data.zip unpacked')
print(cache_zip(zip_path, cache_path))

# 3.
def cached_files():
    cache_absolute_path_list = [os.path.join(cache_path, file) for file in os.listdir(cache_path)]
    return cache_absolute_path_list
print(cached_files())

# 4.
def find_password(cached_files_list):
    for file in cached_files_list:
        search_file = open(file, 'r')
        lines = search_file.readlines()
        for line in lines:
            if 'password' in line:
                password = line.partition('password: ')[2][:-1]
                return password 
print(find_password(cached_files()))