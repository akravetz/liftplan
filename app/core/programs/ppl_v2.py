from core import models
import core.exercises as ex
from core.models import ExerciseProgram as EP
from core.models import Set as S
from core.models import Day as D


PPL_V2 = [
    models.Block(
        "Initiation Block",
        4,
        [
            D(
                "Push A",
                "All exercises performed to 2-3 RIR",
                0,
                [
                    EP(ex.INCLINE_DB_PRESS, [S(6, 8)] * 3),
                    EP(ex.INCLINE_SMITH_PRESS, [S(8, 10)] * 3),
                    EP(ex.CABLE_FLY, [S(10, 12)] * 3),
                    EP(ex.DELT_Y_RAISE, [S(10, 12)] * 4),
                    EP(ex.JM_PRESS, [S(10, 12)] * 4),
                ],
            ),
            D(
                "Pull A",
                "All exercises performed to 2-3 RIR",
                1,
                [
                    EP(ex.DB_ROW, [S(6, 8)] * 3),
                    EP(ex.CHEST_SUPPORTED_ROW, [S(8, 10)] * 3),
                    EP(ex.TBAR_ROW, [S(10, 12)] * 3),
                    EP(ex.REVERSE_PEC_DEC, [S(10, 12)] * 4),
                    EP(ex.CABLE_CURL, [S(10, 12)] * 4),
                ],
            ),
            D(
                "Lower A",
                "All exercises performed to 2-3 RIR",
                2,
                [
                    EP(ex.QUAD_SQUAT, [S(6, 8)] * 3),
                    EP(ex.HACK_SQUAT, [S(8, 10)] * 3),
                    EP(ex.LEG_EXT, [S(10, 12)] * 3),
                    EP(ex.LEG_CURL, [S(10, 12)] * 3),
                    EP(ex.TOE_PRESS, [S(10, 12)] * 3),
                ],
            ),
            D(
                "Push B",
                "All exercises performed to 2-3 RIR",
                3,
                [
                    EP(ex.DB_PRESS, [S(6, 8)] * 3),
                    EP(ex.HS_PRESS, [S(8, 10)] * 3),
                    EP(ex.PEC_DEC, [S(10, 12)] * 3),
                    EP(ex.CUFF_LAT_RAISE, [S(10, 12)] * 3),
                    EP(ex.CABLE_CROSS_EXT, [S(10, 12)] * 3),
                ],
            ),
            D(
                "Pull B",
                "All exercises performed to 2-3 RIR",
                4,
                [
                    EP(ex.MACHINE_PULLDOWN, [S(6, 8)] * 3),
                    EP(ex.SINGLE_ARM_PULLDOWN, [S(8, 10)] * 3),
                    EP(ex.CABLE_ROPE_PULLOVER, [S(10, 12)] * 3),
                    EP(ex.CABLE_REAR_DELT, [S(10, 12)] * 3),
                    EP(ex.HAMMER_CURL, [S(10, 12)] * 3),
                ],
            ),
            D(
                "Lower B",
                "All exercises performed to 2-3 RIR",
                5,
                [
                    EP(ex.SLDL, [S(6, 8)] * 3),
                    EP(ex.HIP_EXTENSION, [S(8, 10)] * 3),
                    EP(ex.LEG_CURL, [S(10, 12)] * 3),
                    EP(ex.LEG_PRESS, [S(10, 12)] * 3),
                    EP(ex.SEATED_CALF_RAISE, [S(10, 12)] * 3),
                ],
            ),
        ],
    ),
    models.Block("Intensity Block", 4, []),
    models.Block("Finishing Block", 4, []),
]
