from datetime import datetime


def get_time():
    return datetime.now().hour


def get_response(name, time_function=get_time):
    current_hour = time_function()
    if current_hour >= 20 or current_hour < 6:
        return f"¡Buenas noches {name}!"
    elif 6 <= current_hour < 12:
        return f"¡Buenos días {name}!"
    else:
        return f"¡Buenas tardes {name}!"


def test_between_20_and_6_returns_buenas_noches():
    response = get_response("Daniel", lambda: 20)

    assert response == "¡Buenas noches Daniel!"


def test_between_6_and_12_returns_buenos_dias():
    response = get_response("Federica", lambda: 6)

    assert response == "¡Buenos días Federica!"


def test_says_buenas_tardes_daniel():
    response = get_response("Daniel", lambda: 12)

    assert response == "¡Buenas tardes Daniel!"


def test_on_stop_says_adios():
    _ = get_response("Daniel", lambda: 12)
    response = get_response("Stop!", lambda: 12)

    assert response == "Adios Daniel"
