#curl -XPOST http://127.0.0.1:5000/signup -H 'Content-Type: application/json' --data '{"name":"sarath","gender":"male","phone":"8105651525","age":22}'
#curl -XPOST http://127.0.0.1:5000/otp -H 'Content-Type: application/json' --data '{"user_id":"97030700511140d3afb0fd927e875432"}'
#curl -XPOST http://127.0.0.1:5000/verify -H 'Content-Type: application/json' --data '{"user_id":"97030700511140d3afb0fd927e875432","otp":75732}'
#curl -XPOST http://127.0.0.1:5000/location -H 'Content-Type: application/json' --data '{"user_id":"42e75852e92a405f94c505bc62383a3f","lat":"9.2505757","long": "70.999999999400806"}'
#curl -XPOST http://127.0.0.1:5000/crime -H 'Content-Type: application/json' --data '{"user_id":"f7a5e414949940bfa2b7e60a5b67ef42","lat":"9.2505757","long": "70.5400806"}'
