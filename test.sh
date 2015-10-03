#url -XPOST http://127.0.0.1:5000/signup -H 'Content-Type: application/json' --data '{"name":"sarath","gender":"male","phone":"+97420433616","age":22}'
#curl -XPOST http://127.0.0.1:5000/otp -H 'Content-Type: application/json' --data '{"user_id":"97030700511140d3afb0fd927e875432"}'
#curl -XPOST http://127.0.0.1:5000/verify -H 'Content-Type: application/json' --data '{"user_id":"97030700511140d3afb0fd927e875432","otp":75732}'
#curl -XPOST http://127.0.0.1:5000/location -H 'Content-Type: application/json' --data '{"user_id":"97030700511140d3afb0fd927e875432","lat":"9.2505757","long": "76.5400806"}'
