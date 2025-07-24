import os


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template containing placeholders.
        attendees (list of dict): List of attendee information dictionaries.

    Returns:
        None

    Prints error messages for invalid inputs or file writing issues.
    """
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees should be a list of dictionaries.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees should be a list of dictionaries.")
            return

    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) or "N/A"
            placeholder = "{" + key + "}"
            invitation = invitation.replace(placeholder, value)

        output_filename = f"output_{index}.txt"

        if os.path.exists(output_filename):
            print(f"Error: The file {output_filename} already exists.")
            continue

        try:
            with open(output_filename, 'w') as file:
                file.write(invitation)
        except Exception as e:
            print(
                f"Error: Impossible to write to the file {output_filename}. Exception: {e}")
