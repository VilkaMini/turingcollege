from factory.py import Tesla

def test_tesla_color:
  tesla = Tesla("ModelX", "black")
  assert tesla.color == "black"

def test_tesla_seat_count:
  tesla = Tesla("ModelX", "black")
  assert tesla.seats_count == 5
