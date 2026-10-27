from AI_LAB import ClassroomAgent
agent = ClassroomAgent()
test = [
    ((29, True), ("COOL", True)),((29, True), ("COOL", False)),
    ((20, True), ("IDLE", True)),((26, True), ("IDLE", False)),
    ((19, True), ("WARM", True)),((29, False), ("ECO", True)),
]
for num, (percept,expected) in enumerate(test,1):
    actual = agent.act*(percept)
    assert actual == expected,(
        f"Test{num} = Failed:"
        f"expected {expected}, got {actual}"
    )
    print(f"Test{num}:Pass")
print("All test passed")