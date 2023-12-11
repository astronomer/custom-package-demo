import os

import pytest

# These have to come before any Airflow imports
os.environ["AIRFLOW__CORE__UNIT_TEST_MODE"] = "True"

from airflow.models import (  # noqa: E402
    DagModel,
    DagRun,
    DagTag,
    TaskInstance,
    TaskReschedule,
    Trigger,
    Variable,
    XCom,
)
from airflow.utils import db  # noqa: E402
from airflow.utils.session import create_session  # noqa: E402
from airflow.utils.timezone import datetime  # noqa: E402


@pytest.fixture(scope="session", autouse=True)
def airflow_db():
    """
    Session-wide fixture that ensures the database is set up for tests.
    """
    db.resetdb()


@pytest.fixture
def session():
    """
    Creates a SQLAlchemy session.
    """
    with create_session() as session:
        yield session


@pytest.fixture(autouse=True)
def clean_db(session):
    """
    Clears test database after each test is run.
    """
    session.query(Trigger).delete()
    session.query(DagRun).delete()
    session.query(TaskInstance).delete()
    session.query(DagTag).delete()
    session.query(DagModel).delete()
    session.query(TaskReschedule).delete()
    session.query(Variable).delete()
    session.query(XCom).delete()


@pytest.fixture
def context():
    """
    Creates a context with default execution date.
    """
    context = {
        "execution_date": datetime(2023, 1, 1),
        "logical_date": datetime(2023, 1, 1),
    }
    yield context
