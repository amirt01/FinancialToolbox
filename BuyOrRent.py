def gen_mortgage_cost_fixed(home_price: int, down_payment: int, mortgage_interest_rate: float, loan_term: int):
    total_cost = home_price
    for _ in range(1, loan_term + 1):
        monthly_cost = total_cost / loan_term
        total_cost += home_price * mortgage_interest_rate

def gen_mortgage_cost_percent(down_payment: float, loan_term: int):
    for _ in range(1, loan_term + 1):
        ...


if __name__ == "__main__":
    ...
