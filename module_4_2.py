def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function() # это будет работать
inner_function() # это не будет работать, не в области видимости