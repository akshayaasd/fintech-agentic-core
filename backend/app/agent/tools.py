from langchain_core.tools import tool

# -------------------------------------------------------------------------
# Accounts Tools (Phase 7 Mock)
# -------------------------------------------------------------------------

@tool
def get_account_balance(account_number: str = "default") -> str:
    """
    Retrieves the current balance for the specified account.
    """
    # Mock implementation
    return f"The balance for account {account_number} is $4,500.00."

@tool
def get_account_details(account_number: str = "default") -> str:
    """
    Retrieves the details (type, status, etc.) for the specified account.
    """
    # Mock implementation
    return f"Account {account_number} is an Active Checking Account."


# -------------------------------------------------------------------------
# Transactions Tools (Phase 7 Mock)
# -------------------------------------------------------------------------

@tool
def transfer_funds(amount: float, to_account: str) -> str:
    """
    Transfers the specified amount to the target account.
    """
    # Mock implementation
    return f"Successfully transferred ${amount} to account {to_account}. Reference ID: TXN-987654321."

@tool
def get_recent_transactions(limit: int = 5) -> str:
    """
    Retrieves the most recent transactions for the user.
    """
    # Mock implementation
    return (
        f"Here are your last {limit} transactions:\n"
        "- Amazon.com: $45.99\n"
        "- Starbucks: $4.50\n"
        "- Salary Deposit: +$3,000.00"
    )


# -------------------------------------------------------------------------
# Service Tools (Phase 7 Mock)
# -------------------------------------------------------------------------

@tool
def request_cheque_book(account_number: str = "default", leaves: int = 25) -> str:
    """
    Requests a new cheque book for the specified account.
    """
    # Mock implementation
    return f"A new cheque book with {leaves} leaves has been requested for account {account_number}. It will be delivered in 3-5 business days."

@tool
def update_kyc(document_type: str, document_id: str) -> str:
    """
    Submits a request to update KYC (Know Your Customer) information.
    """
    # Mock implementation
    return f"KYC update request submitted with {document_type} (ID ending in ...{document_id[-4:] if len(document_id) > 4 else document_id}). Pending verification."

