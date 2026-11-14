server_liste = ["Router-01", "Switch-02", "Firewall-03"]

# Step 1: Create the bookmark (Iterator)
bookmark = iter(server_liste)

# Step 2: Pull items one by one
print("1. Schritt:", next(bookmark))
print("2. Schritt:", next(bookmark))
print("3. Schritt:", next(bookmark))

# Step 3: Try pulling a 4th item (raises StopIteration!)
try:
    print("4. Schritt:", next(bookmark))
except StopIteration:
    print("Fertig! Der Iterator hat keine Elemente mehr (StopIteration).")
