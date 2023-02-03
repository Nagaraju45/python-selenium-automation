import logging
from selenium.webdriver.common.by import By
from testFramework.base.base_driver import BaseDriver
from testFramework.utilities.utils import Utils


class SearchFlightsResult(BaseDriver):
    log = Utils.custom_logger(logLevel = logging.WARNING)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
    # Locators
    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    # FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_2_STOP_ICON = "//div[@class='filter-heading pr sticky full-width']//label[3]"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stops')]"

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)
    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)
    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)
    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)

    log.info("enter flight search page")
    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.warning("Selected flights with 1 stop")
            # time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            self.log.warning("Selected flight with 2 stops")
            # time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            self.log.warning("Selected flights with Non-Stop")
            # time.sleep(2)
        else:
            self.log.warning("Please provide valid filter option")

    # def filter_flights(self):
    #     # time.sleep(2)
    #     self.driver.find_elements(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
    #     time.sleep(4)
    #     # pyautogui.click(x = 150, y = 150)
    #     # time.sleep(5)

# You don't have permission to access "http://flight.yatra.com/air-search-ui/int2/trigger?" on this server.
# Reference #18.e01c045.1671014193.35e57e97
