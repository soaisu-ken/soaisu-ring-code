
from sympy import symbols, expand
import sys

def parse_input_set(prompt):
    """
    Prompts the user for input and converts it into a list of integers.
    """
    while True:
        try:
            user_input = input(prompt)
            # Remove full-width spaces, half-width spaces, and curly braces
            cleaned_input = user_input.strip('{} ').replace(' ', '').strip()
            if not cleaned_input:
                print("Input is empty. Please try again.")
                continue
            
            s_list = list(map(int, cleaned_input.split(',')))
            
            if len(s_list) != 6:
                print("The number of elements is not 6. Please try again.")
            else:
                return s_list
        except ValueError:
            print("Invalid input. Please enter integers separated by commas. e.g., 5,14,34,45,36,16")

def cyclic_prod_sum_expr(arr, m_power):
    """
    Calculates the m-th cyclic product sum for a list of SymPy expressions.
    """
    expr = 0
    N = len(arr)
    for j in range(N):
        term = 1
        for k in range(m_power):
            term *= arr[(j + k) % N]
        expr += term
    return expr

def verify_all_conditions_with_nm(s1_base, s2_base):
    """
    Algebraically verifies all soaisu ring conditions with n and m expressions.
    """
    n, m = symbols('n m')

    # Define the new expressions for S1 and S2 based on the input
    s1_expr = [val * n + m for val in s1_base]
    s2_expr = [val * n + m for val in s2_base]

    print(f"\n--- Generated S1 expressions: {[str(e) for e in s1_expr]}")
    print(f"--- Generated S2 expressions: {[str(e) for e in s2_expr]}")
    
    overall_match = True

    # ================== 1-5th Power Sum Verification ==================
    print("\n" + "="*50)
    print("\n--- 1-5th Power Sum Verification ---")
    for p in range(1, 6):
        s1_power_sum = sum(val**p for val in s1_expr)
        s2_power_sum = sum(val**p for val in s2_expr)
        expanded_s1 = expand(s1_power_sum)
        expanded_s2 = expand(s2_power_sum)
        
        print(f"\n[{p}th Power Sum]")
        print(f"S1: {expanded_s1}")
        print(f"S2: {expanded_s2}")

        if expanded_s1 != expanded_s2:
            print("❌ The polynomials do not match.")
            overall_match = False
        else:
            print("✅ The polynomials match.")

    # ================== 1-5th Cyclic Product Sum Verification ==================
    print("\n" + "="*50)
    print("\n--- 1-5th Cyclic Product Sum Verification ---")
    for p in range(1, 6):
        c1 = cyclic_prod_sum_expr(s1_expr, p)
        c2 = cyclic_prod_sum_expr(s2_expr, p)
        expanded_c1 = expand(c1)
        expanded_c2 = expand(c2)

        print(f"\n[{p}th Cyclic Product Sum]")
        print(f"S1: {expanded_c1}")
        print(f"S2: {expanded_c2}")
        
        if expanded_c1 != expanded_c2:
            print("❌ The polynomials do not match.")
            overall_match = False
        else:
            print("✅ The polynomials match.")

    # ================== Diagonal Product Sum Verification ==================
    print("\n" + "="*50)
    print("\n--- Diagonal Product Sum Verification ---")
    diag_sum1 = s1_expr[0]*s1_expr[3] + s1_expr[1]*s1_expr[4] + s1_expr[2]*s1_expr[5]
    diag_sum2 = s2_expr[0]*s2_expr[3] + s2_expr[1]*s2_expr[4] + s2_expr[2]*s2_expr[5]
    expanded_diag1 = expand(diag_sum1)
    expanded_diag2 = expand(diag_sum2)

    print(f"\nDiagonal Product Sum Expression")
    print(f"S1: {expanded_diag1}")
    print(f"S2: {expanded_diag2}")

    if expanded_diag1 != expanded_diag2:
        print("❌ The polynomials do not match.")
        overall_match = False
    else:
        print("✅ The polynomials match.")

    # ================== Regular Triangle Product Sum Verification ==================
    print("\n" + "="*50)
    print("\n--- Regular Triangle Product Sum Verification ---")
    tri_sum1 = s1_expr[0]*s1_expr[2]*s1_expr[4] + s1_expr[1]*s1_expr[3]*s1_expr[5]
    tri_sum2 = s2_expr[0]*s2_expr[2]*s2_expr[4] + s2_expr[1]*s2_expr[3]*s2_expr[5]
    expanded_tri1 = expand(tri_sum1)
    expanded_tri2 = expand(tri_sum2)

    print(f"\nRegular Triangle Product Sum Expression")
    print(f"S1: {expanded_tri1}")
    print(f"S2: {expanded_tri2}")
    
    if expanded_tri1 != expanded_tri2:
        print("❌ The polynomials do not match.")
        overall_match = False
    else:
        print("✅ The polynomials match.")
    
    # ================== Embedded 3-3 Soaisu Ring Verification ==================
    print("\n" + "="*50)
    print("\n--- Embedded 3-3 Soaisu Ring Verification ---")
    s1_tri_expr = [s1_expr[0], s1_expr[2], s1_expr[4]]
    s2_tri_expr = [s2_expr[1], s2_expr[3], s2_expr[5]]
    
    # Power Sum Verification
    for p in range(1, 3):
        s1_tri_power_sum = sum(val**p for val in s1_tri_expr)
        s2_tri_power_sum = sum(val**p for val in s2_tri_expr)
        expanded_s1_tri = expand(s1_tri_power_sum)
        expanded_s2_tri = expand(s2_tri_power_sum)

        print(f"\n[Embedded 3-3 Soaisu {p}th Power Sum]")
        print(f"S1: {expanded_s1_tri}")
        print(f"S2: {expanded_s2_tri}")

        if expanded_s1_tri != expanded_s2_tri:
            print("❌ The polynomials do not match.")
            overall_match = False
        else:
            print("✅ The polynomials match.")
    
    # Cyclic Product Sum Verification
    for p in range(1, 3):
        c1_tri = cyclic_prod_sum_expr(s1_tri_expr, p)
        c2_tri = cyclic_prod_sum_expr(s2_tri_expr, p)
        expanded_c1_tri = expand(c1_tri)
        expanded_c2_tri = expand(c2_tri)
        
        print(f"\n[Embedded 3-3 Soaisu Ring {p}th Cyclic Product Sum]")
        print(f"S1: {expanded_c1_tri}")
        print(f"S2: {expanded_c2_tri}")

        if expanded_c1_tri != expanded_c2_tri:
            print("❌ The polynomials do not match.")
            overall_match = False
        else:
            print("✅ The polynomials match.")
            
    return overall_match


if __name__ == "__main__":
    print("--- 6-6 Soaisu❤︎❤︎❤︎❤︎❤︎ Ring Polynomial Verification Program ---")
    print("Please enter the original 6-6 soaisu heart heart heart heart heart ring s1 and s2.")

    # 1. Prompt the user for S1 and S2 input
    s1_input = parse_input_set("Enter the 6 elements for S1, separated by commas. e.g., 5,14,34,45,36,16\nS1 = ")
    s2_input = parse_input_set("Enter the 6 elements for S2, separated by commas. e.g., 6,21,40,44,29,10\nS2 = ")
    
    print(f"Entered S1: {s1_input}")
    print(f"Entered S2: {s2_input}")

    # Verify all conditions
    result = verify_all_conditions_with_nm(s1_input, s2_input)

    # Display the final result
    print("\n" + "="*50)
    if result:
        print("🎉🎉🎉 Conclusion: The 6-6 soaisu❤︎❤︎❤︎❤︎❤︎ ring is maintained for all m and n.")
    else:
        print("💔💔💔 Conclusion: The ring structure is not maintained because some conditions do not match for all values of n and m.")
    print("="*50)




