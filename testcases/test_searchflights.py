import pytest
import softest
from testFramework.pages.yatra_launch_page import LaunchPage
from testFramework.utilities.utils import Utils
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    # @data(("New Delhi", "JFK", "10/01/2023", "Non Stop"), ("HYD", "Dubai", "10/01/2023", "1 Stop"))
    # @unpack
    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testyml.yaml")
    # @data(*Utils.read_data_from_excel("D:\\Book1excel.xlsx", "Sheet1"))
    @data(*Utils.read_data_from_csv("C:\\SeleniumProjects\\testFramework\\testdata\\tdatacsv.csv"))
    @unpack
    def test_search_flights_2_stop(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stop(stops)
        allstops2 = search_flight_result.get_search_flight_results()
        self.log.info(len(allstops2))
        self.ut.assertListItemText(allstops2, stops)


# pytest -v --browser=chrome