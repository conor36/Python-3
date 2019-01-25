class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def greater_than(self, t):
        convert = self.goals * 3
        s_total = convert + self.points
        con = t.goals * 3
        t_total = con + t.points
        if t_total < s_total:
            return True
        else:
            return False

    def less_than(self, t):
        convert = self.goals * 3
        s_total = convert + self.points
        con = t.goals * 3
        t_total = con + t.points
        if t_total > s_total:
            return True
        else:
            return False

    def equal_to(self, t):
        convert = self.goals * 3
        s_total = convert + self.points
        con = t.goals * 3
        t_total = con + t.points
        if s_total == t_total:
            return True
        else:
            return False
