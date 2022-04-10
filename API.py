import requests
import jsonpath

resp=requests.get("https://reqres.in/api/users?page=2")
response=resp.json()
print(response)
print(response["total_pages"])
assert response['total']==13,"NOt a correct count"