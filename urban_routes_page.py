import locators
from selenium.webdriver import Keys
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class UrbanRoutesPage:


    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

        #establecer ruta desde
    def set_from(self, from_address):
        self.wait.until(EC.visibility_of_element_located(locators.from_field))
        self.driver.find_element(*locators.from_field).send_keys(from_address)

        #agregar valor desde
    def get_from(self):
        return self.driver.find_element(*locators.from_field).get_property('value')

        #establcer ruta hasta
    def set_to(self, to_address):
        self.wait.until(EC.visibility_of_element_located(locators.to_field))
        self.driver.find_element(*locators.to_field).send_keys(to_address)

        #agregar valor hasta
    def get_to(self):
        return self.driver.find_element(*locators.to_field).get_property('value')

        #establecer ruta
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def is_taxi_requested(self):
        return self.driver.find_element(*locators.ask_for_a_taxi_button).is_enabled() #nueva funcion para validar el click

        #pedir un taxi
    def get_taxi(self):
        self.wait.until(EC.visibility_of_element_located(locators.ask_for_a_taxi_button))
        self.driver.find_element(*locators.ask_for_a_taxi_button).click()

        #especificar el servicio a pedir
    def set_service(self):
        self.wait.until(EC.visibility_of_element_located(locators.ask_for_a_taxi_button))
        self.driver.find_element(*locators.comfort_button).click()

    def get_service_status(self):
        button = self.driver.find_element(*locators.comfort_button) #Nueva funcion para validar el servicio
        return 'Comfort' in button.text
        #return 'active' in button.get_attribute('class')

        #click en numero de telefono
    def add_phone(self):
        self.driver.find_element(*locators.telephone_number_field).click() ############

        #agregar telefono
    def add_number_phone(self, phone):
        self.driver.find_element(*locators.number_phone).send_keys(phone)

        #insertar telefono
    def get_number_phone(self):
        return self.driver.find_element(*locators.number_phone).get_property('value')

        #enviar nuemro de telefono
    def phone_number_submit(self):
        self.driver.find_element(*locators.next_button).click()

    def is_phone_number_submitted(self):
        return self.driver.find_element(*locators.next_button).is_enabled() #nueva funcion para dar click y enviar nuemro de telefono

        #solicitar codigo
    def set_code(self, code):
        self.driver.find_element(*locators.code_phone).send_keys(code)

        #confirmar codigo
    def send_code_phone(self):
        self.driver.find_element(*locators.confirm_code).click()

        #agregar metodo de pago
    def add_payment_method(self):
        self.driver.find_element(*locators.payment_method).click()

    def is_selected_payment_method(self):
        return self.driver.find_element(*locators.payment_method).is_enabled() #funcion para dar click al metodo de pago

        #insertar tarjeta
    def set_card(self):
        self.wait.until(EC.visibility_of_element_located(locators.add_card_button))
        self.driver.find_element(*locators.add_card_button).click()

    def is_add_card(self):
        return self.driver.find_element(*locators.add_card_button).is_enabled() #funcion para dar click a agregar tarjeta

        #insertar numero de tarjeta
    def add_card_number(self, card):
        self.driver.find_element(*locators.card_number).send_keys(card)

        #solicitar numero de tarjeta
    def get_card_number(self):
        return self.driver.find_element(*locators.card_number).get_property('value')

        #insertar codigo de tarjeta
    def add_card_code(self, card_code_data):
        self.driver.find_element(*locators.card_code).send_keys(card_code_data)

        #solicitar codigo
    def get_card_code(self):
        return self.driver.find_element(*locators.card_code).get_property('value')

    def activate_payment_card(self):
        return self.driver.find_element(*locators.card_code).is_enabled()  #Funcion para validar TAB

        #activar boton agregar
    def active_button_add(self):
        self.driver.find_element(*locators.card_code).send_keys(Keys.TAB)

    def is_active_button_add(self):
        return self.driver.find_element(*locators.card_code).is_enabled()

        #agregar informacion de tarjeta
    def is_add_card_information(self):
        return self.driver.find_element(*locators.add_button).is_enabled()  ####

        #enviar informacion de tarjeta
    def add_card_information(self):
        self.driver.find_element(*locators.add_button).click()  ###

        #cerrar ventana metodo de pago
    def close_payment_method(self):
        self.wait.until(EC.visibility_of_element_located(locators.close_payment_method_modal))
        self.driver.find_element(*locators.close_payment_method_modal).click()

    def is_payment_method_closed(self):
        try:
            if self.driver.find_element(*locators.close_payment_method_modal).is_enabled():
                return True
            else:
                return False

        except NoSuchElementException:
            return False

        #establecer mensaje al conductor
    def set_message_driver(self, message):
        self.driver.find_element(*locators.message_to_driver).send_keys(message)

        #enviar mensaje al conductor
    def get_message_to_driver(self):
        return self.driver.find_element(*locators.message_to_driver).get_property('value')

        #solciitar pañuelos
    def request_blanket_to_driver(self):
        self.driver.find_element(*locators.activate_button).click()

    def is_request_blanket_to_driver(self):
        return self.driver.find_element(*locators.activate_button).is_enabled()

        #solicitar Helados
    def increment_button_ice_cream(self):
        actions = ActionChains(self.driver)
        actions.double_click(self.driver.find_element(*locators.increment_button)).perform()

        #confirmar solicitud
    def ice_cream_order(self):
        return self.driver.find_element(*locators.ice_cream_counter).text

        #solicitar taxi
    def button_request_a_taxi(self):
        self.driver.find_element(*locators.request_a_taxi).click()

    def is_request_a_taxi(self):
        return self.driver.find_element(*locators.request_a_taxi).is_enabled() #funcion para dar click a solicitar taxi








