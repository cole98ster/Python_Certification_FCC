def add_setting(settings, pair):
    key = pair[0]
    key = key.lower()
    value = pair[1]
    value = value.lower()
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key]= value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pair):
    key = pair[0]
    key = key.lower()
    value = pair[1]
    value = value.lower()
    if key in settings.keys():
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings.keys():
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        view_message = 'Current User Settings:\n'
        for key, value in settings.items():
            key = key.capitalize()
            view_message += f"{key}: {value}\n"
        return view_message

test_settings = {
    'theme': 'dark',
     'notifications': 'enabled',
      'volume': 'high'}
view_settings(test_settings)
