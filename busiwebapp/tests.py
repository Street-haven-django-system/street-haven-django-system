# tests.py
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class HomepageTest(LiveServerTestCase):
    """
    Test class for verifying elements on the Django homepage.
    Uses Selenium WebDriver to simulate browser interaction.
    """

    def setUp(self):
        """
        Runs BEFORE each test.
        Initializes Chrome WebDriver and opens the browser.
        """
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)

    def test_logo_text_is_visible(self):
        """
        Test 1: Verify the logo text 'STREET.HAVEN' is visible on the page.
        Uses Selenium to check the .logo-text element.
        """
        # Navigate to homepage
        self.driver.get(self.live_server_url)

        # Locate the logo text element using its class
        logo = self.driver.find_element(By.CLASS_NAME, "logo-text")

        # Assert the logo text contains the site name
        self.assertIn("STREET", logo.text)
        print("✅ Test 1 passed: Logo text is visible!")

    def test_homepage_status_code(self):
        """
        Test 2: Verify the homepage returns HTTP 200 OK.
        Uses self.client to check the response status code.
        """
        # Use Django test client to send GET request
        response = self.client.get('/')

        # Assert page loads successfully
        self.assertEqual(response.status_code, 200)
        print("✅ Test 2 passed: Homepage returns 200 OK!")

    def tearDown(self):
        """
        Runs AFTER each test.
        Closes the browser to free up resources.
        """
        self.driver.quit()