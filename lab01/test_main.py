import main
print(dir(main))
print(dir(main.a01_circle))
def test_addition():
    assert main.a00_distance.main() == main.a00_distance.distances
# def test_addition2():
    # assert main.a01_circle.main1() == (f'{main.a01_circle.square}\n{main.a01_circle.point_1[0]**2 + main.a01_circle.point_1[1]**2 <= main.a01_circle.radius**2}\n{main.a01_circle.point_2[0]**2 + main.a01_circle.point_2[1]**2 <= main.a01_circle.radius**2}')