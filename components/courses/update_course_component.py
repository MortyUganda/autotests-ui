import re
from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from elements.button import Button
from elements.text import Text


class UpdateCourseComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(
            page, 'create-course-toolbar-create-course-button', 'Update course'
        )

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Update course')

        self.create_course_button.check_visible()

    def click_create_course_button(self):
        self.create_course_button.click()
        self.check_current_url(re.compile(".*/#/courses"))