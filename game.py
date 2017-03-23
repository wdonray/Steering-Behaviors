"""Main Game File."""


class Game(object):
    """Game Class."""

    def __init__(self):
        """Constructor."""
        self.batch = []

    def add_to_batch(self, obj):
        """Add_to_batch."""
        self.batch.append(obj)

    def start(self):
        """Start."""
        pass

    def update(self, deltatime):
        """Update."""
        pass

    def draw(self):
        """Draw."""
        pass

    def run(self):
        """Run."""
        pass

    def exit(self):
        """Exit."""
        pass
