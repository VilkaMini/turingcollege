# REST API for house prices in Boston
This repository is a fully functional REST API that can predict house prices in Boston provided 13 values.
## Input requirements:
Your input to the model should be either:
1. 1D array with 13 values
2. 2D array with 1D arrays with 13 values.

## Usage with python request library:
```python
house = [4.3370e-02,
         2.1000e+01,
         5.6400e+00,
         0.0000e+00,
         4.3900e-01,
         6.1150e+00,
         6.3000e+01,
         6.8147e+00,
         4.0000e+00,
         2.4300e+02,
         1.6800e+01,
         3.9397e+02,
         4.5800e-01]

# Feeding data to the model deployed on heroku
response = requests.post("https://tc-235-house-prices.herokuapp.com/price", data=json.dumps(house))

# Printing the status code 
print(response)
# Printing predicted values
print(json.loads(response.text)["predicted"])
```

## Usage with Postman:
![](https://i.ibb.co/ZLn9dr6/Screenshot-2021-05-18-101458.png)

After passing raw information through the POST method you wil get a response prediction values.

## Handling errors:
1. Error: METHOD NOT ALLOWED -> Check the method you are using (App is accesible only with POST method)
2. Error: INPUT MUST BE A 2D ARRAY -> Data is formated in a wrong way, check if the data given meets input [requirements](#Input-requirements).



## License:

The MIT License (MIT). Please see the [license file](./LICENSE) for more information.