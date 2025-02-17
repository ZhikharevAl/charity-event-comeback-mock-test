import allure

from src.charity_event.__init__ import main


@allure.step("Test main function")
def test_main() -> None:
    """Test main function."""
    assert main() == "Hello from charity-event!"
