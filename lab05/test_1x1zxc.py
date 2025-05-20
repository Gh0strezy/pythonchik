import os
import tempfile
import shutil
import pytest
from zxc1x1 import get_file_name

@pytest.fixture
def test_dir():
    temp_dir = tempfile.mkdtemp()
    bath_dir = os.path.join(temp_dir, "BATH")
    os.makedirs(bath_dir)
    
    test_files = [
        "a.txt", "a_sort.txt", "cdfile", "cdfile.bat", "cf.txt",
        "cf1.bat", "ex.txt", "list_n.txt", "part1.bat",
        "part2.bat", "return.bat"
    ]
    
    for file in test_files:
        with open(os.path.join(bath_dir, file), 'w') as f:
            f.write("test")
    
    new_dir = os.path.join(bath_dir, "Новая папка")
    os.makedirs(new_dir)
    with open(os.path.join(new_dir, "new_123123131.txt"), 'w') as f:
        f.write("test")
    
    yield bath_dir
    
    shutil.rmtree(temp_dir)

def test_with_real_files(test_dir):
    result = list(get_file_name(directory=test_dir))
    
    # Преобразуем ожидаемые пути к временной директории
    expected_list1 = [
        os.path.join(test_dir, f) for f in [
            'a.txt', 'a_sort.txt', 'cdfile', 'cdfile.bat', 'cf.txt',
            'cf1.bat', 'ex.txt', 'list_n.txt', 'part1.bat',
            'part2.bat', 'return.bat'
        ]
    ] + [os.path.join(test_dir, "Новая папка", "new_123123131.txt")]
    
    expected_list2 = [
        os.path.join(test_dir, f) for f in [
            'cdfile.bat', 'cf1.bat', 'part1.bat', 'part2.bat', 'return.bat'
        ]
    ]
    
    expected_list3 = [
        os.path.join(test_dir, f"new_{os.path.basename(p)}") 
        for p in expected_list2
    ]
    
    assert sorted(result[0]) == sorted(expected_list1)
    assert sorted(result[1]) == sorted(expected_list2)
    assert sorted(result[2]) == sorted(expected_list3)