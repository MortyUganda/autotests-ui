import allure
from playwright.sync_api import expect
from elements.base_element import BaseElement
from elements.ui_coverage import tracker, ActionType

from tools.logger import get_logger

logger = get_logger('BUTTON')

class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return 'button'
    
    def check_enabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" if enabled'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()
        self.track_coverage(ActionType.ENABLED, nth=0, **kwargs)

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" if enabled'
        
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()
        self.track_coverage(ActionType.DISABLED, nth=0, **kwargs)