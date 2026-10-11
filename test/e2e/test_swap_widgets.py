import re
from playwright.sync_api import expect


# User Story 3: Swap Two Widgets
# As a user, I want to rearrange widgets so that I can organise my dashboard as I prefer.

def test_swap_timer_note_widget(app):

    # 3.1 swap timer & note widget

    # Add timer button
    add_timer_btn = app.get_by_role("button", name=re.compile("Add timer"))
    add_timer_btn.click()
    app.wait_for_timeout(1000)

    # Add note button
    add_note_btn = app.get_by_role("button", name=re.compile("Add note"))
    add_note_btn.click()
    app.wait_for_timeout(1000)

    # widgets order
    widgets = app.locator(".widget")

    timer_index = None
    note_index = None

    for i in range(widgets.count()):
        text = widgets.nth(i).text_content()

        if "Break" in text:
            timer_index = i

        if "Click to change text" in text:
            note_index = i

    assert timer_index < note_index

    # note widget icon panel
    note_text = app.get_by_text(re.compile("Click to change text"))
    note_text.click()

    # Find note widget input
    note_input = app.locator('input[placeholder ="Description"]')

    # Enter text
    note_input.fill("Swap order test")
    note_input.press("Tab")

    # note widget arrow 
    note_widget = app.locator(".widget").filter(
        has=app.get_by_text("Swap order test"))
    note_up_arrow = note_widget.locator(".icon.up")

    # Swap note widget
    expect(note_up_arrow).to_be_visible()
    note_up_arrow.click()
    app.wait_for_timeout(1000)
    expect(app.get_by_role("heading", name="Swap order test")).to_be_visible()

    # Assert widgets swaped and note widget displayed 1st
    assert note_index > timer_index
    