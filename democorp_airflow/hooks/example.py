from airflow.hooks.base import BaseHook
from airflow.models import Connection


class ExampleHook(BaseHook):
    """..."""

    def __init__(self, conn_id: str) -> None:
        """
        Example Airflow hook. Implement your own business logic here.

        :param conn_id: Airflow connection id
        """
        super().__init__()
        self._conn_id = conn_id

        self._conn: Connection | None = None

    @property
    def conn(self) -> Connection:
        """
        Cache connection to avoid re-fetching multiple times.

        :return: Airflow connection object
        """
        if self._conn is None:
            self._conn = self.get_connection(conn_id=self._conn_id)
        return self._conn

    def test_connection(self) -> tuple[bool, str]:
        """
        Verify a connection.

        :return:
        """
        try:
            # ... Implement your business logic to validate a connection here ...
            _ = self.conn
            return True, "Connection successful."
        except Exception as e:
            self.log.warning("Failed connection verification.")
            return False, str(e)
