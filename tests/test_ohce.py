from datetime import datetime


def get_time():
    return datetime.now().hour


def get_response(name, time_function=get_time):
    current_hour = time_function()
    if 6 < current_hour >= 20:
        return f"¡Buenas noches {name}!"
    return f"¡Buenos días {name}!"


def test_between_20_and_6_returns_buenas_noches():

    response = get_response("Daniel", lambda: 20)

    assert response == "¡Buenas noches Daniel!"


def test_says_buenos_dias_daniel():

    response = get_response("Daniel")

    assert response == "¡Buenos días Daniel!"


def test_says_buenos_dias_pedro():

    response = get_response("Pedro")

    assert response == "¡Buenos días Pedro!"
