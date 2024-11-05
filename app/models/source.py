import re
import uuid


class InvalidURLError(ValueError):
    """Exception raised for invalid URL formats."""
    pass


class Source:
    def __init__(self, url: str, name: str):
        self._validate_url(url)
        self.url = url
        self.name = name
        self.id = uuid.uuid4()  # Generate a unique UUID for each source

    def _validate_url(self, url: str):
        # Simple URL validation regex
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            # domain...
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not url or not url_pattern.match(url):
            raise InvalidURLError("Invalid URL format")
