from dataclasses import dataclass, field
from .models import Intensifier

@dataclass
class Myorep(Intensifier):
    def name(self):
        return "myorep set"

    def description(self):
        return (
            "perform a set to 2-3RIR, then perform sets "
            + "of 5 reps with 5 second rest in between.  "
            + " Once you can no longer perform 5 reps, stop"
        )


@dataclass
class Dropset(Intensifier):
    n_drops: int = field(default=1)

    def name(self):
        return "drop set"

    def description(self):
        return (
            "perform working set, drop the weight 20%"
            + f"and perform another set to failure.  Do this {self.n_drops} times."
        )


@dataclass
class Partial(Intensifier):
    n_reps: int

    def name(self):
        return "partial set"

    def description(self):
        return f"perform a set of {self.n_reps} partials"


class IsoHold(Intensifier):
    hold_seconds: int

    def name(self):
        return "isometric hold"

    def description(self):
        return f"hold in the eccentric position for {self.hold_seconds} seconds"
