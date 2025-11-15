import allure 


def test_feature_practic():
    with allure.step('Opening brawser'):
        ...

    with allure.step('Creating course'):
        ...

    with allure.step('Closing browser'):
        ...



@allure.step('Closing browser')
def close_browser():
    ...


@allure.step('Check data browser with title {title}')
def create_course(title: str):
    ...
    

@allure.step('Open browser')
def open_browser():
    ...


def test_feature():
    open_browser()

    create_course(title='Locust')
    create_course(title='Check')
    create_course(title='Data #1')

    close_browser()
