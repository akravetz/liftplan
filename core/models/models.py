from dataclasses import dataclass, field
from abc import ABC
from enum import Enum


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


class Intensifier:
    @abstractmethod
    def name():
        pass

    @abstractmethod
    def description():
        pass


@dataclass
class Myorep(Intensifier):
    n_myorep_sets: int

    def name():
        return "myorep set"

    def description():
        return f"perform a set to 2-3RIR, then perform {n_myorep_sets} sets of 5 reps with 5 second rest in between.  Once you can no longer perform 5 reps, stop"


@dataclass
class Dropset(Intensifier):
    n_drops: int

    def name():
        return "drop set"

    def description():
        return f"perform working set, drop the weight 20% and perform another set to failure.  Do this {n_drops} times."


@dataclass
class Partial(Intensifier):
    n_reps: int

    def name():
        return "partial set"

    def description():
        return f"perform a set of {n_reps} partials"


class IsoHold(Intensifier):
    hold_seconds: int

    def name():
        return "isometric hold"

    def description():
        return f"hold in the eccentric position for {hold_seconds} seconds"


@dataclass
class Set:
    rep_range_low: int
    rep_range_high: int
    intensifier: Intensifier = field(default=None)


@dataclass
class ExerciseProgram:
    exercise: Exercise
    sets: list[Set]


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
