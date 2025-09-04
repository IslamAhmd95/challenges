class AccountInfoMixin:
    def display_account_info(self):
        print(
            f"This account of type {self.account_type.upper()} is owned by ({self.name}) and created at {self.creation_date}"
        )

