import core.models
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
                    ES(ex.INCLINE_DB_PRESS, [S(6, 8)] * 3),
                    ES(ex.INCLINE_SMITH_PRESS, [S(8, 10)] * 3),
                    ES(ex.CABLE_FLY, [S(10, 12)] * 3),
                    ES(ex.DELT_Y_RAISE, [S(10, 12)] * 4),
                    ES(ex.JM_PRESS, [S(10, 12)] * 4),
                ],
            ),
            D(
                "Pull A",
                "All exercises performed to 2-3 RIR",
                1,
                [
                    ES(ex.DB_ROW, [S(6, 8)] * 3),
                    ES(ex.CHEST_SUPPORTED_ROW, [S(8, 10)] * 3),
                    ES(ex.TBAR_ROW, [S(10, 12)] * 3),
                    ES(ex.REVERSE_PEC_DEC, [S(10, 12)] * 4),
                    ES(ex.CABLE_CURL, [S(10, 12)] * 4),
                ],
            ),
            D(
                "Lower A",
                "All exercises performed to 2-3 RIR",
                2,
                [
                    ES(ex.QUAD_SQUAT, [S(6, 8)] * 3),
                    ES(ex.HACK_SQUAT, [S(8, 10)] * 3),
                    ES(ex.LEG_EXTENSION, [S(10, 12)] * 3),
                    ES(ex.LEG_CURL, [S(10, 12)] * 3),
                    ES(ex.TOE_PRESS, [S(10, 12)] * 3),
                ],
            ),
            D(
                "Push B",
                "All exercises performed to 2-3 RIR",
                3,
                [
                    ES(ex.DB_PRESS, [S(6, 8)] * 3),
                    ES(ex.HS_PRESS, [S(8, 10)] * 3),
                    ES(ex.PEC_DEC, [S(10, 12)] * 3),
                    ES(ex.CUFF_LAT_RAISE, [S(10, 12)] * 3),
                    ES(ex.CABLE_CROSS_EXT, [S(10, 12)] * 3),
                ],
            ),
            D(
                "Pull B",
                "All exercises performed to 2-3 RIR",
                4,
                [
                    ES(ex.MACHINE_PULLDOWN, [S(6, 8)] * 3),
                    ES(ex.SINGLE_ARM_PULLDOWN, [S(8, 10)] * 3),
                    ES(ex.CABLE_ROPE_PULLOVER, [S(10, 12)] * 3),
                    ES(ex.CABLE_REAR_DELT, [S(10, 12)] * 3),
                    ES(ex.HAMMER_CURL, [S(10, 12)] * 3),
                ],
            ),
            D(
                "Lower B",
                "All exercises performed to 2-3 RIR",
                5,
                [
                    ES(ex.SLDL, [S(6, 8)] * 3),
                    ES(ex.HIP_EXTENSION, [S(8, 10)] * 3),
                    ES(ex.LEG_CURL, [S(10, 12)] * 3),
                    ES(ex.LEG_PRESS, [S(10, 12)] * 3),
                    ES(ex.SEATED_CALF_RAISE, [S(10, 12)] * 3),
                ],
            ),
        ],
    ),
    models.Block("Intensity Block", 4, []),
    models.Block("Finishing Block", 4, []),
]
