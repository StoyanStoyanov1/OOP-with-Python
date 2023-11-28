from exams.exam_10_december_2022.project import Adult
from exams.exam_10_december_2022.project import Student
from exams.exam_10_december_2022.project import MortgageLoan
from exams.exam_10_december_2022.project import StudentLoan


class BankApp:
    VALID_LOAN = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN:
            raise Exception("Invalid loan type!")
        new_loan = self.VALID_LOAN[loan_type]()
        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT:
            raise Exception("Invalid client type!")

        if not len(self.clients) < self.capacity:
            return "Not enough bank capacity."

        new_client = self.VALID_CLIENT[client_type](client_name, client_id, income)
        self.clients.append(new_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = [client for client in self.clients if client.client_id == client_id][0]
        loan = [loan for loan in self.loans if loan.TYPE == loan_type][0]
        current_client_type = client.TYPE
        current_loan_type = loan.TYPE

        if (current_client_type == "Student" and current_loan_type != "StudentLoan") or \
                (current_client_type == "Adult" and current_loan_type != "MortgageLoan"):
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = [client for client in self.clients if client.client_id == client_id]

        if not client:
            raise Exception("No such client!")

        client = client[0]

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = len([loan.increase_interest_rate() for loan in self.loans if loan.TYPE == loan_type])

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = len([client.increase_clients_interest()
                                           for client in self.clients if client.interest < min_rate])

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum([client.income for client in self.clients])
        loans_count_granted_to_clients = sum([len(client.loans) for client in self.clients])
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([loan.amount for loan in self.loans])
        granted_sum = sum([sum([loan.amount for loan in client.loans])for client in self.clients])
        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients) \
            if self.clients else 0

        return f"""Active Clients: {total_clients_count}
Total Income: {total_clients_income:.2f}
Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}
Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_client_interest_rate:.2f}"""

