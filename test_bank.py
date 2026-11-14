import pytest
from Konto import Konto
from Sparbuch import Sparbuch

# =====================================================================
# 🏦 SECTION 1: TESTING BASE KONTO ENCAPSULATION
# =====================================================================

def test_konto_initialization():
    """Verify that a standard account initializes its values correctly."""
    k = Konto("DE111", "Anna", 500)
    assert k.kontonummer == "DE111"
    assert k.inhaber == "Anna"
    # 🔴 Fixed: Removed .get_kontostand() method call in favor of property attribute syntax
    assert k.kontostand == 500

def test_konto_private_attribute_restriction():
    """Prove that encapsulation is active and __kontostand cannot be read directly."""
    k = Konto("DE111", "Anna", 500)
    with pytest.raises(AttributeError):
        _ = k.__kontostand

def test_konto_invalid_deposit():
    """Verify that entering negative amounts triggers our safety error."""
    k = Konto("DE111", "Anna", 500)
    with pytest.raises(ValueError, match="Betrag muss positiv sein!"):
        k.einzahlen(-50)


# =====================================================================
# 🐖 SECTION 2: TESTING SPARBUCH POLYMORPHISM
# =====================================================================

def test_sparbuch_floor_limit():
    """Verify that Sparbuch successfully blocks withdrawals leaving less than 50€."""
    sb = Sparbuch("DE222", "Ben", 100)
    
    # 1. Valid withdrawal (leaves exactly 50€)
    sb.abheben(50)
    # 🔴 Fixed: Removed .get_kontostand() method call in favor of property attribute syntax
    assert sb.kontostand == 50

    # 2. Invalid withdrawal (attempts to drop below 50€ floor)
    with pytest.raises(ValueError, match="Sparbuch muss mindestens 50 Euro Guthaben behalten!"):
        sb.abheben(5)
