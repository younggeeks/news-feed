import requests


def get_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    return r.json()


def get_single_post(post_id):
    r = requests.get('https://jsonplaceholder.typicode.com/posts/'.format(post_id))

    return r.json()


def create_single_post(title, body, id, user_id):
    r = requests.post('https://jsonplaceholder.typicode.com/posts/', data={'title': title,
                                                                           "body": body, "id": id, "user_id": user_id})
    return r.json()
