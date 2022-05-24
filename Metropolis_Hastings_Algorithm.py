from typing import Callable
import numpy as np
import matplotlib.pyplot as plt

def metropolis_hastings(
    f: Callable, x_0: float = 0.0, n_samples: int = 10000
) -> np.ndarray:
    """Implements the metropolis-hastings algorithm with a normal distribution as proposal function.

    Args:
        f (Callable): An arbitrary probability density function
            that is used to calculate the acceptance ratio alpha=f(x_next)/f(x_t).
            f has to accept a single parameter x and return the function value for x.
        x_0 (float, optional): The first observation to start from.
        n_samples (int, optional): Number of samples to be drawn. Defaults to 10000.

    Returns:
        (np.ndarray): Drawn samples from the target distribution.
    """

    if n_samples <= 0:
        raise ValueError("n_samples needst to be positive!")

    samples_mc = [x_0]
    for i in range(n_samples):
        x_t = samples_mc[-1]
        x_next = np.random.normal(loc=x_t, scale=1)
        prob = min(1, f(x_next) / f(x_t))
        if np.random.uniform(0, 1) <= prob:
            samples_mc.append(x_next)
        else:
            samples_mc.append(x_t)
    result = np.array(samples_mc[1:])
    return result

#for testing:
def norm_dist(x, mean=0, std=1):
    """Gaussian normal probability distribution."""
    return np.exp(-0.5 * (x - mean) ** 2 / std ** 2)

samples = metropolis_hastings(f=lambda x: norm_dist(x, mean=0, std=1), x_0=-1, n_samples=10000)
print(samples.mean(), samples.std())
print(samples)
print(len(samples))

plt.hist(samples, bins=20)
plt.show()

