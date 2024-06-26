import happybase as hb


connection = hb.Connection()

connection.create_table(
    "powers",
    {
        "personal": dict(),
        "professional": dict(),
        "custom": dict(),
    }
)

connection.create_table(
    "food",
    {
        "nutrition": dict(),
        "taste": dict(),
    }
)

connection.close()
