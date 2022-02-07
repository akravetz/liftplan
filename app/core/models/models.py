from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod
from enum import IntEnum, Enum, auto


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


class MuscleGroup(IntEnum):
    BACK = auto()
    CHEST = auto()
    SHOULDERS = auto()
    LEGS = auto()
    CALVES = auto()
    ARMS = auto()
    ABS = auto()


class Finisher(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def description(self):
        pass


class Intensifier(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def description(self):
        pass


@dataclass
class Exercise:
    name: str
    execution_video_link: str
    muscle_group: MuscleGroup
    category: ExerciseCategory


@dataclass
class Set:
    rep_range_low: int
    rep_range_high: int
    intensifier: Optional[Intensifier] = None


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
    finisher: Optional[Finisher] = None


@dataclass
class Block:
    name: str
    n_weeks: int
    days: list[Day]


@dataclass
class Program:
    name: str
    blocks: list[Block]
