user_story_headers = ["Id", "Story Title", "User Story", "Acceptance Criteria", "Business Value", "Estimation", "Status"]

test_user_stories = \
[
    {
        "Id": 1, "Story Title": "Test User Story 1", "User Story": "...",
        "Acceptance Criteria": "It works",
        "Business Value": 1000, "Estimation": 4, "Status": "TODO"
    },
    {
        "Id": 2, "Story Title": "Some Test Story", "User Story": "...",
        "Acceptance Criteria": "Something",
        "Business Value": 500, "Estimation": 6, "Status": "In Progress"
    },
    {
        "Id": 3, "Story Title": "Super Sprinter works", "User Story": "...",
        "Acceptance Criteria": "Super Sprinter is done",
        "Business Value": 20000, "Estimation": 4, "Status": "Planning"
    },
]


def get_display_value(user_story, key):
    value = user_story[key]

    if key == "Business Value":
        return str(value) + " points"
    elif key == "Estimation":
        return str(value) + "h"
    else:
        return value


def get_new_id():
    max_val = 0
    for dic in test_user_stories:
        if dic["Id"] > max_val:
            max_val = dic["Id"]

    return max_val + 1


def get_user_story_by_id(user_story_id):
    for user_story in test_user_stories:
        if user_story["Id"] == user_story_id:
            return user_story
    return None


def update_user_story(data):
    index = -1
    user_story_id = data["Id"]

    for i in range(len(test_user_stories)):
        user_story = test_user_stories[i]
        if user_story["Id"] == user_story_id:
            index = i
            break

    if index != -1:
        test_user_stories[index] = data
