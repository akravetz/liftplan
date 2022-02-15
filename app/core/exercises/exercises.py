from core.models import Exercise, MuscleGroup, ExerciseCategory

BARBELL_HIP_THRUST = Exercise(
    "Hip Thrust, Barbell",
    "https://exrx.net/WeightExercises/GluteusMaximus/BBHipThrust",
    MuscleGroup.LEGS,
    ExerciseCategory.SQUAT,
)
HIP_EXTENSION = Exercise(
    "45 Degree Hip Extension",
    "http://link.com",
    MuscleGroup.LEGS,
    ExerciseCategory.HIP_HINGE,
)
SLDL = Exercise(
    "Deadlift - Stiff Leg, Barbell",
    "http://link.com",
    MuscleGroup.LEGS,
    ExerciseCategory.HIP_HINGE,
)
CABLE_CURL = Exercise(
    "Curl - Incline, Cable",
    "http://link.com",
    MuscleGroup.BICEPS,
    ExerciseCategory.ARM_CURL,
)
HAMMER_CURL = Exercise(
    "Curl - Hammer, Cable",
    "http://link.com",
    MuscleGroup.BICEPS,
    ExerciseCategory.SQUAT,
)
WRIST_CURL = Exercise(
    "Curl - Wrist, DB",
    "https://exrx.net/WeightExercises/WristFlexors/DBWristCurl",
    MuscleGroup.BICEPS,
    ExerciseCategory.ARM_CURL,
)
CABLE_REAR_DELT = Exercise(
    "Row - Rear Delt, Cable",
    "http://link.com",
    MuscleGroup.SHOULDERS,
    ExerciseCategory.ROW,
)
CABLE_ROPE_PULLOVER = Exercise(
    "Pullover - Standing, Rope",
    "https://exrx.net/WeightExercises/LatissimusDorsi/CBBentoverPullover",
    MuscleGroup.BACK,
    ExerciseCategory.ROW,
)
DELT_Y_RAISE = Exercise(
    "Lateral Raise - Y Cable",
    "https://www.youtube.com/watch?v=XGqH9EAMmUc&t=1250s",
    MuscleGroup.SHOULDERS,
    ExerciseCategory.LATERAL_RAISE,
)
DB_PRESS = Exercise(
    "Press - Flat, DB",
    "https://www.youtube.com/watch?v=j8Z1nE7-5Ic",
    MuscleGroup.CHEST,
    ExerciseCategory.PRESS,
)
MACHINE_PRESS = Exercise(
    "Press - Flat, Machine",
    "http://link.com",
    MuscleGroup.CHEST,
    ExerciseCategory.PRESS,
)
HS_PRESS = Exercise(
    "Press - Flat, Hammer Strength",
    "http://link.com",
    MuscleGroup.CHEST,
    ExerciseCategory.PRESS,
)
INCLINE_DB_PRESS = Exercise(
    "Press - Incline, DB",
    "http://link.com",
    MuscleGroup.CHEST,
    ExerciseCategory.PRESS,
)
INCLINE_SMITH_PRESS = Exercise(
    "Press - Incline, Smith (Banded)",
    "http://link.com",
    MuscleGroup.CHEST,
    ExerciseCategory.PRESS,
)
HACK_SQUAT = Exercise(
    "Squat - Hack",
    "https://exrx.net/WeightExercises/Quadriceps/SLHackSquat",
    MuscleGroup.LEGS,
    ExerciseCategory.SQUAT,
)
QUAD_SQUAT = Exercise(
    "Squat - Heel Elevated Barbell",
    "http://link.com",
    MuscleGroup.LEGS,
    ExerciseCategory.SQUAT,
)
LEG_CURL = Exercise(
    "Leg Curl",
    "https://exrx.net/WeightExercises/Hamstrings/LVSeatedLegCurl",
    MuscleGroup.LEGS,
    ExerciseCategory.HIP_HINGE,
)
LEG_EXT = Exercise(
    "Leg Extension",
    "https://exrx.net/WeightExercises/Quadriceps/LVLegExtension",
    MuscleGroup.LEGS,
    ExerciseCategory.SQUAT,
)
LEG_PRESS = Exercise(
    "Leg Press",
    "https://www.youtube.com/watch?v=VqrZi5JmPp0",
    MuscleGroup.LEGS,
    ExerciseCategory.SQUAT,
)
CUFF_LAT_RAISE = Exercise(
    "Lateral Raise, Cuff, Laying",
    "http://link.com",
    MuscleGroup.SHOULDERS,
    ExerciseCategory.LATERAL_RAISE,
)
CHEST_SUPPORTED_ROW = Exercise(
    "Row - Chest Supported, DB",
    "https://www.youtube.com/watch?v=IRmjIkHFj3w",
    MuscleGroup.BACK,
    ExerciseCategory.ROW,
)
MEADOW_ROW = Exercise(
    "Row - Meadow, Landmine",
    "http://link.com",
    MuscleGroup.BACK,
    ExerciseCategory.ROW,
)
DB_ROW = Exercise(
    "Row - Single Arm, DB",
    "http://link.com",
    MuscleGroup.BACK,
    ExerciseCategory.ROW,
)
TBAR_ROW = Exercise(
    "Row - T-Bar",
    "http://link.com",
    MuscleGroup.BACK,
    ExerciseCategory.ROW,
)
MACHINE_PULLDOWN = Exercise(
    "Pulldown - Machine",
    "http://link.com",
    MuscleGroup.BACK,
    ExerciseCategory.PULLDOWN,
)
SINGLE_ARM_PULLDOWN = Exercise(
    "Pulldown - Single Arm, Cable",
    "http://link.com",
    MuscleGroup.BACK,
    ExerciseCategory.PULLDOWN,
)
PEC_DEC = Exercise(
    "Fly - Pec Dec", "http://link.com", MuscleGroup.CHEST, ExerciseCategory.FLY
)
REVERSE_PEC_DEC = Exercise(
    "Reverse Pec Dec", "http://link.com", MuscleGroup.SHOULDERS, ExerciseCategory.ROW
)
CABLE_FLY = Exercise(
    "Fly - Roller, Cable", "http://link.com", MuscleGroup.CHEST, ExerciseCategory.FLY
)
CABLE_CROSS_EXT = Exercise(
    "Cross Extension - Seated, Cable",
    "http://link.com",
    MuscleGroup.TRICEPS,
    ExerciseCategory.ARM_EXTENSION,
)
TOE_PRESS = Exercise(
    "Toe Press", "http://link.com", MuscleGroup.CALVES, ExerciseCategory.SQUAT
)
SEATED_CALF_RAISE = Exercise(
    "Calf Raise, Seated", "http://link.com", MuscleGroup.CALVES, ExerciseCategory.SQUAT
)
JM_PRESS = Exercise(
    "JM Press - Smith (Banded)",
    "http://link.com",
    MuscleGroup.TRICEPS,
    ExerciseCategory.ARM_EXTENSION,
)
