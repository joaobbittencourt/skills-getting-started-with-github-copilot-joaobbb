def test_root_redirects_to_static_index(client):
    # Arrange
    redirect_options = {"follow_redirects": False}

    # Act
    response = client.get("/", **redirect_options)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_expected_activity_data(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert "Chess Club" in activities
    assert set(activities["Chess Club"]) == expected_fields
    assert isinstance(activities["Chess Club"]["participants"], list)
