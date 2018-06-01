class Vitals:
    def __init__(self):
        """
        For mental stats goes, just like for physical stats; 100 = good, 0 = problem.
        This list can be expanded indefinately.
        Convention:
            Physical attributes can receive damage, other attributes follow from the physical ones.
            All attributes can be set through the set_vital function
        """
        def vi(health: int = 100, status: str = "healthy") -> list: return [health, status]
        self.vitals = {
            "general": {
                "hunger": vi(),
                "thirst": vi(),
                "joy": vi(),
                "health": vi(),
                },
            "physical": {
                "head": {
                    "left_eye": vi(),
                    "right_eye": vi(),
                    "left_ear": vi(),
                    "right_ear": vi(),
                    "mouth": vi(),
                    "brain": vi(),
                    "nose": vi(),
                    "jaw": vi(),
                    },
                "upper_torso": {
                    "neck": vi(),
                    },
                },
            "mental": {
                "panic": vi(),
                "fear": vi(),
                "happiness": vi(),
                "joy": vi(),
                "coordination": vi(),
                },
            }

        def set_vital(self, category, part, subpart):
            """
            Should check whether some other things happen when you change a vital.
            E.g. => If the neck is destroyed, some other stuff should happen too.
            """
            pass

        def receive_damage(self, part, subpart):
            """
            Semirandomizer function to decide where damage goes.
            """
            pass
