#url -XPOST http://127.0.0.1:5000/signup -H 'Content-Type: application/json' --data '{"name":"sarath","gender":"male","phone":"+97420433616","age":22}'
curl -XPOST http://127.0.0.1:5000/otp -H 'Content-Type: application/json' --data '{"user_id":"97030700511140d3afb0fd927e875432"}'
#curl -XPOST http://127.0.0.1:5000/verify -H 'Content-Type: application/json' --data '{"user_id":"97030700511140d3afb0fd927e875432","otp":75732}'


#curl -H 'X-APP-TOKEN:12f6ee8fb16f48d885bf7d28b35262e8' -H 'Authorization:Bearer 519a6ede0ddd4cfd81e3161982d34aac' 'http://sandbox-t.olacabs.com/v1/bookings/create?pickup_lat=12.950072&pickup_lng=77.642684&pickup_mode=NOW&category=sedan'
