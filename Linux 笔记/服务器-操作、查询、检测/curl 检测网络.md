curl -w "Lookup time: %{time_namelookup}\nConnect time: %{time_connect}\nPretransfer time: %{time_pretransfer}\nStarttransfer time: %{time_starttransfer}\nTotal time: %{time_total}\n" --location 'http://wan610.weinpay.com:9007/load_redis_data' --header 'Content-Type: application/json' --data '{
    "token": "encrypt_token"
}'

返回数据：

{"code":0,"message":"Redis中没有找到数据"}


网络调试信息：

Lookup time: 0.001564
Connect time: 0.019574
Pretransfer time: 0.019622
Starttransfer time: 0.038337
Total time: 0.039048