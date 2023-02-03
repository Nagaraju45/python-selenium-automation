import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from testFramework.base.base_driver import BaseDriver
from testFramework.pages import search_flights_results_page
from testFramework.utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
    #locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULTS_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    # SELECT_DATE_FIELD = "//li[@class='datepicker flex1']"
    ALL_DATES = "//div[@id='monthWrapper']//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"
    # SEARCH_BUTTON = '//*[@id="BE_flight_flsearch_btn"]'

    def getDepartFromField(self):
       return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)
    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)
    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULTS_LIST)
    def getSelectDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)
    def getAllDates(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ALL_DATES)
    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        self.log.info("Clicked on going to")
        self.getGoingToField().send_keys(goingtolocation)
        self.log.info("Typed text into going to feild successfully")
        search_ele = self.getGoingToResults()
        # self.log.info(len(search_ele))
        for result in search_ele:
            if goingtolocation in result.text:
                result.click()
                # time.sleep(2)
                break
    def enterDepartureDate(self, departureDate):
        self.getSelectDateField().click()
        select_date = self.getAllDates()[0].find_elements(By.XPATH, self.ALL_DATES)
        # select_date = all_dates[0].find_elements(By.XPATH, self.ALL_DATES)
        # select_date = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@id='monthWrapper']//td[@class!='inActiveTD']").find_elements(By.XPATH, "//div[@id='monthWrapper']//td[@class!='inActiveTD']")
        time.sleep(2)
        for date in select_date:
            if date.get_attribute("data-date") == departureDate:
                date.click()
                self.log.info("date feild completed")
                time.sleep(2)
                break

    def clickSearchFlightsButton(self):
        self.getSearchButton().click()
        self.log.info("search button completed")
        time.sleep(4)

    def searchFlights(self, departlocation, goingtolocaton, departureDate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocaton)
        self.enterDepartureDate(departureDate)
        self.clickSearchFlightsButton()
        # self.driver.find_element('xpath', "//input[@value='Search Flights']").click()
        search_flights_result = search_flights_results_page.SearchFlightsResult(self.driver)
        return search_flights_result

    # def departfrom(self, departlocation):
    #     # depart_from = self.wait.until(EC.element_to_be_clickable(('xpath', "//input[@id='BE_flight_origin_city']")))
    #     depart_from = self.wait_until_element_is_clickable('xpath', "//input[@id='BE_flight_origin_city']")
    #     depart_from.click()
    #     depart_from.send_keys(departlocation)
    #     depart_from.send_keys(Keys.ENTER)
    #     time.sleep(2)

    # def goingto(self, goingtolocation):
    #     # going_to = self.wait.until(EC.element_to_be_clickable(('xpath', "//input[@id='BE_flight_arrival_city']")))
    #     going_to = self.wait_until_element_is_clickable('xpath', "//input[@id='BE_flight_arrival_city']")
    #     time.sleep(2)
    #     going_to.send_keys(goingtolocation)
    #     time.sleep(3)
    #     # search_ele = self.wait.until(EC.presence_of_all_elements_located(('xpath', "//div[@class='viewport']//div[1]/li")))
    #     search_ele = self.wait_for_presence_of_all_elements('xpath', "//div[@class='viewport']//div[1]/li")
    #     time.sleep(4)
    #     print("\nCities:", len(search_ele))
    #     for result in search_ele:
    #         if "New York (JFK)" in result.text:
    #             result.click()
    #             time.sleep(2)
    #             break

    # def selectdate(self, departuredate):
    #     self.wait_until_element_is_clickable('xpath', "//input[@id='BE_flight_origin_date']").click()
    #
    #     select_dates = self.wait_for_presence_of_all_elements('xpath', "//div[@id='monthWrapper']//td[@class!='inActiveTD']")\
    #         .find_elements('xpath', "//div[@id='monthWrapper']//td[@class!='inActiveTD']")
    #     for date in select_dates:
    #         if date.get_attribute("data-date") == departuredate:
    #             date.click()
    #             time.sleep(2)
    #             break
    #
    # def clicksearch(self):
    #     self.driver.find_element('xpath', "//input[@value='Search Flights']").click()
    #     time.sleep(4)
