from main import SmartDiet

def test_is_empty():
    diet = SmartDiet()

    assert 0 == diet.calculate()

def test_is_one():
    diet = SmartDiet()


    diet.register_food("Хлеб",300)
    diet.add_food("Хлеб",2)

    actual = diet.calculate
    expected = 600

    assert 600 == diet.calculate()

def test_if_many():
    diet = SmartDiet()
    diet.register_food("Хлеб",300)
    diet.register_food("Мясо", 500)
    diet.register_food("Яблоко",100)

    diet.add_food("Мясо",2)
    diet.add_food("Яблоко", 1)

    assert 1500 == diet.calculate()