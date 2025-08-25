def add_expense(description: str, amount: float):
    return {"description": description, "amount": amount}


def list_expenses(expenses: list) -> None:
    final_list = ''
    for index, expense in enumerate(expenses, start=1):
        final_list += f"{index}. {expense['description']} - ${expense['amount']}\n"
    return final_list


def total_expenses(expenses: list) -> str:
    total = 0
    for expense in expenses:
        total += expense['amount']
    total_spent = f"Total spent: ${total}"
    return total_spent


def export_to_csv(filename: str, data: str) -> None:
    with open(filename, "w") as f:
        f.write(data)
    print(f"Exported to {filename}")
