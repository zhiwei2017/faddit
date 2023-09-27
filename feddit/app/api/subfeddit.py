from typing import Any
from fastapi import APIRouter, HTTPException
from ..db.session import session_scope
from ..db.models.subfeddit import Subfeddit, Comment
from ..schemas.subfeddit import (
    SubfedditResponse, SubfedditsResponse, CommentsResponse
)

subfeddit_router = APIRouter()


@subfeddit_router.get("/subfeddits/", response_model=SubfedditsResponse,
                      response_description="A json response containing brief"
                                           " information of extracted "
                                           "subfeddits.")
async def get_subfeddits(skip: int = 0, limit: int = 10) -> SubfedditsResponse:
    """Get brief information of max `limit` number of subfeddits with skipping
    `skip` number of subfeddits .

    \f
    Args:
        skip (int): Number of subfeddits to skip. Default value is 0.
        limit (int): Max number of subfeddits to return. Default value is 10.

    Returns:
        SubfedditsResponse: A json response containing brief information of
        extracted subfeddits.
    """
    with session_scope() as session:
        subfeddits = session.query(Subfeddit).offset(skip).limit(limit).all()
        subfeddits = [subfeddit._asdict() for subfeddit in subfeddits]
    return SubfedditsResponse(skip=skip, limit=limit, subfeddits=subfeddits)


@subfeddit_router.get("/subfeddit/", response_model=SubfedditResponse,
                      response_description="A json response containing detailed"
                                           " information of the subfeddit with"
                                           " given `subfeddit_id`.")
async def get_subfeddit_info(subfeddit_id: int) -> SubfedditResponse:
    """Get detailed information of the subfeddit with given `subfeddit_id`.

    \f
    Args:
        subfeddit_id (int): ID of the subfeddit for returning.

    Returns:
        SubfedditResponse: A json response containing detailed information of
        the subfeddit with given `subfeddit_id`.
    """
    skip, limit = 0, 10
    with session_scope() as session:
        subfeddit = session.query(Subfeddit).filter_by(id=subfeddit_id)
        subfeddit = subfeddit.one_or_none()
        if not subfeddit:
            raise HTTPException(status_code=404, detail="No subfeddit found.")
        subfeddit_info = subfeddit._asdict()
        comments = session.query(Comment).filter_by(subfeddit_id=subfeddit_id)
        comments = comments.offset(skip).limit(limit).all()
        comments = [comment._asdict() for comment in comments]

    return SubfedditResponse(**subfeddit_info, skip=skip, limit=limit,
                             comments=comments)


@subfeddit_router.get("/comments/", response_model=CommentsResponse,
                      response_description="A json response containing comments"
                                           " information of the desired"
                                           " subfeddit.")
async def get_subfeddit_comments(subfeddit_id: int, skip: int = 0,
                                 limit: int = 10) -> CommentsResponse:
    """Provide version information about the web service.

    \f
    Args:
        subfeddit_id (int): ID of the subfeddit for returning.
        skip (int): Number of comments to skip. Default value is 0.
        limit (int): Max number of comments to return. Default value is 10.

    Returns:
        CommentsResponse: A json response containing comments information of the
        desired subfeddit.
    """
    with session_scope() as session:
        comments = session.query(Comment).filter_by(subfeddit_id=subfeddit_id)
        comments = comments.offset(skip).limit(limit).all()
        comments = [comment._asdict() for comment in comments]
    return CommentsResponse(subfeddit_id=subfeddit_id, skip=skip, limit=limit,
                            comments=comments)
