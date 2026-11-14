def ping_generator(server_liste):
    """A generator function that yields one status at a time instead of building a huge list."""
    for server in server_liste:
        print(f"  [Generator arbeitet gerade an {server}...]")
        yield f"{server}: ONLINE"


if __name__ == "__main__":
    geraete = ["Router-Magdeburg-01", "Switch-02", "Firewall-03"]

    # Calling the function does NOT run the loop yet! It returns a Generator object.
    gen = ping_generator(geraete)
    print("Generator erstellt:", gen)

    # Now we pull values one by one using a for-loop (which calls next() automatically)
    print("\nStarte Abfrage:")
    for status in gen:
        print("Empfangen ->", status)
