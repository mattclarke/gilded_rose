def get_response(name):
    pass


def test_says_buenos_dias():

    response = get_response("Pedro")

    assert response == "¡Buenos días Pedro!"
