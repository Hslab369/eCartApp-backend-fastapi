from sqlmodel import Field, Session, SQLModel, create_engine, select

DATABASE_URL = "sqlite:///./eCartApp.db"
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session