import copy
import datetime
import itertools
from typing import List
from .session import session_scope
from .models.subfeddit import Subfeddit, Comment


positive_sentences = ["It looks great!", "Love it.", "Awesome.", "Well done!",
                      "Looks decent.", "What you did was right.", "Thumbs up.",
                      "Like it a lot!", "Good work.", "Luckily you did it.",
                      "Proud of you.", "Enjoy!"]
negative_sentences = ["You have done it in a wrong way.", "Don't do it.",
                      "Leave it alone.", "Walk away!", "Come on dude.",
                      "Why are you doing this?", "Are you insane?",
                      "I don't like it at all.", "Nooooooo!", "Hate it!"]
subfeddits = ["Dummy Topic 1", "Dummy Topic 2", "Dummy Topic 3"]


def generate_comment_texts(sentences: List[str]) -> List[str]:
    """Generate comment texts with given sentences.

    The logic of this function is to combine the single sentence to each other
    to generate a new sentence.

    Args:
        sentences (:obj:`list` of :obj:`str`]): base sentences for generating
          complex sentences by combining any of them.

    Returns:
        List[str]: Generated comment texts.
    """
    comment_texts = copy.deepcopy(sentences)
    for i in range(2, 5):
        combinations = itertools.product(*([sentences] * i))
        comment_texts += [" ".join(combination) for combination in combinations]
    return comment_texts


def flash_contents() -> None:
    """Flash contents to DB."""
    comment_texts = generate_comment_texts(positive_sentences)
    comment_texts += generate_comment_texts(negative_sentences)
    for i in range(1, len(subfeddits) + 1):
        comments = [Comment(username=f"user_{j}",  # type: ignore
                            text=comment_text,
                            created_at=datetime.datetime.timestamp(datetime.datetime.utcnow() - datetime.timedelta(hours=len(comment_texts) - j)))  # noqa: E501
                    for j, comment_text in enumerate(comment_texts)]
        subfeddit = Subfeddit(username=f"admin_{i}", title=subfeddits[i - 1],  # type: ignore
                              description=subfeddits[i - 1], comments=comments)
        with session_scope() as session:
            session.add(subfeddit)
            session.commit()
