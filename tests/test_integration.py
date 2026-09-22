from src.app import activities


def test_student_can_signup_and_unregister_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"
    participants_before = list(activities[activity_name]["participants"])

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    activities_after_signup = client.get("/activities").json()
    unregister_response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )
    activities_after_unregister = client.get("/activities").json()

    # Assert
    assert signup_response.status_code == 200
    assert email in activities_after_signup[activity_name]["participants"]
    assert unregister_response.status_code == 200
    assert activities_after_unregister[activity_name]["participants"] == participants_before
