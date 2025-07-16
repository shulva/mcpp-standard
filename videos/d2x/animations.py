from manim import *

class DHighlight(Succession):
    def __init__(self, mobject, color=YELLOW, scale_factor=1.1, **kwargs):
        start_mobject = mobject.copy()
        target_mobject = mobject.copy().scale(scale_factor).set_color(color)
        super().__init__(
            Transform(mobject, target_mobject),
            Transform(mobject, start_mobject),
            run_time=1, # default run_time
            **kwargs
        )

class DCameraMove(Succession):
    def __init__(self, camera, target_mobject, scale_factor=0.5, **kwargs):
        super().__init__(
            ApplyMethod(camera.frame.scale, 1 / scale_factor),
            ApplyMethod(camera.frame.move_to, target_mobject),
            ApplyMethod(camera.frame.scale, scale_factor),
            run_time=1,  # total run_time
            **kwargs
        )