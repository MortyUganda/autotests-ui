from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login', wait_until='networkidle')


    # -----------Через f строку----------

    # new_text = '1234'
    # page.evaluate(
    #     f"""
    #     const title = document.getElementById('authentication-ui-course-title-text')
    #     title.textContent = {new_text}
    #     """
    #     )
    # page.wait_for_timeout(2000)


    # -----------Через безымянную функцию JavaScript-------------

    new_text = '1234'
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text
        }
        """, 
        new_text
    )
    
    page.wait_for_timeout(2000)