"""
User module
"""


class User:
    """
    User class for user-related operations.
    """

    def __init__(self, username: str):
        """
        Initialize a new User.

        :param username: The username of the user.
        """
        self.username = username

    def get_username(self) -> str:
        """
        Get the username of the user.

        :return: The username of the user.
        """
        return self.username
