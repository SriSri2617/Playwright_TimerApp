import pytest

Base_URL = "https://lejonmanen.github.io/timer-vue/"

# Every test strat from the homepage
@pytest.fixture(autouse=True)
def before_all(page):
    page.goto(Base_URL)  
    return page
