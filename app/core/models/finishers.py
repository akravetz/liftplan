from .models import Finisher


class TricepFinisher(Finisher):
    def name(self):
        return "Tricep Trouble"

    def description(self):
        return "Banded extension 10-12, Baded CG pushup AMRAP, 3 sets"


class BicepFinisher(Finisher):
    def name(self):
        return "Bicep Blast"

    def description(self):
        return "Spider curls, Incline DB Curls, Hammer Curls. 10-15 reps, 3 sets"


class CalfFinisher(Finisher):
    def name(self):
        return "Calftastrophe"

    def description(self):
        return "hip loaded calf raise, seated calf raise, squatting calf raise. 15 reps, 3 sets"


class PushDeltFinisher(Finisher):
    def name(self):
        return "Delt 60s Death"

    def description(self):
        return "cuff cable rear delt, Y raise, face pull. 10-15 reps, 3 sets."


class PullDeltFinisher(Finisher):
    def name(self):
        return "Delt 60s Death"

    def description(self):
        return ("seated Y raise (pulsed), standing Y raise, "+
    "standing lateral partials, iso stretch. 20 reps, 3 sets")
