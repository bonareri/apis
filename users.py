import requests

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

if response.status_code == 200:
    user_data = response.json()
    # Loop through each user in the user data
    for user in user_data:
        name = user.get('name', 'N/A')
        username = user.get('username', 'N/A')
        email = user.get('email', 'N/A')
        address = user.get('address')
        phone_number = user.get('phone', 'N/A')

        # Extract city and street from address
        street = address.get('street', 'N/A')
        city = address.get('city', 'N/A')

        print(f"Name: {name}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Street: {street}")
        print(f"City: {city}")
        print(f"Phone: {phone_number}")
        print("-" * 40)  # Separator for readability

else:
    print(f"Failed to retrieve user data. Status code: {response.status_code}")
