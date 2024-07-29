def update_settings(**kwargs):
    print("Updated Settings:")
    for key,value in kwargs.items():
        print(f"{key}: {value}")

def set_user(user_id, **settings):
    print(f"Updating settings for user {user_id}")
    update_settings(**settings)
set_user(123456,theme="dark",language="English",academy="Picsart")    
