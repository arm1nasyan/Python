import requests

URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    response = requests.get(f'{URL}/posts')
    if response.status_code == 200:
        data = response.json()
        filtered_data = [post for post in data if len(post['title'].split(" ")) > 6 and post['body'].count('\n') >= 3]
        print("Filtered data: ")
        for post in filtered_data:
            print(f"Id: {post['id']}, Title: {post['title']}")
        return filtered_data
    else:
        print(f"Get request faild with status code: {response.status_code}")
        return []
    
def create_post(payload):
    response = requests.post(f"{URL}/posts", json=payload)
    if response.status_code == 201:
        data = response.json()
        print("Created post: ", data)
        return data
    else:
        print(f"POST request faild with status code: {response.status_code}")
        return None
    
def update_post(post_id, payload):
    response = requests.put(f"{URL}/posts/{post_id}", json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Updated post: ", data)
        return data
    else:
        print(f"PUT request faild with status code: {response.status_code}")
        return None

def delete_post(post_id):
    response = requests.delete(f"{URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"Post with id {post_id} deleted successfully")
        return True
    else:
        print(f"DELETE request faild with status code: {response.status_code}")
        return False

while True:
    try:
        print("Available operations!")
        print("1. GET")
        print("2. POST")
        print("3. PUT")
        print("4. DELETE")
        print("5. Exit")
        
        choose = input("Choose an operation (1-5): ")
        
        if choose == 5:
            print("Exiting operations")
            break
        
        if choose not in ['1', '2', '3', '4']:
            print('Invalid operation, select valid operation')
            continue
        
        print("Result is:")
        match choose:
            case '1':
                get_posts()
                
            case '2':
                title = input("Enter title for new post: ")
                body = input("Enter body for new post: ")
                user_id = int(input("Enter user id for new post: "))
                create_post({"title": title, "body": body, "userId": user_id})
                
            case '3':
                post_id = int(input("Enter post id you want to edit: "))
                title = input("Enter title for editing post: ")
                body = input("Enter body for editing post: ")
                user_id = int(input("Enter user id for editing post: "))
                update_post(post_id, {"title": title, "body": body, "userId": user_id})
                
            case '4':
                post_id = int(input("Enter post id you want to delete: "))
                delete_post(post_id)

    except ValueError:
        print("Enter numeric value")