from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import Session as AlchemySession

from app.database.session import Session


def test_session_is_instance():
    s = Session()

    assert isinstance(s, Session)


def test_get_engine_should_return_engine():
    s = Session()

    engine = s.get_engine()

    assert isinstance(engine, Engine)


def test_enter_should_return_session():
    s = Session()

    session = s.__enter__()

    assert isinstance(session, AlchemySession)
