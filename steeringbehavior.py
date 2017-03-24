"""SteeringBehavior."""

from gametemplate import GameTemplate

class SteeringBehavior(GameTemplate):
    """Seeking Behavior."""

    def __init__(self, name):
        """Initialize."""
        super(SteeringBehavior, self).__init__()
        self._name = name
        self._gameobjects = []


    def addtobatch(self, gameobject):
        """Add gameobjects to this game."""
        self._gameobjects.append(gameobject)

    def update(self):
        """Update this games logic."""
        if not super(SteeringBehavior, self).update():
            return False
        return True

    def draw(self):
        """Draw all gameobjects added to this game."""
        super(SteeringBehavior, self).draw()

    def run(self):
        """Need documentation."""
        if super(SteeringBehavior, self).startup():
            while self.update():
                self.draw()
        super(SteeringBehavior, self).shutdown()
