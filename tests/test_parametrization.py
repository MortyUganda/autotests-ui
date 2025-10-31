import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])  # Параметризируем тест
# Название "number" в декораторе "parametrize" и в аргументах автотеста должны совпадать
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
# В данном случае в качестве данных используется список с кортежами
def test_several_numbers(number: int, expected: int):
    # Возводим число number в квадрат и проверяем, что оно равно ожидаемому
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Параметризируем по операционной системе
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])  # Параметризируем по браузеру
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0  # Проверка указана для примера



import pytest

@pytest.fixture(params=["chrome", "firefox", "safari"])
def browser(request: SubRequest):
    return request.param

def test_browser(browser: str):
    assert browser in ["chrome", "firefox", "safari"]

@pytest.mark.parametrize('user', ['Alise', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self ,user: str, account: str):
        print(f'User with operations {user}')

    def test_user_without_operations(self , user: str):
        print(f'User without operations {user}')


users = {
    '+700000011': 'User with money',
    '+700000022': 'User with operations',
    '+700000033': 'user without money',
}

@pytest.mark.parametrize(
    'phone_number', 
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...

# @pytest.mark.parametrize(
#     'phone_numbers', 
#     ['+700000011', '+700000022', '+700000033', ],
#     ids=[
#         'User with money',
#         'User with operations',
#         'user without money',
# ])
# def test_identifiers(phone_numbers: str):
#     ...

