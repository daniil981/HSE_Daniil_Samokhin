class CourtCase:
    def __init__(self, case_number):
        self.case_number = case_number
        self.case_participants = []
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ''


    def set_a_listening_datetime(self, case_cont):
        self.listening_datetimes.append(case_cont)
        for i in self.listening_datetimes:
            print(i)

    def add_participant(self, partic_inn):
        self.case_participants.append(partic_inn)
        for i in self.case_participants:
            print(i)

    def remove_participant(self, rem_inn):
        self.case_participants.remove(rem_inn)
        for i in self.case_participants:
            print(i)

    def make_a_decision(self, verdict_text):
        self.is_finished = True
        self.verdict = verdict_text
        print(self.verdict)
        print(self.is_finished)




ts = CourtCase(3455562)


case_str = {
'date': '5/3/2023',
'address': 'г. Москва, Московская ул., 24 д., 56 каб.',
}

ts.add_participant(3214343)
ts.add_participant(3424235)
ts.remove_participant(3424235)
ts.set_a_listening_datetime(case_str)
ts.make_a_decision('Решено в пользу ответчика')
