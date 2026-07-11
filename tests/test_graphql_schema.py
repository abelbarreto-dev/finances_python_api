from fastapi.testclient import TestClient

from app import app


def test_post_graphql_rejects_operations_not_defined_in_schema() -> None:
    client = TestClient(app)
    response = client.post(
        "/graphql",
        json={"query": "mutation { unknownOperation }"},
    )

    assert response.status_code == 400
    assert "unknownOperation" in response.json()["errors"][0]["message"]


def test_post_graphql_executes_known_mutation() -> None:
    client = TestClient(app)
    response = client.post(
        "/graphql",
        json={
            "query": (
                'mutation { loginUser(user: {username: "demo", password: "12345678"}) '
                "{ username email } }"
            )
        },
    )

    assert response.status_code == 200
    assert response.json()["data"]["loginUser"]["username"] == "demo"
