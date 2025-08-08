# soaisu-ring-code

programA（soaisu_ring_finder）

Overview

This Python program searches for pairs of soaisu , which are ideal solutions to the Prouhet-Tarry-Escott problem, within a specified range of natural numbers. It then identifies which of these pairs, when arranged in a specific order, satisfy all the conditions for a 6-6 soaisu❤︎❤︎❤︎❤︎❤︎  ring as defined in the paper (power sums, cyclic product sums, diagonal product sums, and regular triangle product sums).


How to Run

This program is compatible with a Python 3.x environment and requires no special libraries.
	1	Save the Python file (soaisu_ring_finder.py) to your local environment.
	2	Navigate to the directory where the file is saved using your terminal or command prompt.
	3	Execute the following command:Bashpython soaisu_ring_finder.py
	4	
	5	When the program starts, you'll be prompted with "Enter the upper limit (n) for natural numbers:". Enter the upper bound of the range you wish to search.


Important Notes

	•	Computation Time Warning: Due to its combinatorial search nature, the program's execution time increases dramatically as the upper limit (n) gets larger. For example, setting n to 25 or higher may take several hours to days to complete.
	•	Known Examples: To find the soaisu ring pairs discussed in the paper, you need to set the upper limit to 24 or higher.


Key Features

	•	find_soaisu_rings_in_range(n_limit):
	◦	Searches for 6-6 soaisu pairs (two sets with matching power sums) within the range of integers up to n_limit.
	◦	Considers all possible permutations of the found soaisu pairs to identify specific arrangements that meet the additional conditions for a soaisu ring (cyclic product sums, diagonal product sums, and regular triangle product sums).
	•	Helper Functions:
	◦	calculate_power_sums: Computes the power sums for a given set.
	◦	cyclic_product_sum: Calculates the cyclic product sum for a given sequence.
	◦	diagonal_product_sum: Computes the diagonal product sum for a 6-element sequence.
	◦	regular_triangle_product_sum: Computes the regular triangle product sum for a 6-element sequence.
	◦	get_unique_cyclic_and_reversed_arrangements: Filters a list of permutations to find unique arrangements, treating cyclic and reversed orders as equivalent.


—————

programB（soaisu_ring_validator）
Overview

This Python program validates whether two sets of six integers, provided by the user, meet all the conditions for a 6-6 soaisu ring as defined in the paper.
The program performs the following steps in its verification process:
	1	soaisu (amicable numbers) Verification: Checks if the power sums from the 1st to the 5th degree match between the two sets.
	2	soaisu Ring Verification: Explores all possible arrangements of the sets to determine if a specific ordering exists that satisfies the additional conditions of matching cyclic product sums, diagonal product sums, and regular triangle product sums.
	3	Embedded soaisu Ring Verification: Confirms if the two 3-element subsets, which are inscribed triangles within the 6-6 soaisu ring, also form a 3-3 soaisu ring.


How to Run

This program is compatible with a Python 3.x environment and does not require any special libraries.
	1	Save the Python file (soaisu_ring_validator.py) to your local machine.
	2	Open your terminal or command prompt and navigate to the directory where the file is saved.
	3	Execute the following command:Bashpython soaisu_ring_validator.py
	4	
	5	When the program starts, two prompts will appear in succession.
	◦	For the first prompt, enter the six elements for the first set (S1), separated by commas or spaces.
	◦	For the second prompt, enter the six elements for the second set (S2).
	6	Input Example:5, 14, 16, 34, 36, 45


Important Notes

	•	Computation Time: The program's verification process involves checking all possible permutations of the input sets, so the computation time may vary depending on the complexity of the input.
	•	Known soaisu Rings: You can use the known soaisu ring examples from the paper for verification.
	◦	Pair 0: S1 = {5, 14, 34, 45, 36, 16} / S2 = {6, 21, 40, 44, 29, 10}
	◦	Pair 1: S1 = {2, 12, 35, 48, 38, 15} / S2 = {3, 20, 42, 47, 30, 8}
	◦	Please refer to the paper for other examples.


Key Features

	•	main_program():
	◦	Accepts user input and verifies if the sets satisfy all the soaisu ring conditions, then prints the results.
	•	calculate_power_sums(s_list, max_power):
	◦	Calculates the power sums for a given list from the 1st to the max_power degree.
	•	cyclic_product_sum(sequence, m):
	◦	Computes the m-th cyclic product sum for an ordered sequence.
	•	diagonal_product_sum(sequence):
	◦	Calculates the diagonal product sum for a 6-element sequence.
	•	regular_triangle_product_sum(sequence):
	◦	Calculates the regular triangle product sum for a 6-element sequence.
	•	get_unique_cyclic_and_reversed_arrangements(permutations_list):
	◦	Filters a list of permutations to find unique arrangements, treating cyclic and reversed orders as equivalent.
	•	parse_input_set(prompt):
	◦	Parses user input to return a set of six integers.

—————
programC（soaisu_ring_algebraic_verifier）
Overview

This Python program takes two sets of six integers, provided by the user, and algebraically verifies whether they maintain the structure of a 6-6 soaisu ring when each element is transformed into a polynomial of the form an+m.
The program expands and compares the following conditions for both sets to determine if their resulting polynomials are identical:
	•	Power sums from the 1st to 5th degree
	•	Cyclic product sums from the 1st to 5th degree
	•	Diagonal product sum
	•	Regular triangle product sum
	•	Conditions for the embedded 3-3 soaisu rings (power sums and cyclic product sums for the 1st and 2nd degree)


How to Run

This program is compatible with a Python 3.x environment. It requires the SymPy symbolic computation library to run.
	1	First, install SymPy:Bashpip install sympy
	2	
	3	Save the Python file (soaisu_ring_algebraic_verifier.py) to your local machine.
	4	Open your terminal or command prompt and navigate to the directory where the file is saved.
	5	Execute the following command:Bashpython soaisu_ring_algebraic_verifier.py
	6	
	7	When the program starts, you will be prompted for two inputs:
	◦	First, enter the six elements for set S1, separated by commas.
	◦	Next, enter the six elements for set S2.
	8	Input Example:5,14,34,45,36,16


Important Notes

	•	Input Format: The program expects six comma-separated integers.
	•	Algebraic Verification: This program is designed to prove that the ring structure holds for any integer values of n and m, not just for specific numbers. If all conditions match, it implies the existence of an infinite number of soaisu ring pairs.


Key Features

	•	verify_all_conditions_with_nm(s1_base, s2_base):
	◦	Transforms each element of the input sets into the polynomial val * n + m.
	◦	Computes and compares all defined ring conditions as polynomials to check for equality.
	•	parse_input_set(prompt):
	◦	Parses user input and returns a list of six integers.
	•	cyclic_prod_sum_expr(arr, m_power):
	◦	Calculates the m_power-th cyclic product sum for a list of polynomials.
	•	__main__:
	◦	Prompts the user for input, calls the verification function, and prints the final result.