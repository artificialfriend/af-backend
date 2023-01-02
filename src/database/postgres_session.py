from sqlalchemy import create_engine, text

connection_string = ""

engine = create_engine(connection_string, echo=True, future=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

