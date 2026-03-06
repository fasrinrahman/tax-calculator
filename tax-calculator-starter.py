# ============================================
# SRI LANKAN TAX CALCULATOR PROJECT
# Session 04: Functions, Lambdas & Functional Programming
# ============================================
# Name: _____________________________
# Date: _____________________________

# ============================================
# SRI LANKA TAX BRACKETS (Effective April 1, 2025)
# ============================================
# Annual Income (LKR):
#   Up to 1,800,000: 0% (Tax-free!)
#   1,800,001 - 2,800,000: 6%
#   2,800,001 - 3,300,000: 18%
#   3,300,001 - 3,800,000: 24%
#   3,800,001 - 4,300,000: 30%
#   Greater than 4,300,000: 36%
# ============================================


def calculate_income_tax(annual_income):
    """
    Calculate progressive income tax based on Sri Lankan tax brackets
    (effective April 1, 2025).

    Args:
        annual_income: Annual income in LKR (float or int)

    Returns:
        Total income tax amount (float)

    Example:
        >>> calculate_income_tax(4000000)
        330000.0
    """
    # YOUR CODE HERE
    # Implement the progressive tax calculation
    # pass
    tax_fee = 0

    if annual_income == 0:
        return 0
    # because annual_income 0 can be lead to miss calculation

    if annual_income <= 1800000:  # above it 1 rupee change
        # tax free
        tax_fee = 0
    elif annual_income <= 2800000:
        tax_fee = (annual_income - 1800000) * 0.06
        # coz, always 1.8M have free charge of tax
    elif annual_income <= 3300000:
        # 1.8 m - free tax
        # 2.8 m - 6% ( another 1m going to - 6% )
        # 3.3 m - 18% ( rest of after 1.8 + 1 m = 2.8m going to 18% )
        # all sum is tax_fee
        tax_fee = 1000000 * 0.06 + (annual_income - 2800000) * 0.18
    elif annual_income <= 3800000:
        # 1.8m -free tax
        # 2.8m - 6% (another 1m)    # 3.3m - 18% (another 0.5m [3.3m-2.8m]) # 3.8m - 24%

        tax_fee = 1000000 * 0.06 + 500000 * 0.18 + (annual_income - 3300000) * 0.24

    elif annual_income <= 4300000:
        # another increase by 0.5m

        tax_fee = (
            1000000 * 0.06
            + 500000 * 0.18
            + 500000 * 0.24
            + (annual_income - 3800000) * 0.30
        )

    #   Greater than 4,300,000: 36%
    # another last increase 0.5m
    else:
        tax_fee = (
            1000000 * 0.06
            + 500000 * 0.18
            + 500000 * 0.24
            + 500000 * 0.30
            + (annual_income - 4300000) * 0.36
        )

    return tax_fee


def calculate_effective_tax_rate(annual_income):
    """
    Calculate effective tax rate as a percentage.

    Args:
        annual_income: Annual income in LKR (float or int)

    Returns:
        Effective tax rate as percentage (float)

    Example:
        >>> calculate_effective_tax_rate(4000000)
        8.25
    """
    # YOUR CODE HERE
    # pass
    tax_fee = calculate_income_tax(annual_income)

    return (tax_fee / annual_income) * 100


def calculate_take_home(annual_income):
    """
    Calculate take-home income after tax.

    Args:
        annual_income: Annual income in LKR (float or int)

    Returns:
        Take-home income (float)

    Example:
        >>> calculate_take_home(4000000)
        3670000.0
    """
    # YOUR CODE HERE
    # pass

    tax_fee = calculate_income_tax(annual_income)

    return annual_income - tax_fee


# ============================================
# HELPER FUNCTIONS FOR DISPLAY (PROVIDED)
# ============================================


def print_taxpayer_details(income):
    """Print detailed tax information for a single taxpayer"""
    tax = calculate_income_tax(income)
    effective_rate = calculate_effective_tax_rate(income)
    take_home = calculate_take_home(income)
    monthly_take_home = take_home / 12

    print(f"\nAnnual Income: Rs. {income:,.2f}")
    print(f"  Income Tax: Rs. {tax:,.2f} ({effective_rate:.2f}%)")
    print(f"  Take-Home (Annual): Rs. {take_home:,.2f}")
    print(f"  Take-Home (Monthly): Rs. {monthly_take_home:,.2f}")
    print("-" * 60)


def print_ranking(sorted_income_tax_pairs):
    """Print ranked list of taxpayers by tax paid"""
    for rank, (income, tax) in enumerate(sorted_income_tax_pairs, start=1):
        print(f"{rank}. Rs. {income:,.2f} - Tax Paid: Rs. {tax:,.2f}")


def print_high_earners(high_earner_incomes):
    """Print details for high earners (>= Rs. 4,300,000)"""
    for income in high_earner_incomes:
        tax = calculate_income_tax(income)
        print(f"Income: Rs. {income:,.2f} - Tax: Rs. {tax:,.2f}")


# ============================================
# MAIN PROGRAM
# ============================================


def main():
    """Main program to demonstrate tax calculations"""

    # Test data: Multiple taxpayer incomes (in LKR)
    incomes = [2500000, 4000000, 5000000, 1500000, 3500000]

    print("=" * 60)
    print("SRI LANKAN TAX CALCULATOR (April 2025 Tax Reforms)")
    print("=" * 60)

    # ========================================
    # TODO 1: Calculate taxes for all incomes using map()
    # ========================================
    # Use map() to calculate income tax for each income

    taxes = list(
        map(calculate_income_tax, incomes)
    )  # YOUR CODE HERE - replace with map()

    # ========================================
    # TODO 2: Filter high earners using filter()
    # ========================================
    # Find all incomes >= Rs. 4,300,000 (highest tax bracket)

    high_earners = list(
        filter(lambda income: income >= 4300000, incomes)
    )  # YOUR CODE HERE - replace with filter()

    # ========================================
    # TODO 3: Create (income, tax) pairs and sort
    # ========================================
    # 1. Use zip() to pair incomes with taxes
    # 2. Use sorted() to rank by tax amount (highest first)

    income_tax_pairs = list(zip(incomes, taxes))

    sorted_incomes_taxes = list(
        sorted(income_tax_pairs, key=lambda i: i[1], reverse=True)
    )  # YOUR CODE HERE - replace with zip() and sorted()

    # ========================================
    # Display Results (Provided - No need to modify)
    # ========================================

    # Display detailed tax reports
    print("\n" + "=" * 60)
    print("DETAILED TAX REPORTS")
    print("=" * 60)
    for income in incomes:
        print_taxpayer_details(income)

    # Display top taxpayers ranking
    print("\n" + "=" * 60)
    print("TOP TAXPAYERS (Ranked by Tax Paid)")
    print("=" * 60)
    print_ranking(sorted_incomes_taxes)

    # Display high earners
    print("\n" + "=" * 60)
    print("HIGH EARNERS (>= Rs. 4,300,000 - Top Tax Bracket)")
    print("=" * 60)
    print_high_earners(high_earners)

    # ========================================
    # BONUS: Calculate summary statistics
    # ========================================
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)

    # YOUR CODE HERE (BONUS)
    # Calculate and print:
    # - Total tax revenue: sum(taxes)
    total_taxes = sum(taxes)
    print(f"Total Amount of Taxes :-  Rs.{total_taxes}")
    # print("\n")
    
    # - Average effective tax rate {so percentage} (toatl of effective tax / total effective income )*100
    # avg_effective_tax_rate = (sum(calculate_effective_tax_rate)/len(incomes))*100
    # print(f"Avarage effective Tax Rate :- {avg_effective_tax_rate}")
    
    
    
    
    # - Highest and lowest tax amounts: max(taxes), min(taxes)
    highest_tax_fee = max(taxes)
    print(f"Highest Amount in Taxes :-  Rs.{highest_tax_fee}")
    # print("\n")
    
    lowest_tax_fee = min(taxes)
    print(f"Lowest Amount in Taxes :-  Rs.{lowest_tax_fee}")
    print("\n")
    
    # - Average monthly take-home


# Run the program
if __name__ == "__main__":
    main()
