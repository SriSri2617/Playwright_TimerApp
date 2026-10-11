import re
from playwright.sync_api import expect

def test_timer_app_page_verification(app):
    
    # page verification
    app.wait_for_timeout(1000)
    expect(app.get_by_role("button", name="Add Timer")).to_be_visible()
    btns = app.locator("button")
    btns_expected = ['Add timer',
                        'Add note',
                        ' Light ',
                        ' Dark ',
                        ' Forest ',
                        ' Orange ',
                        ' Christmas ']
    btns_actual = btns.all_text_contents()
    assert btns_actual == btns_expected

#=========================================================================================================    

# User Story 1 : Create and Delete Timer Widgets
# As a user, I want to create and delete timer widgets so that I can manage the timers I need on my dashboard.

def test_timer_widget_verification(app):
    
    # Add timer button
    add_timer_btn = app.get_by_role("button", name = re.compile("Add timer"))
    add_timer_btn.click()
    app.wait_for_timeout(1000)
    
    # 1.1 new timer frame
    timer_frame = app.get_by_text(re.compile("Break"))    
     
    # Timer buttons
    start_btn = app.get_by_role("button", name = re.compile("Start"))
   
    # Reset button
    reset_btn = app.get_by_role("button", name = re.compile("Reset"))   
    
    # Icons
    icon_panel = app.locator(".align-top-right")   
    btn_setting = icon_panel.locator(".icon.settings")   
    btn_up = icon_panel.locator(".icon.up")    
    btn_close = icon_panel.locator(".icon.close")    
    
    # Assert timer widget
    expect(timer_frame).to_be_visible()
    timer = app.get_by_text(re.compile("15:00"))
    expect(timer).to_be_visible()
    assert timer.text_content() == "15:00"
    
    # Assert action buttons
    expect(start_btn).to_be_enabled()
    expect(reset_btn).to_be_enabled()
    
    # Assert icon panel
    expect(icon_panel).to_be_visible()
    expect(icon_panel.locator(".icon")).to_have_count(3)
    
    # Assert individual icons
    expect(btn_setting).to_be_enabled()
    expect(btn_up).to_be_visible()
    expect(btn_close).to_be_visible()

    # 1.2 Delete a timer
    btn_close.click()
    app.wait_for_timeout(1000)
    
    # verify deletion
    expect(timer_frame).not_to_be_visible()
    
# ---------------------------------------------------------------------------------- #    
       
# User Story 4: Start, Pause, and Reset a Timer
# As a user, I want to start, pause, and reset a timer so that I can control the countdown.    

    # 4.1 start the timer
    add_timer_btn.click()
    start_btn.click()
    
    # varify pause button
    pause_btn = app.get_by_role("button", name = re.compile("Pause"))
    expect(pause_btn).to_be_visible()
    
     # assert timer
    timer = app.locator('[class="row time"]')
    expect(timer).to_be_visible()
    
    before_timer = timer.text_content()
    app.wait_for_timeout(1000)

    # 4.2 Pause timer verification
    pause_btn.click()
    
    pause_time_1 = timer.text_content()
    app.wait_for_timeout(1000)
    pause_time_2 = timer.text_content()
    
    # 4.2 - assert pause time
    assert pause_time_1 == pause_time_2    
    
    # 4.1 assert before & after time 
    after_timer = timer.text_content()
    assert before_timer != after_timer
    
    # 4.3 Reset Time
    
    reset_btn.click()
    expect(timer_frame).to_be_visible()
    timer = app.get_by_text(re.compile("15:00"))
    expect(timer).to_be_visible()
    assert timer.text_content() == "15:00"
