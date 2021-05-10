from flask import Flask
import json

app = Flask(__name__)

cars = []

@app.route('/cars', methods=["GET", "POST"])
def cars() -> str:
    if request.method == "GET":
        return json.dumps(cars)

    if request.method == "POST":
        car_data = json.loads(request.data)

        if "model" in car_data and "range" in car_data:
            car_data["id"] = str(len(cars) + 1)
            cars.append(car_data)
        else:
            return json.dumps({"error": "BAD REQUEST"}), 400
        
        return json.dumps(car_data)

@app.route('/cars/<car_id>', methods=["GET", "PUT", "DELETE"])
def cars_id(car_id: str) -> str:
    if request.method == "GET":
        for car in cars:
            if car["id"] == car_id:
                return json.dumps(car)
            else:
                return json.dumps({"error": "CAR NOT FOUND"})
    
    if request.method == "PUT":
        car_data = json.loads(request.data)
        for car in cars:
            if car["id"] == car_id:
                car["model"] = car_data["model"]
                car["range"] = car_data["range"]
                return json.dumps(car)
        return json.dumps({"error": "CAR NOT FOUND"})
    
    if request.method == "DELETE":
        for car in cars:
            if car["id"] == car_id:
                cars.remove(car)
                return json.dumps({"message": "CAR WAS DELETED"}), 200
        return json.dumps({"error": "CAR NOT FOUND"})            

if __name__ == "__main__":
    app.run(debug=True)