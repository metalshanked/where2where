import streamlit as st

class CustomException(Exception):
    """A base class for this project's exceptions."""


class FileTooLarge(CustomException):
    """Custom exception for when filesize value is too large."""

    def __init__(self, value, maximum, message=None):
        if message is None and value != -1:
            message = f"File is too large [{str(value/(1024*1024))[:6]} MB], it should be at most[{maximum/(1024*1024)} MB]"
        else:
            message = 'Invalid file'
        super().__init__(message)

