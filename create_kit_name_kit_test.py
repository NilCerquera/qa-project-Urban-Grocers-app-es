import data
import sender_stand_request
# Pruebas, generamos las pruebas positivas y negativas del caso
# prueba positiva


def positive_assert(kit_body):
    user_response_new_kit = sender_stand_request.post_new_client_kit(kit_body)
    assert user_response_new_kit.status_code == 201
# prueba negativa


def negative_assert_code_400(kit_body):
    user_response_new_kit = sender_stand_request.post_new_client_kit(kit_body)
    assert user_response_new_kit.status_code == 400
# Ingresamos la prueba de 1 solo caracter


def test_create_kit_name_only_char():
    kit_body_two = data.only_letter
    positive_assert(kit_body_two)
# prueba 2


def test_create_kit_511_name():cd 
    kit_body_three = data.five_hundred_eleven_letters
    positive_assert(kit_body_three)
# prueba 3


def test_create_kit_name_empty_string():
    kit_body_four = data.empty_letters_string
    negative_assert_code_400(kit_body_four)
    # prueba 4


def test_create_kit_512_name():
    kit_body_five = data.five_hundred_twelve_letters
    negative_assert_code_400(kit_body_five)
# prueba 5


def test_create_characters_special():
    kit_body_six = data.characters_special
    positive_assert(kit_body_six)
# prueba 6


def test_create_spaces_allowed():
    kit_body_seven = data.kits_spaces
    positive_assert(kit_body_seven)
# prueba 7


def test_create_numbers_allowed():
    kit_body_eight = data.numbers_kit
    positive_assert(kit_body_eight)
# prueba 8


def test_create_request_not_passed():
    kit_body_nine = data.empty_letters
    negative_assert_code_400(kit_body_nine)
# prueba 9


def test_create_parameters_numbers():
    kit_body_ten = data.invalid_data
    negative_assert_code_400(kit_body_ten)
