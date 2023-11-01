class Target:

    def __init__(self, message):
        self.message = message
        pass

    def request(self) -> str:
        return f"{self.message} from default"


class Adaptee:

    def __init__(self, message):
        self.message = message
        pass

    def specific_request(self) -> str:
        return f"{self.message} from adaptee"


class Adapter(Target, Adaptee):
    def __init__(self, message):
        super().__init__(message)

    def specific_request(self) -> str:
        return f"{self.message} translated"


def client_code(target: Target) -> None:
    print(target.request(), end="")
