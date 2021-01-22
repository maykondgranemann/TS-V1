import sys

sys.path.append('.')

from dao.session import Session


session = Session()
assert isinstance(session, Session)
assert type(session.__enter__()) is not None
