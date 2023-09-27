from pydantic import BaseModel, Field
from typing import List


class CommentInfo(BaseModel):
    """Contain basic fields of a comment."""
    id: int = Field(...,
                    description="ID of the comment",
                    examples=['1'])
    username: str = Field(...,
                          description="User who commented on the subfeddit.",
                          examples=["dummy_user"])
    text: str = Field(...,
                      description="Content of the comment.",
                      examples=["I upgraded pydantic from v1 to v2, which "
                                "brings a lot of problems."])
    created_at: int = Field(...,
                            description="Created time of the subfeddit in Unix"
                                        " epochs.", examples=[1695757477])


class CommentsResponse(BaseModel):
    """Comments response schema."""
    subfeddit_id: int = Field(...,
                              description="ID of the subfeddit, to which the"
                                          " comments belong.",
                              examples=[1])
    limit: int = Field(10,
                       description="Max number of returning comments.",
                       examples=[10])
    skip: int = Field(0,
                      description="Number of comments to skip.",
                      examples=[0])
    comments: List[CommentInfo] = Field(...,
                                        description="Comments in this subfeddit.")


class SubfedditInfo(BaseModel):
    """Contain basic fields of a subfeddit."""
    id: int = Field(..., description="ID of the subfeddit",
                    examples=['1'])
    username: str = Field(...,
                          description="User who created the subfeddit.",
                          examples=["dummy_user"])
    title: str = Field(...,
                       description="Title of the subfeddit",
                       examples=["Pydantic Upgrading issue"])
    description: str = Field(...,
                             description="Description of the subfeddit",
                             examples=["I upgraded pydantic from v1 to v2, "
                                       "which brings a lot of problems."])


class SubfedditResponse(SubfedditInfo):
    """Subfeddit response schema."""
    limit: int = Field(10,
                       description="Max number of returning comments.",
                       examples=[10])
    skip: int = Field(0,
                      description="Number of comments to skip.",
                      examples=[0])
    comments: List[CommentInfo] = Field(...,
                                        description="Comments in this subfeddit.")


class SubfedditsResponse(BaseModel):
    """Subfeddits response schema."""
    limit: int = Field(10,
                       description="Max number of returning subfeddits.",
                       examples=[10])
    skip: int = Field(0,
                      description="Number of subfeddits to skip.",
                      examples=[0])
    subfeddits: List[SubfedditInfo] = Field(...,
                                            description="List of subfeddits "
                                                        "with brief information.")
