from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input', 'TitleInput')
        self.estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'TimeInput')
        self.description_textarea = Textarea(page, 'create-course-form-description-input', 'TextArea')
        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'MaxScoreInput')
        self.min_score_input = Input(page, 'create-course-form-min-score-input', 'MinScoreInput')

    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.title_input.check_visible
        self.title_input.check_have_value(title)

        self.estimated_time_input.check_visible
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.check_visible
        self.description_textarea.check_have_value(description)

        self.max_score_input.check_visible
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.check_visible
        self.min_score_input.check_have_value(min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.title_input.fill(title)
        self.title_input.check_have_value(title)

        self.estimated_time_input.fill(estimated_time)
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.fill(description)
        self.description_textarea.check_have_value(description)

        self.max_score_input.fill(max_score)
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.fill(min_score)
        self.min_score_input.check_have_value(min_score)

