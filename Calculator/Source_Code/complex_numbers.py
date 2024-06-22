def add_complex(real_part1, imaginary_part1, real_part2, imaginary_part2):
    real_result = real_part1 + real_part2
    imaginary_result = imaginary_part1 + imaginary_part2
    return real_result, imaginary_result

def subtract_complex(real_part1, imaginary_part1, real_part2, imaginary_part2):
    real_result = real_part1 - real_part2
    imaginary_result = imaginary_part1 - imaginary_part2
    return real_result, imaginary_result

def multiply_complex(real_part1, imaginary_part1, real_part2, imaginary_part2):
    real_result = real_part1 * real_part2 - imaginary_part1 * imaginary_part2
    imaginary_result = real_part1 * imaginary_part2 + imaginary_part1 * real_part2
    return real_result, imaginary_result

def divide_complex(real_part1, imaginary_part1, real_part2, imaginary_part2):
    denominator = real_part2**2 + imaginary_part2**2
    if denominator == 0:
        return None  # Handle division by zero case appropriately
    real_result = (real_part1 * real_part2 + imaginary_part1 * imaginary_part2) / denominator
    imaginary_result = (imaginary_part1 * real_part2 - real_part1 * imaginary_part2) / denominator
    return real_result, imaginary_result
