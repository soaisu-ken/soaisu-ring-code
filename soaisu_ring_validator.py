
import itertools
import math

# --- Helper Functions ---

def calculate_power_sums(s_list, max_power):
    """
    Calculates power sums for a given list up to max_power.
    """
    sums = [0] * (max_power + 1)
    for x in s_list:
        for p in range(max_power + 1):
            sums[p] += x**p
    return tuple(sums)

def cyclic_product_sum(sequence, m):
    """
    Calculates the m-th cyclic product sum.
    :param sequence: A sequence of numbers (list or tuple).
    :param m: The degree of the product.
    :return: The cyclic product sum.
    """
    n = len(sequence)
    if n == 0:
        return 0
    total_sum = 0
    if m == 0:
        return n
    for j in range(n):
        product = 1
        for k in range(m):
            index = (j + k) % n
            product *= sequence[index]
        total_sum += product
    return total_sum

def diagonal_product_sum(sequence):
    """
    Calculates the diagonal product sum for n=6.
    P^diag(S) = a1*a4 + a2*a5 + a3*a6
    """
    if len(sequence) != 6:
        return None
    return sequence[0]*sequence[3] + sequence[1]*sequence[4] + sequence[2]*sequence[5]

def regular_triangle_product_sum(sequence):
    """
    Calculates the regular triangle product sum for n=6.
    P^(3)(S) = a1*a3*a5 + a2*a4*a6
    """
    if len(sequence) != 6:
        return None
    return sequence[0]*sequence[2]*sequence[4] + sequence[1]*sequence[3]*sequence[5]

def get_unique_cyclic_and_reversed_arrangements(permutations_list):
    """
    Filters a list of permutations to get only unique arrangements,
    considering cyclic and reversed orderings as equivalent.
    """
    unique_arrangements = set()
    for p in permutations_list:
        p_list = list(p)
        equivalent_arrangements = []
        for i in range(len(p_list)):
            shifted = tuple(p_list[i:] + p_list[:i])
            equivalent_arrangements.append(shifted)
        p_list_rev = p_list[::-1]
        for i in range(len(p_list_rev)):
            shifted_rev = tuple(p_list_rev[i:] + p_list_rev[:i])
            equivalent_arrangements.append(shifted_rev)
        representative = min(equivalent_arrangements)
        unique_arrangements.add(representative)
    return list(unique_arrangements)

def parse_input_set(prompt):
    """
    Prompts user for input and parses it into a set of integers.
    """
    while True:
        try:
            user_input = input(prompt)
            cleaned_input = user_input.strip('{} ').replace(' ', ',').strip()
            if not cleaned_input:
                print("Input is empty. Please try again.")
                continue
            
            s_set = set(map(int, cleaned_input.split(',')))
            
            if len(s_set) != 6:
                print("The number of elements is not 6. Please try again.")
            else:
                return s_set
        except ValueError:
            print("Invalid input. Please enter integers separated by commas or spaces. e.g., 5, 14, 16, 34, 36, 45")

# --- Main Program Logic ---
def main_program():
    print("Starting the 6-6 soaisu heart heart heart heart heart ring verification program.")

    # Step 1: Get user input for S1 and S2
    s1_set = parse_input_set("Enter six distinct integers for set S1, separated by commas or spaces. e.g., 5,14,16,34,36,45\nS1 = ")
    s2_set = parse_input_set("Enter six distinct integers for set S2, separated by commas or spaces. e.g., 6,10,21,29,40,44\nS2 = ")
    
    s1_list = sorted(list(s1_set))
    s2_list = sorted(list(s2_set))

    print(f"\nS1 entered: {s1_list}")
    print(f"S2 entered: {s2_list}")

    # Check 6-6 soaisu (PTE ideal solution)
    s1_power_sums = calculate_power_sums(s1_list, 5)
    s2_power_sums = calculate_power_sums(s2_list, 5)
    
    if s1_power_sums != s2_power_sums:
        print("\n--- Verification Result ---")
        print("S1 and S2 do not have matching 1st to 5th power sums. They are not a 6-6 soaisu.")
        return

    print(f"\n✅ Step 1 passed: Power sums from 1st to 5th degree match. This is a 6-6 soaisu.")
    print(f"  Power Sums: 1st: {s1_power_sums[1]}, 2nd: {s1_power_sums[2]}, 3rd: {s1_power_sums[3]}, 4th: {s1_power_sums[4]}, 5th: {s1_power_sums[5]}")
    
    # Steps 2, 3, 4: Find arrangements with matching product sums
    all_s1_permutations = list(itertools.permutations(s1_list))
    all_s2_permutations = list(itertools.permutations(s2_list))
    
    unique_s1_arrangements = get_unique_cyclic_and_reversed_arrangements(all_s1_permutations)
    unique_s2_arrangements = get_unique_cyclic_and_reversed_arrangements(all_s2_permutations)
    
    soaisu_ring_candidates = []
    
    print("\n--- Running Steps 2, 3, and 4: Searching for arrangements... ---")

    for perm1 in unique_s1_arrangements:
        for perm2 in unique_s2_arrangements:
            
            # Step 2: Check 1-5 cyclic product sums
            cyclic_sums_match = True
            cyclic_sums1 = [cyclic_product_sum(perm1, m) for m in range(1, 6)]
            cyclic_sums2 = [cyclic_product_sum(perm2, m) for m in range(1, 6)]
            
            if cyclic_sums1 != cyclic_sums2:
                cyclic_sums_match = False
            
            if cyclic_sums_match:
                # Step 3: Check Diagonal Product Sum
                diag_sum1 = diagonal_product_sum(perm1)
                diag_sum2 = diagonal_product_sum(perm2)
                
                if diag_sum1 == diag_sum2:
                    # Step 4: Check Regular Triangle Product Sum
                    tri_sum1 = regular_triangle_product_sum(perm1)
                    tri_sum2 = regular_triangle_product_sum(perm2)
                    
                    if tri_sum1 == tri_sum2:
                        soaisu_ring_candidates.append((perm1, perm2))

    if not soaisu_ring_candidates:
        print("❌ Steps 2-4 failed: No arrangements with matching cyclic, diagonal, and triangle product sums were found.")
        return
    
    print(f"\n✅ Steps 2-4 passed: {len(soaisu_ring_candidates)} matching arrangements found.")
    
    # Steps 5 & 6: Check sub-sets for 3-3 soaisu and 3-3 soaisu Ring
    final_soaisu_rings = []
    
    for perm1, perm2 in soaisu_ring_candidates:
        print(f"\n--- Verifying candidate arrangement: S1={perm1}, S2={perm2} ---")
        
        # Define sub-sets (triangles)
        s1_triangle1 = [perm1[0], perm1[2], perm1[4]] # a1, a3, a5
        s1_triangle2 = [perm1[1], perm1[3], perm1[5]] # a2, a4, a6
        s2_triangle1 = [perm2[0], perm2[2], perm2[4]]
        s2_triangle2 = [perm2[1], perm2[3], perm2[5]]
        
        # Step 5: Check for 3-3 soaisu (power sums up to degree 2)
        s1_tri_sums = calculate_power_sums(s1_triangle1, 2)
        s2_tri_sums = calculate_power_sums(s2_triangle2, 2)
        if s1_tri_sums != s2_tri_sums:
            print("❌ Step 5 failed: The sets of inscribed triangle vertices do not form a 3-3 soaisu.")
            continue
        
        print(f"✅ Step 5 passed: The inscribed triangle vertices form a 3-3 soaisu.")
        print(f"  Power Sums: 1st: {s1_tri_sums[1]}, 2nd: {s1_tri_sums[2]}")

        # Step 6: Check for 3-3 soaisu ring (cyclic product sums up to degree 2)
        s1_tri_cyclic_sums = [cyclic_product_sum(s1_triangle1, m) for m in range(1, 3)]
        s2_tri_cyclic_sums = [cyclic_product_sum(s2_triangle2, m) for m in range(1, 3)]
        
        if s1_tri_cyclic_sums != s2_tri_cyclic_sums:
            print("❌ Step 6 failed: The 3-3 soaisu ring condition (matching 1st and 2nd cyclic product sums) is not met.")
            continue
        
        print(f"✅ Step 6 passed: The 3-3 soaisu ring condition is met.")
        print(f"  Cyclic Product Sums: 1st: {s1_tri_cyclic_sums[0]}, 2nd: {s1_tri_cyclic_sums[1]}")
        
        final_soaisu_rings.append((perm1, perm2))

    # Final Result
    if not final_soaisu_rings:
        print("\n--- Final Result ---")
        print("No arrangements satisfied all conditions for a 6-6 soaisu ring.")
    else:
        print("\n--- Final Result ---")
        print("🎉🎉🎉 All conditions were met! A 6-6 soaisu heart heart heart heart heart ring was found! 🎉🎉🎉")
        for i, (p1, p2) in enumerate(final_soaisu_rings):
            print(f"\n[Pair {i+1}]")
            print(f"S1 arrangement: {p1}")
            print(f"S2 arrangement: {p2}")
            
            # Print specific values for each check
            cyclic_sums1 = [cyclic_product_sum(p1, m) for m in range(1, 6)]
            print(f"  Cyclic Product Sums (1st to 5th): {cyclic_sums1}")
            print(f"  Diagonal Product Sum: {diagonal_product_sum(p1)}")
            print(f"  Regular Triangle Product Sum: {regular_triangle_product_sum(p1)}")
            
            s1_tri1 = [p1[0], p1[2], p1[4]]
            s2_tri1 = [p2[0], p2[2], p2[4]]
            print(f"  Embedded 3-3 soaisu heart heart ring (S1): {s1_tri1}")
            print(f"  Embedded 3-3 soaisu heart heart ring (S2): {s2_tri1}")
            
            # Print specific values for the embedded 3-3 ring
            s1_tri_sums = calculate_power_sums(s1_tri1, 2)
            s2_tri_sums = calculate_power_sums(s2_tri1, 2)
            print(f"    Embedded 3-3 soaisu power sums: 1st: {s1_tri_sums[1]}, 2nd: {s1_tri_sums[2]}")
            
            s1_tri_cyclic_sums = [cyclic_product_sum(s1_tri1, m) for m in range(1, 3)]
            s2_tri_cyclic_sums = [cyclic_product_sum(s2_tri1, m) for m in range(1, 3)]
            print(f"    Embedded 3-3 soaisu cyclic sums: 1st: {s1_tri_cyclic_sums[0]}, 2nd: {s1_tri_cyclic_sums[1]}")
            print("-" * 30)


if __name__ == "__main__":
    main_program()
