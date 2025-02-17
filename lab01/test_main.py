import main
print(dir(main))
print(dir(main.a01_circle))
def test_addition():
    assert main.a00_distance.main() == main.a00_distance.distances
def test_addition2():
    assert main.a01_circle.main1() == main.a01_circle.result
def test_addition3():
    assert main.a02_operations.main2() == 25
def test_addition4():
    assert main.a03_favorite_movies.main3() == main.a03_favorite_movies.result3
def test_addition5():
    assert main.a04_my_family.main4() == main.a04_my_family.res4
def test_addition6():
    assert main.a05_zoo.main5() == main.a05_zoo.res5
def test_addition7():
    assert main.a06_songs_list.main6() == main.a06_songs_list.res6
def test_addition8():
    assert main.a07_secret.main7() == main.a07_secret.res7
def test_addition9():
    assert main.a08_garden.main8() == main.a08_garden.res8
def test_addition10():
    assert main.a09_shopping.main9() == main.a09_shopping.res9
def test_addition11():
    assert main.a10_store.main10() == main.a10_store.res10