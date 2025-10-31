from playwright.sync_api import expect


def test_empty_courses_list(chromium_page_with_state):
    courses_toolbar_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_toolbar_text).to_be_visible()
    expect(courses_toolbar_text).to_have_text('Courses')

    course_icon_visible = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(course_icon_visible).to_be_visible()
    expect(course_icon_visible).to_be_attached()

    course_no_res_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(course_no_res_text).to_be_visible()
    expect(course_no_res_text).to_have_text('There is no results')

    course_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(course_description_text).to_be_visible()
    expect(course_description_text).to_have_text('Results from the load test pipeline will be displayed here')

       