def thomas_algorithm(a, b, c, d):
    """Solves a tridiagonal matrix system (Ax = d) using the Thomas Algorithm."""
    n = len(d)
    c_prime = [0.0] * (n - 1)
    d_prime = [0.0] * n
    x = [0.0] * n
    
    # Forward elimination phase
    c_prime[0] = c[0] / b[0]
    d_prime[0] = d[0] / b[0]
    
    for i in range(1, n):
        denominator = b[i] - (a[i] * c_prime[i - 1])
        if i < n - 1:
            c_prime[i] = c[i] / denominator
        d_prime[i] = (d[i] - (a[i] * d_prime[i - 1])) / denominator

    # Backward substitution phase
    x[n - 1] = d_prime[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = d_prime[i] - (c_prime[i] * x[i + 1])
        
    return x


def get_user_input():
    print("=== Tridiagonal System Solver (Thomas Algorithm) ===")
    
    # 1. Get system size
    while True:
        try:
            n = int(input("Enter the number of equations (matrix size N): "))
            if n < 2:
                print("System size must be at least 2.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Initialize vectors
    a = [0.0] * n  # Lower diagonal (a[0] stays 0.0)
    b = [0.0] * n  # Main diagonal
    c = [0.0] * n  # Upper diagonal (c[-1] stays 0.0)
    d = [0.0] * n  # Right-hand side vector

    print("\n--- Enter Coefficients Row by Row ---")
    print("Format for Row 1:   [Main_B] [Upper_C] = [D1]")
    print("Format for Middle:  [Lower_A] [Main_B] [Upper_C] = [D2]")
    print("Format for ......:  ............................ = [Dn-1]")
    print("Format for Row N:   [Lower_A] [Main_B] = [Dn]")
    print("-" * 50)

    # 2. Collect row values dynamically
    for i in range(n):
        while True:
            try:
                row_input = input(f"Row {i + 1}: ").strip()
                
                # Split by equals sign to separate LHS coefficients from RHS value
                if "=" not in row_input:
                    print("Error: Missing '=' to separate the RHS value. Example: 2 1 = 5")
                    continue
                
                lhs_str, rhs_str = row_input.split("=")
                lhs_vals = [float(val) for val in lhs_str.split()]
                d[i] = float(rhs_str.strip())

                # Validate structural counts based on row index
                if i == 0:  # First row: needs b[0] and c[0]
                    if len(lhs_vals) != 2:
                        print("First row must have exactly 2 LHS values: [b1 c1]")
                        continue
                    b[0], c[0] = lhs_vals
                    
                elif i == n - 1:  # Last row: needs a[n-1] and b[n-1]
                    if len(lhs_vals) != 2:
                        print("Last row must have exactly 2 LHS values: [aN bN]")
                        continue
                    a[i], b[i] = lhs_vals
                    
                else:  # Intermediate rows: needs a[i], b[i], and c[i]
                    if len(lhs_vals) != 3:
                        print(f"Row {i + 1} must have exactly 3 LHS values: [a{i+1} b{i+1} c{i+1}]")
                        continue
                    a[i], b[i], c[i] = lhs_vals
                
                break # Input accepted, move to next row
            except ValueError:
                print("Invalid numerical input. Please use spaces to separate numbers.")

    return a, b, c, d


# ==========================================
# Main Execution Loop
# ==========================================
if __name__ == "__main__":
    # Get values from console terminal interaction
    diag_a, diag_b, diag_c, vector_d = get_user_input()
    
    print("\nProcessing vectors using Thomas Algorithm...")
    try:
        solution = thomas_algorithm(diag_a, diag_b, diag_c, vector_d)
        
        print("\n=== Calculation Successful ===")
        for index, value in enumerate(solution):
            print(f"x{index + 1} = {value:.4f}")
            
    except ZeroDivisionError:
        print("\nExecution Error: Division by zero encountered. The matrix might not be diagonally dominant.")