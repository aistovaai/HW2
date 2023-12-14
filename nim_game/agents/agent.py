from random import choice, randint

from nim_game.common.enumerations import AgentLevels
from nim_game.common.models import NimStateChange


class Agent:
    """
    В этом классе реализованы стратегии игры для уровней сложности
    """

    _level: AgentLevels         # уровень сложности

    def __init__(self, level: str) -> None:
        level = AgentLevels(level)

        if not (level == AgentLevels.EASY or level == AgentLevels.HARD
                or level == AgentLevels.NORMAL):
            raise ValueError(
                "Not expected level: {level}"
            )

        self._level = level

    def _make_step_easy(self, state_curr: list[int]):
        choice_heap_id = choice(
            [heap for heap in range(len(state_curr)) if state_curr[heap] != 0])
        choice_decrease = randint(1, state_curr[choice_heap_id])

        return NimStateChange(
            choice_heap_id,
            choice_decrease
        )

    def _make_step_hard(self, state_curr: list[int]):
        decrease_c = 0
        for heap in range(len(state_curr)):
            nim_sum = -1

            if state_curr[heap] != 0:
                for decrease in range(1, state_curr[heap] + 1):
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
            heap_c = choice([heap for heap in range(len(state_curr))
                            if state_curr[heap] != 0])
            decrease_c = randint(1, state_curr[heap])

        return NimStateChange(
            heap_c,
            decrease_c
        )

    def make_step(self, state_curr: list[int]) -> NimStateChange:
        """
        Сделать шаг, соотвутствующий уровню сложности

        :param state_curr: список целых чисел - состояние кучек
        :return: стуктуру NimStateChange - описание хода
        """
        if self._level == AgentLevels.EASY:
            return self._make_step_easy(state_curr)

        elif self._level == AgentLevels.HARD:
            return self._make_step_hard(state_curr)

        elif self._level == AgentLevels.NORMAL:
            return choice([self._make_step_easy(state_curr),
                           self._make_step_hard(state_curr)])
