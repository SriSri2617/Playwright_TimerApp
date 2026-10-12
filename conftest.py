import pytest

Base_URL = "https://lejonmanen.github.io/timer-vue/"

# Every test strat from the homepage
@pytest.fixture(autouse=True)
def app(page):
    page.goto(Base_URL)  
    return page
