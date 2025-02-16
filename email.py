#you have a list of user records with email and a verification status. Extract the emails of verified users.
def email():
	users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	]
	#res=sorted(users,key=lambda x:(x["verified"]))
	res=filter(lambda x:x["verified"],users)
	print(list(res))
email()