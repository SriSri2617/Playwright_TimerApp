import re
from playwright.sync_api import expect

# User Story 2: Create and Delete Note Widgets
# As a user, I want to create and delete note widgets so that I can manage notes and reminders.

def test_note_widget_verification(app):
    # Add note button
    add_note_btn = app.get_by_role("button", name=re.compile("Add note"))
    add_note_btn.click()
    app.wait_for_timeout(1000)

    # 2.1 note widget
    note_widget = app.locator(".note")

    # Icons
    icon_panel = app.locator(".align-top-right")
    btn_up = icon_panel.locator(".icon.up")
    btn_close = icon_panel.locator(".icon.close")

    # Assert note widget frame
    expect(note_widget).to_be_visible()
    expect(note_widget).to_have_count(1)
    expect(app.get_by_text(re.compile("Click to change text"))).to_be_visible()

    # Assert icons
    expect(btn_up).to_be_enabled()
    expect(btn_close).to_be_enabled()

    # 2.2 delete note widget
    btn_close.click()
    app.wait_for_timeout(1000)

    # verify deletion
    expect(note_widget).not_to_be_visible()
    expect(note_widget).to_have_count(0)
    
    # ----------------------------------------------------------------- #

    # User Story 5: Change Note Text
    # As a user, I want to edit note text so that I can keep my notes updated.    

    # 5.1 Add text to a note
    add_note_btn.click()
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
    
    # 5.2: Edit note text
    note_widget.click()

    # Find note widget input
    note_input = app.locator('input[placeholder ="Description"]')

    # Enter text
    note_input.fill("Timer starts now")
    note_input.press("Tab")
    app.wait_for_timeout(1000)
    note_widget = app.locator(".widget").filter(
        has=app.get_by_text("Timer starts now"))

    # Assert
    expect(note_widget).to_be_visible()

    # 5.3 Negative Scenario: Save an empty note
    note_widget.click()

    # Find note widget input
    note_input = app.locator('input[placeholder ="Description"]')

    # Enter text
    note_input.fill("")
    note_input.press("Tab")
    app.wait_for_timeout(1000)

    # note widget panel
    note_widget_panel = app.locator(".note").locator(".row")

    # Assert
    assert note_widget_panel.text_content().strip() == ""
    assert note_input.input_value() == ""

# =========================================================================================================