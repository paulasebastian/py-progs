n_terms = int(input("Enter the number of terms: "))

n1 = 0
n2 = 1

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print(f"Fibonacci series up to {n_terms} term:")
    print(n1)
else:
    print("Fibonacci series:")
    
    for i in range(n_terms):
        print(n1, end=" ")
        
        next_term = n1 + n2
        
        n1 = n2
        n2 = next_term