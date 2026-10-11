import re
from playwright.sync_api import expect

def test_theme_color(app):
    theme_panel = app.locator('[class="component"]')
    expect(theme_panel).to_be_visible()
    buttons = theme_panel.locator("button")
    light_btn = app.get_by_role("button", name = re.compile("Light"))
    dark_btn = app.get_by_role("button", name = re.compile("Dark"))
    forest_btn = app.get_by_role("button", name = re.compile("Forest"))
    orange_btn = app.get_by_role("button", name = re.compile("Orange"))
    christmas_btn = app.get_by_role("button", name = re.compile("Christmas"))
    
    # heading
    expect(app.get_by_text(re.compile(" Select theme "))).to_be_visible()

    # Verify the total number of theme buttons
    expect(buttons).to_have_count(5)
    
    # 6.1: Change application theme
    christmas_btn.click()
    
    # Assert
    expect(christmas_btn).to_have_class(re.compile("selected"))
    
    # 6.2: Verify theme is applied consistently
    orange_btn.click()
    
    # Assert
    expect(orange_btn).to_have_class(re.compile("selected"))
    
    # Add time panel 
    add_timer_btn = app.get_by_role("button", name=re.compile("Add timer"))
    add_timer_btn.click()
    
    app.wait_for_timeout(800)
    
    # Assert
    expect(app.locator("html")).to_have_attribute("data-theme", "orange")
    
    
    
    