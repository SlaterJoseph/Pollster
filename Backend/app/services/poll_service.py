from app.models.poll_model import PollCreate, PollResponse


def create_poll(poll: PollCreate) -> PollResponse:
    """
    Creates a new poll.
    :param poll: The poll payload
    :return: The created poll response
    """
    pass