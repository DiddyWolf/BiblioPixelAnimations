from bibliopixel.animation import BaseStripAnim


class ColorFill(BaseStripAnim):
    """Fill the dots progressively along the strip."""

    def __init__(self, layout, color, start=0, end=-1):
        super(ColorFill, self).__init__(layout)
        self._color = color
        self._start = start
        self._end = end

    def step(self, amt=1):
        self.layout.fill(self._color, self._start, self._end)
