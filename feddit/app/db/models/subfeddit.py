from datetime import datetime
from sqlalchemy import ForeignKey, Integer, String, Boolean, DateTime  # type: ignore
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship  # type: ignore
from typing import List
from ..base import Base


class Subfeddit(Base):
    """A subreddit like stuff, places to start discussions with different people.

    Attributes:
        id (int): unique identifier of the subfeddit.
        username (str): user, who started the subfeddit.
        title (str): topic of the subfeddit.
        description (str): short description of the subfeddit.
        comments (:obj:`list` of :obj:`Comment`): comments under the subfeddit.
    """
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    comments: Mapped[List["Comment"]] = relationship(back_populates="subfeddit")


class Comment(Base):
    """Comment on the subfeddit.

    Attributes:
        id (int): unique identifier of the comment.
        subfeddit_id (int): referred subfeddit id.
        username (str): user, who made/wrote the comment.
        text (str): content of the comment in free text format.
        created_at (int): timestamp in unix epoch time, when the comment was made.
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subfeddit_id: Mapped[int] = mapped_column(ForeignKey("subfeddit.id"))
    subfeddit: Mapped["Subfeddit"] = relationship(back_populates="comments")
    username: Mapped[str] = mapped_column(String, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[int] = mapped_column(Integer,
                                            default=datetime.timestamp(datetime.utcnow()))
