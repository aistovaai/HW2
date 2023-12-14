from dataclasses import dataclass
from random import choice, randint

# модель для описания ходов
@dataclass
class NimStateChange:
    heap_id: int                                    # номер кучки
    decrease: int   



class Agent:
    """
    В этом классе реализованы стратегии игры для уровней сложности
    """       # уровень сложности


    def _make_step_hard(self, state_curr: list[int]):
        decrease_c = 0
        for heap in range(len(state_curr)):
            nim_sum = -1

            if state_curr[heap] != 0:
                for decrease in range(1, state_curr[heap]):
                    nim_sum = state_curr[heap] - decrease

                    for curr_heap in range(len(state_curr)):
                        if curr_heap != heap:
                            nim_sum = nim_sum ^ state_curr[curr_heap]

                    if nim_sum == 0:
                        heap_c = heap
                        decrease_c = decrease
                        break
            if decrease_c != 0:
                break
        
        if decrease_c == 0:
            nim_sum = 1
#           если хода нет
            for heap in range(len(state_curr)):
                nim_sum ^= state_curr[heap]

            if nim_sum == 0:
                heap_c = choice(heap for heap in range(len(state_curr)) if state_curr[heap] != 0)
                decrease_c = randint(1, state_curr[heap])

            else:
                heap_c = min(heap for heap in range(len(state_curr)) if state_curr[heap] != 0)
                decrease_c = state_curr[heap_c]

        return NimStateChange(
            heap_c,
            decrease_c
        )


    def make_step(self, state_curr: list[int]) -> NimStateChange:
        return self._make_step_hard(state_curr)



'''def test_make_step_return_value():
    state = list(range(5))

    agent = Agent(level='hard')
    step = agent.make_step(state)

    return (step)

    assert isinstance(step, NimStateChange)
    assert 0 <= step.heap_id <= len(state)
    assert 1 <= step.decrease <= state[step.heap_id]
'''
state = list(range(5))
agent = Agent()
step = agent.make_step(state)

print(step.decrease)
print(step)