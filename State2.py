class ReportState:
    def __init__(self, report):
        self.report = report

    def check_logic(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def change_internal_state(self):
        raise NotImplementedError("Subclasses should implement this method.")


class ReadyState(ReportState):
    def check_logic(self):
        if self.report.data_is_correct():
            self.report.set_state(ReadyState(self.report))

    def change_internal_state(self):
        self.report.internal_state = "ready"


class InQueueState(ReportState):
    def check_logic(self):
        self.report.set_state(InQueueState(self.report))

    def change_internal_state(self, service):
        if service == "Service1":
            self.report.internal_state = "inqueue_Service1"
        elif service == "Service2":
            self.report.internal_state = "inqueue_Service2"


class SendToUserState(ReportState):
    def check_logic(self):
        self.report.set_state(SendToUserState(self.report))

    def change_internal_state(self, stage):
        if stage == "VarifySMS":
            self.report.internal_state = "sendtouser_VarifySMS"
        elif stage == "SMS":
            self.report.internal_state = "sendtouser_SMS"


class CompleteState(ReportState):
    def check_logic(self):
        self.report.set_state(CompleteState(self.report))

    def change_internal_state(self):
        self.report.internal_state = "complete"


class Report:
    def __init__(self):
        self.state = None
        self.internal_state = None

    def set_state(self, state):
        self.state = state

    def data_is_correct(self):
        # Logic to check if data is correct
        return True

    def prepare_report(self):
        self.state.check_logic()
        self.state.change_internal_state()


# Example usage
report = Report()
report.set_state(ReadyState(report))
report.prepare_report()
print(report.internal_state)  # Output: ready

report.set_state(InQueueState(report))
report.state.change_internal_state("Service1")
print(report.internal_state)  # Output: inqueue_Service1

report.set_state(SendToUserState(report))
report.state.change_internal_state("VarifySMS")
print(report.internal_state)  # Output: sendtouser_VarifySMS

report.set_state(CompleteState(report))
report.prepare_report()
print(report.internal_state)  # Output: complete
