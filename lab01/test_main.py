import main
print(dir(main))
print(dir(main.a01_circle))
def test_addition():
    assert main.a00_distance.main() == {'Moscow': {'Paris': 130.38404810405297, 'London': 145.60219778561037}, 'London': {'Paris': 42.42640687119285, 'Moscow': 145.60219778561037}, 'Paris': {'London': 42.42640687119285, 'Moscow': 130.38404810405297}}
def test_addition2():
    assert main.a01_circle.main1() ==  '5541.7693\nTrue\nFalse'
def test_addition3():
    assert main.a02_operations.main2() == 25
def test_addition4():
    assert main.a03_favorite_movies.main3() == "Терминатор\nНазад в будущее\nПятый элемент\nЧужие"
def test_addition5():
    assert main.a04_my_family.main4() == "Общий рост моей семьи - 642 см"
def test_addition6():
    assert main.a05_zoo.main5() == ("лев сидит в клетке под номером 1, а жаваронок находится в клетке под номером 7")
def test_addition7():
    assert main.a06_songs_list.main6() == "А другие три песни звучат 13 минут"
def test_addition8():
    assert main.a07_secret.main7() == "в бане веник дороже денег"
def test_addition9():
    assert main.a08_garden.main8() == {'клевер', 'мак'}
def test_addition10():
    assert main.a09_shopping.main9() == {'Twix': [{'shop': 'к&б', 'price': 64.99}, {'shop': 'монетка', 'price': 69.99}], 'Milkyway': [{'shop': 'к&б', 'price': 49.99}, {'shop': 'монетка', 'price': 54.99}]}
def test_addition11():
    assert main.a10_store.main10() == "Стол - 54 шт, стоимость 27860 руб\nДиван - 3 шт, стоимость 3550 руб\nСтулья - 105 шт, стоимость 10311 руб"