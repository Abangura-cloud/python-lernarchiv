# =====================================================================
# PART 1: The Correct, Clean Library Class
# =====================================================================
class Bibliothek:
    def __init__(self, name):
        self.name = name
        # Task 1: Ausleihliste as a distinct instance attribute
        self.ausgeliehene_buecher = []

    def ausleihen(self, buchtitel):
        # Buchtitel zur Liste hinzufügen
        self.ausgeliehene_buecher.append(buchtitel)

    # Subtask 1: Triggering and analyzing the 'self' error
    # INTENTIONAL ERROR: We omit 'self' to trigger the positional argument mismatch.
    # def zurueckgeben(buchtitel): 
    #     pass

    # FIXED VERSION (After encountering the error):
    def zurueckgeben(self, buchtitel):
        if buchtitel in self.ausgeliehene_buecher:
            self.ausgeliehene_buecher.remove(buchtitel)


"""
SUBTASK 1 ANALYSIS (The 'self' Error Comment):
---------------------------------------------------------------------
When calling `my_library.return_book("Title")` without `self` in the parameter definition:
- Python automatically passes the instance (`self`) as the first argument behind the scenes.
- Therefore, Python actually passes TWO arguments: (the_instance, "Title").
- However, because the method was defined as `def zurueckgeben(buchtitel):`, it only expects ONE argument.
- Error Message look: "TypeError: zurueckgeben() takes 1 positional argument but 2 were given."
- Fix: Adding `self` as the first parameter tells Python where to bind the instance context.
---------------------------------------------------------------------
"""

# =====================================================================
# PART 2: The Flawed Version with Shared Class Attribute
# =====================================================================
class BibliothekFehlerhaft:
    # 🚨 PITFALL: Defined here, this list belongs to the CLASS, not the instance!
    ausgeliehene_buecher = []

    def __init__(self, name):
        self.name = name

    def ausleihen(self, buchtitel):
        self.ausgeliehene_buecher.append(buchtitel)


"""
SUBTASK 2 ANALYSIS (The Shared Class Attribute Comment):
---------------------------------------------------------------------
OBSERVATION: 
When Instance A borrows "Book 1" and Instance B borrows "Book 2", BOTH books 
show up in both libraries' selection lists. 

WHY THIS HAPPENS (The Mutable Default Pitfall Connection):
- Class attributes are created exactly ONCE when Python reads the class blueprint into memory.
- Because a list `[]` is a mutable object, all instances share a single pointer pointing 
  to the exact same list in memory.
- This is identical to the "mutable default argument" trap in functions where `def foo(my_list=[])` 
  appends elements to a shared global list across different function invocations.
- `instance_a.ausgeliehene_buecher is instance_b.ausgeliehene_buecher` evaluates to True!
---------------------------------------------------------------------
"""


# =====================================================================
# 🧪 MANUAL VERIFICATION RUNNER
# =====================================================================
if __name__ == "__main__":
    print("=== SUBTASK 1: Verifying Correct Class ===")
    meine_bib = Bibliothek("Stadtbibliothek Nord")
    meine_bib.ausleihen("Python Crash Course")
    meine_bib.ausleihen("Clean Code")
    print(f"Bücher in '{meine_bib.name}': {meine_bib.ausgeliehene_buecher}")
    
    print("\nTesting Book Return...")
    meine_bib.zurueckgeben("Clean Code")
    print(f"Nach Rückgabe: {meine_bib.ausgeliehene_buecher}")


    print("\n=== SUBTASK 2: Demonstrating the Pitfall ===")
    bib_a = BibliothekFehlerhaft("Zweigstelle Ost")
    bib_b = BibliothekFehlerhaft("Zweigstelle West")

    bib_a.ausleihen("Der Hobbit")
    bib_b.ausleihen("Harry Potter")

    print(f"Bib A ({bib_a.name}) Liste: {bib_a.ausgeliehene_buecher}")
    print(f"Bib B ({bib_b.name}) Liste: {bib_b.ausgeliehene_buecher}")
    
    # Check if they share the exact memory address
    are_same = bib_a.ausgeliehene_buecher is bib_b.ausgeliehene_buecher
    print(f"Verweisen beide Listen auf dasselbe Speicherobjekt? {are_same}")

    print("\n=== SUBTASK 2 CORRECTION: Verifying Independent Lists ===")
    # Using the correct class from Part 1 to show how it should behave
    korrekt_a = Bibliothek("Zweigstelle Ost (Fix)")
    korrekt_b = Bibliothek("Zweigstelle West (Fix)")

    korrekt_a.ausleihen("Der Hobbit")
    korrekt_b.ausleihen("Harry Potter")

    print(f"Korrekt A ({korrekt_a.name}) Liste: {korrekt_a.ausgeliehene_buecher}")
    print(f"Korrekt B ({korrekt_b.name}) Liste: {korrekt_b.ausgeliehene_buecher}")
    
    # Verify they are now completely independent objects in memory
    are_same_now = korrekt_a.ausgeliehene_buecher is korrekt_b.ausgeliehene_buecher
    print(f"Verweisen beide Listen auf dasselbe Speicherobjekt? {are_same_now}")

