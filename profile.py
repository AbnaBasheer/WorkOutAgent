user_profile = {
    "age": None,
    "height": None,
    "weight": None,
    "medical_conditions": None,
    "medications": None,
    "goal": None,
}

required_fields = ["age", "height", "weight", "goal"]

def update_profile(key, value):
    if key in user_profile and value is not None:
        user_profile[key] = value

def is_profile_complete():
    return all(user_profile[field] is not None for field in required_fields)

def profile_summary():
    return "\n".join(f"{k}: {v}" for k,v in user_profile.items())