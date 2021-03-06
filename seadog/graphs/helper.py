import math
import numpy as np

class Helper:
    def get_figsize(size):
        if size:
            x = Helper.px_to_inches(size[0], 8)
            y = Helper.px_to_inches(size[1], 6)
            return (x,y)
        return (8,6)

    def px_to_inches(px, minimum):
        inches = round(px / 100)
        return max(inches, minimum)

    def get_bin_edges(series, bucket_size):
        min = series.min() - bucket_size * 0.5
        max = series.max() + bucket_size * 1.5
        return np.arange(min, max, bucket_size)

    def get_bucket_size(series):
        # TODO: this is not ideal
        range = series.max() - series.min()
        if range > 100:
            power = math.ceil(math.log10(range)) - 2
            return math.pow(10, power)
        
        return math.ceil(range / 20)

    def get_log_ticks(max):
        pattern = [1, 2, 5]
        ticks = []

        index = 0
        while True:
            magnitude, index_pattern = divmod(index, len(pattern))
            tick = pattern[index_pattern] * math.pow(10, magnitude)
            ticks.append(tick)
            if (tick > max):
                break
            index = index + 1

        return ticks

    def log_trans(x, apply = True, inverse = False):
        if not apply:
            return x

        if not inverse:
            return np.log10(x)
        else:
            return np.power(10, x)