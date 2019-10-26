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

# Filter for laureates born in Austria with non-Austria prize affiliation
criteria = {"bornCountry": "Austria", 
              "prizes.affiliations.country": {"$ne": "Austria"}}

# Count the number of such laureates
count = db.laureates.count_documents(criteria)
print(count)

# Filter for documents without a "born" field
criteria = { "born": {"$exists": False}}

# Save count
count = db.laureates.count_documents(criteria)
print(count)

# Filter for laureates with at least three prizes
criteria = {"prizes.2": {"$exists": True}}

# Find one laureate with at least three prizes
doc = db.laureates.find_one(criteria)

# Print the document
print(doc)























