def add_setting(settings, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return f"Setting '{key}' does not exist! Cannot delete a non-existing setting."


def view_settings(settings):
    if not settings:
        return "No settings available.\n"

    result = "Current User Settings:\n"

    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result


def main():
    test_settings = {
        "theme": "dark",
        "notifications": "enabled",
        "volume": "high"
    }

    print(view_settings(test_settings))

    print(add_setting(test_settings, ("Language", "English")))
    print(update_setting(test_settings, ("Volume", "Medium")))
    print(delete_setting(test_settings, "Theme"))

    print()
    print(view_settings(test_settings))


if __name__ == "__main__":
    main()