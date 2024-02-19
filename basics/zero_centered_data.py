import numpy as np
import matplotlib.pyplot as plt
"""
This is a simple example of explaining why zero-centered data is important.
Three approaches are implemented here:
Approach 1: Zero-Centered
- Result: model converges to the expected value
Approach 2: Non-Zero-Centered
- Result: model cannot converge due to exploding gradient
Approach 3: Non-Zero-Centered, but normalized
- Result: model cannot converge due to exploding gradient
"""

def func(a, b, c, d, x):
    return a * x**3 + b * x**2 + c * x + d

def ori_func(x):
    return x**3 + 3*x**2 + 2*x + 10

def gradient_descent(xs, ys, epochs, learning_rate=0.0001):
    a, b, c, d = np.random.random(4)
    for epoch in range(epochs):
        grad = np.zeros(4)
        for i in range(len(xs)):
            difference = ys[i] - func(a, b, c, d, xs[i])
            # error = (ys[i] - func(a, b, c, d, xs[i])) ** 2
            # d_error = -2 * difference
            grad[0] += -2 * difference * xs[i]**3
            grad[1] += -2 * difference * xs[i]**2
            grad[2] += -2 * difference * xs[i]
            grad[3] += -2 * difference
        a -= learning_rate * grad[0]
        b -= learning_rate * grad[1]
        c -= learning_rate * grad[2]
        d -= learning_rate * grad[3]
    return a, b, c, d

# Generate data
np.random.seed(0)
ori_xs = np.linspace(-10, 10, 1000) + np.random.normal(2, 5, 1000)
ori_ys = ori_func(ori_xs)

# APPROACH 1: Zero-Centered
# Normalize data
mean_xs, std_xs = np.mean(ori_xs), np.std(ori_xs)
xs = (ori_xs - mean_xs) / std_xs
print(f"mean data: {np.mean(xs)}, std data: {np.std(xs)}")

# Perform gradient descent
a, b, c, d = gradient_descent(xs, ori_func(xs), epochs=1000, learning_rate=0.00001)
expected_a, expected_b, expected_c, expected_d = 1, 3, 2, 10
print("a: {:.2f}, b: {:.2f}, c: {:.2f}, d: {:.2f}".format(a, b, c, d))
print("expected_a: {:.2f}, expected_b: {:.2f}, expected_c: {:.2f}, expected_d: {:.2f}".format(expected_a, expected_b, expected_c, expected_d))

# Plot results
plt.figure(num="Zero-Centered Data")
plt.scatter(ori_xs, func(expected_a, expected_b, expected_c, expected_d, ori_xs), label='Original Data')
plt.scatter(ori_xs, func(a, b, c, d, ori_xs), color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
# APPROACH 2: Non-Zero-Centered

xs = (ori_xs + ori_xs.min())
print(f"mean data: {np.mean(xs)}, std data: {np.std(xs)}")

# Perform gradient descent
a, b, c, d = gradient_descent(xs, ori_func(xs), epochs=100)
expected_a, expected_b, expected_c, expected_d = 1, 3, 2, 10
print("a: {:.2f}, b: {:.2f}, c: {:.2f}, d: {:.2f}".format(a, b, c, d))
print("expected_a: {:.2f}, expected_b: {:.2f}, expected_c: {:.2f}, expected_d: {:.2f}".format(expected_a, expected_b, expected_c, expected_d))

# Plot results
plt.figure(num="Non-Zero-Centered Data")
plt.scatter(ori_xs, func(expected_a, expected_b, expected_c, expected_d, ori_xs), label='Original Data')
plt.scatter(ori_xs, func(a, b, c, d, ori_xs), color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# APPROACH 3: Non-Zero-Centered, but normalized

xs = ori_xs - mean_xs
print(f"mean data: {np.mean(xs)}, std data: {np.std(xs)}")

# Perform gradient descent
a, b, c, d = gradient_descent(xs, ori_func(xs), epochs=100)
expected_a, expected_b, expected_c, expected_d = 1, 3, 2, 10
print("a: {:.2f}, b: {:.2f}, c: {:.2f}, d: {:.2f}".format(a, b, c, d))
print("expected_a: {:.2f}, expected_b: {:.2f}, expected_c: {:.2f}, expected_d: {:.2f}".format(expected_a, expected_b, expected_c, expected_d))

# Plot results
plt.figure(num="Non-Zero-Centered, but normalized")
plt.scatter(ori_xs, func(expected_a, expected_b, expected_c, expected_d, ori_xs), label='Original Data')
plt.scatter(ori_xs, func(a, b, c, d, ori_xs), color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.show()
