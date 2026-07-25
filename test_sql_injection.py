def fetch_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    print("Running query:", query)
    return query

def main():
    fetch_user("1 OR 1=1")

if __name__ == "__main__":
    main()
