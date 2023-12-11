import json
from unittest import mock

from democorp_airflow.hooks.example import ExampleHook


@mock.patch.dict(
    "os.environ",
    AIRFLOW_CONN_MYDB=json.dumps(
        {
            "conn_type": "my-conn-type",
            "login": "my-login",
            "password": "my-password",
            "host": "my-host",
            "port": 1234,
            "schema": "my-schema",
            "extra": {"param1": "val1", "param2": "val2"},
        }
    ),
)
def test_examplehook():
    """This test verifies fetching of a connection."""
    test_hook = ExampleHook(conn_id="mydb")
    test_hook.test_connection()
