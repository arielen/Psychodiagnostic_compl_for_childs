from importlib import resources

from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import asc, desc, func

from models import Questions, Answers


class Base:

    def __init__(self) -> None:
        with resources.path('base', 'psydiagnostic.db') as sqlite_filepath:
            self.engine = create_engine(f"sqlite:///{sqlite_filepath}")
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()

    def get_questions(self, ascending=True) -> list:
        """Get a list of questions 

        Args:
            self: database session to use
            ascending: direction to sort the results

        Returns:
            List: list of questions sorted by piblisher
        """
        if not isinstance(ascending, bool):
            raise ValueError(f"Sorting value invalid: {ascending}")

        directions = asc if ascending else desc

        return (
            self.session.query(
                Questions.name, func.count(Answers.name).label("total_answers")
            )
            .join(Questions.answers)
            .group_by(Questions.name)
            .order_by(directions("total_answers"))
        )


if __name__ == "__main__":
    main()
