from AQA_exams.fourteen.fsm.state import State

# Start of our states
class S1(State):
    """
    The initial state
    """

    def on_event(self, event):
        if event == '1':
            return S2()
        elif event == '0':
            return S3()

        return self


class S2(State):
    """
    S2 state
    """

    def on_event(self, event):
        if event == '1':
            return S4()
        elif event == '0':
            return S3()

        return self


class S3(State):
    """
    S3 state
    """

    def on_event(self, event):
        if event == '1':
            return S2()
        elif event == '0':
            return S4()

        return self


class S4(State):
    """
    This is the end state
    """

    def on_event(self, event):
        if event == '1':
            return S4()
        elif event == '0':
            return S4()

        return self

# End of our states.