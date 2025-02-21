import data
import time
from selenium import webdriver
from urban_routes_page import UrbanRoutesPage


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_get_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_taxi()
        routes_page.set_service()

    def test_test_get_number_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number_value =data.phone_number
        routes_page.add_phone()
        routes_page.add_number_phone(phone_number_value)
        assert routes_page.get_number_phone() == phone_number_value

    def test_send_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.phone_number_submit()

    def test_send_code_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_code(retrieve_phone_code(self.driver))
        routes_page.send_code_phone()

    def test_get_payment(self):
        route_page = UrbanRoutesPage(self.driver)
        route_page.add_payment_method()

    def test_set_card(self):
        route_page = UrbanRoutesPage(self.driver)
        route_page.set_card()

    def test_get_card_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        number_payment_card = data.card_number
        routes_page.add_card_number(number_payment_card)
        number_card_code = data.card_code
        routes_page.add_card_code(number_card_code)
        assert routes_page.get_card_number() == number_payment_card
        assert routes_page.get_card_code() == number_card_code

    def test_active_button_add(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.active_button_add()

    def test_add_card_active(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_card_information()

    def test_close_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.close_payment_method()

    def test_get_message_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.set_message_driver(message)
        assert routes_page.get_message_to_driver() == message

    def test_activate_button_to_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_blanket_to_driver()

    def test_add_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.increment_button_ice_cream()
        assert routes_page.ice_cream_order() == '2'

    def test_take_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.button_request_a_taxi()


    @classmethod
    def teardown_class(cls):
        time.sleep(60)
        cls.driver.quit()
