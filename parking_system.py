"""
Smart Parking Payment Kiosk
Optimized DFA-Based Version
"""

class ParkingKiosk:

    RATES = {
        1: ("2-Hour", 3),
        2: ("5-Hour", 5),
        3: ("Daily", 15)
    }

    ACCEPTED_NOTES = [1, 5, 10]

    STATE_IDLE = "IDLE"
    STATE_MONEY_INSERTED = "MONEY_INSERTED"
    STATE_PAYMENT_PROCESSED = "PAYMENT_PROCESSED"
    STATE_DISPENSING_CHANGE = "DISPENSING_CHANGE"

    def __init__(self):
        self.state = self.STATE_IDLE
        self.balance = 0

    # =========================
    # INSERT MONEY
    # =========================
    def insert_money(self, amount):

        if amount not in self.ACCEPTED_NOTES:
            print("✗ Invalid note. Only RM1, RM5, RM10 accepted.")
            return

        if self.state not in [self.STATE_IDLE, self.STATE_MONEY_INSERTED]:
            print("✗ Cannot insert money now.")
            return

        self.balance += amount

        if self.state == self.STATE_IDLE:
            self.state = self.STATE_MONEY_INSERTED

        print(f"✓ RM{amount} inserted.")
        print(f"Balance: RM{self.balance:.2f}")

    # =========================
    # PROCESS PAYMENT
    # =========================
    def process_payment(self, option):

        if option not in self.RATES:
            print("Invalid rate option.")
            return

        rate_name, rate_amount = self.RATES[option]

        if self.state != self.STATE_MONEY_INSERTED:
            print("✗ Insert money first.")
            return

        if self.balance < rate_amount:
            print("✗ Insufficient balance.")
            return

        self.balance -= rate_amount
        self.state = self.STATE_PAYMENT_PROCESSED

        print("\n==============================")
        print("        PARKING RECEIPT")
        print("==============================")
        print(f"Type: {rate_name}")
        print(f"Paid: RM{rate_amount:.2f}")
        print(f"Remaining Balance: RM{self.balance:.2f}")
        print("==============================\n")

        if self.balance == 0:
            print("✓ Exact amount received.")
            self.reset()
        else:
            print("💰 Change available. Press [R] to return.")

    # =========================
    # CANCEL
    # =========================
    def cancel(self):

        if self.state != self.STATE_MONEY_INSERTED:
            print("✗ Nothing to cancel.")
            return

        print("⚠ Transaction cancelled.")
        self.state = self.STATE_DISPENSING_CHANGE
        self.dispense_change()

    # =========================
    # RETURN CHANGE
    # =========================
    def return_change(self):

        if self.state != self.STATE_PAYMENT_PROCESSED:
            print("✗ No change available.")
            return

        self.state = self.STATE_DISPENSING_CHANGE
        self.dispense_change()

    # =========================
    # DISPENSE CHANGE
    # =========================
    def dispense_change(self):

        change = self.balance
        print(f"\n💵 Dispensing RM{change:.2f}")

        remaining = change

        for note in [10, 5, 1]:
            count = 0
            while remaining >= note:
                remaining -= note
                count += 1
            if count > 0:
                print(f"RM{note} x {count}")

        print("==============================")

        self.reset()

    # =========================
    # RESET
    # =========================
    def reset(self):
        self.balance = 0
        self.state = self.STATE_IDLE
        print("✓ Kiosk Ready.\n")


# =========================
# WELCOME SCREEN (GLOBAL)
# =========================

def display_welcome_screen():
    print("\n" + "=" * 50)
    print("         SMART PARKING PAYMENT KIOSK SYSTEM")
    print("=" * 50)

    rates_info = [
        ("First 2 Hours", "RM3.00"),
        ("Up to 5 Hours", "RM5.00"),
        ("Daily (>5 hours)", "RM15.00")
    ]

    print("\n📋 PARKING RATES:")
    for duration, price in rates_info:
        print(f"   • {duration:.<15} {price}")

    print("\n💵 ACCEPTED NOTES: RM10, RM5, RM1")
    print("=" * 50 + "\n")


# =========================
# MAIN LOOP
# =========================

def main():

    display_welcome_screen()

    kiosk = ParkingKiosk()
    running = True

    while running:

        print(f"State: {kiosk.state:<15} | Balance: RM{kiosk.balance:.2f}")
        print("-" * 50)

        if kiosk.state == kiosk.STATE_IDLE:
            print("[I] Insert Money")
            print("[Q] Quit")

        elif kiosk.state == kiosk.STATE_MONEY_INSERTED:

            print("[I] Insert Money")

            for option, (name, price) in kiosk.RATES.items():
                if kiosk.balance >= price:
                    print(f"[{option}] Pay {name} (RM{price})")

            print("[C] Cancel")
            print("[Q] Quit")

        elif kiosk.state == kiosk.STATE_PAYMENT_PROCESSED:
            print("[R] Return Change")
            print("[Q] Quit")

        choice = input("Choose: ").upper()

        if choice == "I" and kiosk.state in [kiosk.STATE_IDLE, kiosk.STATE_MONEY_INSERTED]:
            try:
                amount = int(input("Insert note (1/5/10): "))
                kiosk.insert_money(amount)
            except ValueError:
                print("Invalid input.")

        elif choice.isdigit():
            kiosk.process_payment(int(choice))

        elif choice == "C":
            kiosk.cancel()

        elif choice == "R":
            kiosk.return_change()

        elif choice == "Q":
            print("Exiting kiosk.")
            running = False

        else:
            print("Invalid selection.")

        print()


if __name__ == "__main__":
    main()