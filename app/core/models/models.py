from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from enum import Enum, auto


class ExerciseCategory(Enum):
    ROW = auto()
    PRESS = auto()
    FLY = auto()
    PULLDOWN = auto()
    LATERAL_RAISE = auto()
    HIP_HINGE = auto()
    SQUAT = auto()
    ARM_CURL = auto()
    ARM_EXTENSION = auto()


class MuscleGroup(Enum):
    BACK = auto()
    CHEST = auto()
    SHOULDERS = auto()
    LEGS = auto()
    CALVES = auto()
    ARMS = auto()
    ABS = auto()


@dataclass
class Exercise:
    name: str
    execution_video_link: str
    muscle_group: MuscleGroup
    category: ExerciseCategory


class Intensifier(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def description(self):
        pass


@dataclass
class Myorep(Intensifier):
    def name(self):
        return "myorep set"

    def description(self):
        return (
            "perform a set to 2-3RIR, then perform sets "
            + "of 5 reps with 5 second rest in between.  " +
            " Once you can no longer perform 5 reps, stop"
        )


@dataclass
class Dropset(Intensifier):
    n_drops: int

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


@dataclass
class Set:
    rep_range_low: int
    rep_range_high: int
    intensifier: Intensifier = field(default=None)


@dataclass
class ExerciseProgram:
    exercise: Exercise
    sets: list[Set]


@dataclass
class Day:
    name: str
    note: str
    day_offset: int  # day 0, 1,...n etc
    exercises: list[ExerciseProgram]


@dataclass
class Block:
    name: str
    n_weeks: int
    days: list[Day]
