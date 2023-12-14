from random import randint

from nim_game.common.models import NimStateChange


STONE_AMOUNT_MIN = 1        # минимальное начальное число камней в кучке
STONE_AMOUNT_MAX = 10       # максимальное начальное число камней в кучке


class EnvironmentNim:
    """
    Класс для хранения и взаимодействия с кучками
    """

    _heaps: list[int]       # кучки

    def __init__(self, heaps_amount: int) -> None:
        heaps_amount = int(heaps_amount)
        heaps = []

        if 2 > heaps_amount or 10 < heaps_amount:
            raise ValueError(
                "Unexpected heaps amount value: {heaps_amount}"
            )

        for heap in range(heaps_amount):
            stones = randint(STONE_AMOUNT_MIN, STONE_AMOUNT_MAX)
            heaps.append(stones)

        self._heaps = heaps[:]

    def get_state(self) -> list[int]:
        """
        Получение текущего состояния кучек

        :return: копия списка с кучек
        """
        heaps_return = self._heaps[:]

        return heaps_return

    def change_state(self, state_change: NimStateChange) -> None:
        """
        Изменения текущего состояния кучек

        :param state_change: структура описывающая изменение состояния
        """
        if state_change.heap_id < 1\
                or state_change.heap_id - 1 >= len(self._heaps):
            raise ValueError(
                "Unexpected heap id: {state_change.heap_id}"
            )

        if state_change.decrease < 1\
                or state_change.decrease >\
                self._heaps[state_change.heap_id - 1]:
            raise ValueError(
                "Unexpected decrease: {state_change.decrease}"
            )

        self._heaps[state_change.heap_id - 1] -= state_change.decrease
