from user.models import Student, User
from opportunities.models import Opportunity, Interested

class Stats:
    def __init__(self):
        self.all_students = Student.objects.all()
        self.all_users = User.objects.all()

    def get_stats(self):
        print("All Students: ", self.all_students)

        branch_wise_count = {
            "CSE": {"total": 0},
            "IT": {"total": 0},
            "ECE": {"total": 0},
            "EEE": {"total": 0},
            "MECH": {"total": 0},
            "CIVIL": {"total": 0},
        }

        branch_wise = {
            "CSE": [],
            "IT": [],
            "ECE": [],
            "EEE": [],
            "MECH": [],
            "CIVIL": [],
        }

        for s in self.all_students:
            print(s.rollno)
            key = str(s.rollno)[8:11]
            print("K = ", key)
            if key == "737":
                branch_wise["IT"].append(s)
                branch_wise_count["IT"]["total"] += 1
            """
            if key == "733":
                branch_wise["CSE"].append(s)
                branch_wise_count["CSE"]["total"] += 1
            elif key == "737":
                branch_wise["IT"].append(s)
                branch_wise_count["IT"]["total"] += 1
            elif key == "735":
                branch_wise["ECE"].append(s)
                branch_wise_count["ECE"]["total"] += 1
            elif key == "734":
                branch_wise["EEE"].append(s)
                branch_wise_count["EEE"]["total"] += 1
            elif key == "736":
                branch_wise["MECH"].append(s)
                branch_wise_count["MECH"]["total"] += 1
            elif key == "732":
                branch_wise["CIVIL"].append(s)
                branch_wise_count["CIVIL"]["total"] += 1
            """

        return branch_wise_count, branch_wise

    def get_interested(self):
        not_interested_count = 0
        interested_count = 0

        print(self.all_users)
        for s in self.all_users:
            print("S = ", s)
            try:
                interested_opps = Interested.objects.get(user=s)
                print("Interested Opps: ", interested_opps)
            except Exception as e:
                interested_opps = None
            if not interested_opps:
                not_interested_count += 1
            else:
                interested_count += 1

        return interested_count, not_interested_count