

import itertools
import math
import time

# --- Helper Functions ---

def calculate_power_sums(s_set, max_power):
    """
    Calculates power sums for a given set up to max_power.
    """
    sums = [0] * (max_power + 1)
    for x in s_set:
        for p in range(max_power + 1):
            sums[p] += x**p
    return tuple(sums) # Use tuple for hashability

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
    
    if m == 0: # As per manuscript, empty product is 1, so sum is n
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
    Calculates the diagonal product sum for n=6 (x=2, d=3).
    P^diag(S) = a1*a4 + a2*a5 + a3*a6
    """
    if len(sequence) != 6:
        raise ValueError("Diagonal product sum is defined for sequence length 6.")
    return sequence[0]*sequence[3] + sequence[1]*sequence[4] + sequence[2]*sequence[5]

def regular_triangle_product_sum(sequence):
    """
    Calculates the regular triangle product sum for n=6 (x=3, d=2).
    P^(3)(S) = a1*a3*a5 + a2*a4*a6
    """
    if len(sequence) != 6:
        raise ValueError("Regular triangle product sum is defined for sequence length 6.")
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
        
        # Add cyclic shifts
        for i in range(len(p_list)):
            shifted = tuple(p_list[i:] + p_list[:i])
            equivalent_arrangements.append(shifted)
            
        # Add reversed cyclic shifts
        p_list_rev = p_list[::-1]
        for i in range(len(p_list_rev)):
            shifted_rev = tuple(p_list_rev[i:] + p_list_rev[:i])
            equivalent_arrangements.append(shifted_rev)
            
        # Find the lexicographically smallest arrangement to represent the group
        representative = min(equivalent_arrangements)
        unique_arrangements.add(representative)
        
    return list(unique_arrangements)

# --- Main Program Logic ---

def find_soaisu_rings_in_range(n_limit):
    """
    Searches for 6-6 SOAISU heart heart heart heart heart ring pairs within the range 1 to n_limit.
    """
    print(f"--- Step 1: Searching for 6-6 SOAISU (PTE Ideal Solutions) within 1 to {n_limit} ---")
    print("WARNING: This step can be extremely time-consuming for large n_limit due to combinatorial explosion.")
    print("For n_limit > 25, it might take hours or days.")
    
    all_numbers = list(range(1, n_limit + 1))
    soaisu_solutions = []
    
    # Generate all combinations of 6 numbers for S1
    s1_combinations = list(itertools.combinations(all_numbers, 6))
    total_s1_comb = len(s1_combinations)
    print(f"Total S1 combinations to check: {total_s1_comb}")

    start_time_step1 = time.time()
    s1_count = 0
    
    for s1_candidate_tuple in s1_combinations:
        s1_count += 1
        s1_candidate = set(s1_candidate_tuple)
        s1_power_sums = calculate_power_sums(s1_candidate, 5)

        # Optimization: Only consider S2 combinations from numbers not in S1
        remaining_numbers = [x for x in all_numbers if x not in s1_candidate]
        if len(remaining_numbers) < 6:
            continue # Not enough numbers left for S2

        s2_combinations = list(itertools.combinations(remaining_numbers, 6))
        
        for s2_candidate_tuple in s2_combinations:
            s2_candidate = set(s2_candidate_tuple)
            s2_power_sums = calculate_power_sums(s2_candidate, 5)

            # Check if power sums match for k=0 to 5
            if s1_power_sums == s2_power_sums:
                soaisu_solutions.append((s1_candidate, s2_candidate))
                print(f"  Found 6-6 SOAISU: S1={s1_candidate}, S2={s2_candidate}")
        
        if s1_count % 1000 == 0:
            elapsed_time = time.time() - start_time_step1
            print(f"  Processed {s1_count}/{total_s1_comb} S1 combinations. Elapsed: {elapsed_time:.2f}s")

    if not soaisu_solutions:
        print("  No 6-6 SOAISU found within the specified range.")
        return

    print(f"\n--- Step 1 Complete: Found {len(soaisu_solutions)} 6-6 SOAISU pairs ---")

    print("\n--- Step 2, 3, 4: Checking for SOAISU Rings ---")
    soaisu_ring_pairs = []

    for s1_set, s2_set in soaisu_solutions:
        print(f"\nProcessing SOAISU pair: S1={s1_set}, S2={s2_set}")
        
        # Step 2: Find arrangements with matching cyclic product sums (1st to 5th)
        all_s1_permutations = list(itertools.permutations(s1_set))
        all_s2_permutations = list(itertools.permutations(s2_set))
        
        unique_s1_arrangements = get_unique_cyclic_and_reversed_arrangements(all_s1_permutations)
        unique_s2_arrangements = get_unique_cyclic_and_reversed_arrangements(all_s2_permutations)
        
        found_cyclic_match_for_pair = False # Flag for current S1, S2 pair
        
        for perm1 in unique_s1_arrangements:
            for perm2 in unique_s2_arrangements:
                
                # Check 1st to 5th cyclic product sums
                cyclic_sums_match = True
                for m in range(1, 6): # m=1 to 5
                    sum1 = cyclic_product_sum(perm1, m)
                    sum2 = cyclic_product_sum(perm2, m)
                    
                    if sum1 != sum2:
                        cyclic_sums_match = False
                        break
                
                if cyclic_sums_match:
                    found_cyclic_match_for_pair = True
                    print(f"  Found matching cyclic product sums for arrangements:")
                    print(f"    S1 arrangement: {perm1}")
                    print(f"    S2 arrangement: {perm2}")

                    # Step 3: Check Diagonal Product Sum
                    diag_sum1 = diagonal_product_sum(perm1)
                    diag_sum2 = diagonal_product_sum(perm2)
                    
                    if diag_sum1 == diag_sum2:
                        print(f"  Diagonal product sums match: {diag_sum1}")

                        # Step 4: Check Regular Triangle Product Sum
                        tri_sum1 = regular_triangle_product_sum(perm1)
                        tri_sum2 = regular_triangle_product_sum(perm2)
                        
                        if tri_sum1 == tri_sum2:
                            print(f"  Regular triangle product sums match: {tri_sum1}")
                            soaisu_ring_pairs.append((perm1, perm2))
                            print(f"  >>> Found 6-6 SOAISU heart heart heart heart heart Ring Pair! <<<")
                        else:
                            print(f"  Regular triangle product sums DO NOT match. S1: {tri_sum1}, S2: {tri_sum2}")
                    else:
                        print(f"  Diagonal product sums DO NOT match. S1: {diag_sum1}, S2: {diag_sum2}")
                
        if not found_cyclic_match_for_pair:
            print(f"  No arrangements with matching 1-5 cyclic product sums found for S1={s1_set}, S2={s2_set}")

    if not soaisu_ring_pairs:
        print("\n--- Step 2, 3, 4 Complete: No 6-6 SOAISU heart heart heart heart heart Ring pairs found. ---")
    else:
        print(f"\n--- Step 2, 3, 4 Complete: Found {len(soaisu_ring_pairs)} 6-6 SOAISU heart heart heart heart heart Ring pairs. ---")
        print("\n--- All 6-6 SOAISU heart heart heart heart heart Ring Pairs Found: ---")
        for i, (p1, p2) in enumerate(soaisu_ring_pairs):
            print(f"Pair {i+1}:")
            print(f"  S1: {p1}")
            print(f"  S2: {p2}")
            print(f"  Cyclic Product Sums (m=1 to 5):")
            for m in range(1, 6):
                print(f"    m={m}: {cyclic_product_sum(p1, m)}")
            print(f"  Diagonal Product Sum: {diagonal_product_sum(p1)}")
            print(f"  Regular Triangle Product Sum: {regular_triangle_product_sum(p1)}")
            print("-" * 30)


# --- Main execution ---
if __name__ == "__main__":
    # Example usage: Set the upper limit 'n' for natural numbers
    # WARNING: Setting n_limit too high will result in very long computation times.
    # For demonstration, a small n_limit might not find any solutions.
    # The smallest known 6-6 PTE solution (shifted to positive integers) involves numbers up to 22.
    # Example: {0, 5, 6, 16, 17, 22} and {1, 2, 10, 12, 20, 21}
    # If we shift this to start from 1, it might be {1, 6, 7, 17, 18, 23} and {2, 3, 11, 13, 21, 22}
    # This means n_limit should be at least 23 to find such a solution.
    
    # For the example from the user's previous turn:
    # S1 = {5, 14, 16, 34, 36, 45}
    # S2 = {6, 10, 21, 29, 40, 44}
    # The maximum number is 45, so n_limit should be at least 45 to find this specific pair.
    
    n_limit_input = int(input("Enter the upper limit (n) for natural numbers (e.g., 25 or 45 for known solutions): "))
    find_soaisu_rings_in_range(n_limit_input)
