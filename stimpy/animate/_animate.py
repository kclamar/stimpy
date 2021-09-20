from functools import cached_property
from typing import Callable, List, Union

import numpy as np

from ._func import Func


class Animate(Func):
    """Class for specifying how an attribute changes with time.

    :param values: Sequence of values.
    :param dur: Durations. The i-th element is the time needed to change
    from the i-th value to the next value.
    """

    def __init__(
        self,
        values: list,
        dur: Union[float, List[float]],
        calc_mode: str = "linear",
        mode: str = "nearest",
        func: Callable = None,
    ):
        self.__values = values
        if isinstance(dur, (float, int)):
            self.__dur = [dur, 0]
        else:
            self.__dur = dur
        assert len(self.__values) == len(self.__dur)
        self.__calc_mode = calc_mode.lower()
        self.__mode = mode
        self.__func = (lambda x: x) if func is None else func

    def __call__(self, t: float):
        if self.__mode == "wrap":
            t_cycle = t % self._dur_sum
        elif self.__mode == "nearest":
            t_cycle = np.clip(t, 0, self._dur_sum)
        else:
            raise NotImplementedError
        i = min(
            len(self.__dur) - 1, int(np.digitize(t_cycle, self._dur_cumsum))
        )
        t_state = t_cycle - sum(self.__dur[:i])
        f = 0 if self.__dur[i] == 0 else t_state / self.__dur[i]
        return self.__func(self._interpolate(i, f))

    @cached_property
    def _dur_cumsum(self) -> np.ndarray:
        return np.cumsum(self.__dur)

    @cached_property
    def _dur_sum(self) -> float:
        return sum(self.__dur)

    @cached_property
    def _n_states(self) -> int:
        return len(self.__values)

    def _interpolate(self, i: int, f: float):
        if self.__calc_mode == "linear":
            return (
                self.__values[i]
                + (
                    np.array(self.__values[(i + 1) % self._n_states])
                    - self.__values[i]
                )
                * f
            )
        return self.__values[i]
