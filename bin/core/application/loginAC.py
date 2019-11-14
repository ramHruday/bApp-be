def validate_user(input_json):
    try:
        return {"status": "ok", "message": "Login success"}
    except:
        return {"status": "error", "message": "login failed"}
