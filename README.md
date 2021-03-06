## Naree

A REST service to help bangalore police and public

* Ensure women safety using quick and easy set of REST end points for signup/otp-verification/locationtracking/crime reporting
* Reach crime spots quickly
* Notifying about crime to nearby policemen
* Document and analyze the crime freequency and behavior
* Enable authentication through mobile number verification and api for quick help requests
* call / sms about crime and location to all the registered policemen (routes to nearest first)

## REST endpoints

* POST '/signup'   - signup with name,gender,phone and  age
* POST '/otp'      - request to send otp to user identified by user_id
* POST '/verify'   - request to verify the user given user id and the otp message recieved
* POST '/location' - request to set the location given user_id and location as lat and long
* POST '/crime'    - request to notify about possible crime or a situation that demands police help


## Sample curl requests


```sh
 
curl -XPOST http://127.0.0.1:5000/signup -H 'Content-Type: application/json' --data '{"name":"sarath","gender":"male","phone":"8105651525","age":22}'

curl -XPOST http://127.0.0.1:5000/otp -H 'Content-Type: application/json' --data '{"user_id":"97030700511140d3afb0fd927e875432"}'

curl -XPOST http://127.0.0.1:5000/verify -H 'Content-Type: application/json' --data '{"user_id":"97030700511140d3afb0fd927e875432","otp":75732}'
 
curl -XPOST http://127.0.0.1:5000/location -H 'Content-Type: application/json' --data '{"user_id":"42e75852e92a405f94c505bc62383a3f","lat":"9.2505757","long": "70.999999999400806"}'

curl -XPOST http://127.0.0.1:5000/crime -H 'Content-Type: application/json' --data '{"user_id":"f7a5e414949940bfa2b7e60a5b67ef42","lat":"9.2505757","long": "70.5400806"}'

```

## NOTES

* To run the service please check INSTALL
* The police men also uses the same signup mechanism and verification but the system identifies the people as PUBLIC or POLICE by checking the phonenumber to be included in a list of police numbers.
* Here i have attached a possible application prototype as a pdf which can be built using the service (Naree.pdf)