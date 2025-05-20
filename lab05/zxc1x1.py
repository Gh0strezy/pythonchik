import os
import shutil
import typing

def get_file_name(directory: str) -> typing.Generator[str]:
    # list1 = []
    # list3 = []

    for root, _, files in os.walk(directory):
        for file in files:
            # list1.append(os.path.join(root, file))
            yield os.path.join(root, file)

    # yield list1
    # filter_by_extension = filter(lambda file: file.endswith(extension), list1)

    # list2 = os.path.join(root, file) for file in filter_by_extension
    # for file in filter_by_extension:
    #     yield os.path.join(root, file)

    # for file in list2:
    #     dir_path, file_name = os.path.split(file)
    #     new_file = "new_" + file_name
    #     new_file_path = os.path.join(dir_path, new_file)
    #     shutil.copy(file, new_file_path)
    #     list3.append(new_file_path)

    # for file in list1:
    #     dir_path, file_name = os.path.split(file)
    #     new_name = "new_" + file_name
    #     new_file_path = os.path.join(dir_path, new_name)
    #     os.rename(file, new_file_path)
    #     yield new_file_path
    # yield list2
    # yield list3
def rename_file(file_path: str) -> str:
        dir_path, file_name = os.path.split(file_path)
        new_name = "new_" + file_name
        new_file_path = os.path.join(dir_path, new_name)
        os.rename(file_path, new_file_path)
        return new_file_path

directory = "C:\\BATH"
extention = ".bat"

print("ALL FILES:")

print(*get_file_name(directory= directory), sep= '\n')

print('FILTERED FILES:')
for i in filter(lambda file: file.endswith(extention), get_file_name(directory=directory)):
    print(i)

all_files = list(get_file_name(directory=directory))

renamed_files = list(map(rename_file, all_files))
print("RENAMED FILES:")
for i in renamed_files:
    print(i)