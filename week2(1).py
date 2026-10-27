
class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "Cool"
        elif temp < 20:
            target_mode = "Warm"
        else:
            target_mode = "Idle"
        command = target_mode != self.previous_mode
        self.previous_mode = target_mode
        return target_mode,command
agent = ClassroomAgent()

percepts = [
    (29, True),(29, True),(20, True),(26, True),(19, True),(29, False)
]
for step, percept in enumerate(percepts, 1):
    previous = agent.previous_mode
    target_mode, command = agent.act(*percept)
    
    if command:
        result = "send command"
    else:
        result = "no command"

    print(
        f"Step {step}: Previous={previous}, "
        f"Percept={percept}, Target={target_mode}, "
        f"Result={result}"
    )
ClassroomAgent()