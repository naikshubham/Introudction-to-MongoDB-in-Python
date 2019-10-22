# Create a filter for laureates who died in the USA
criteria = {"diedCountry": "USA"}

# Save the count of these laureates
count = db.laureates.count_documents(criteria)
print(count)

# Create a filter for laureates who died in the USA but were born in Germany
criteria = {"diedCountry": "USA", 
            "bornCountry": "Germany"}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)

# Create a filter for Germany-born laureates who died in the USA and with the first name "Albert"
criteria = {"bornCountry": "Germany", 
            "diedCountry": "USA", 
            "firstname": "Albert"}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)

# Save a filter for laureates born in the USA, Canada, or Mexico
criteria = { "bornCountry": 
                { "$in": ["USA","Canada","Mexico"]}
             }

# Count them and save the count
count = db.laureates.count_documents(criteria)
print(count)

# Save a filter for laureates who died in the USA and were not born there
criteria = { "diedCountry": "USA",
               "bornCountry": { "$ne": "USA"}, 
             }

# Count them
count = db.laureates.count_documents(criteria)
print(count)
