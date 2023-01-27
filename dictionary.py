# 3.7 version python has dictionary ordered , earlier it was unordered
# Key : Value pairing with any data type
# changeable


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "com": "Ford"
}
print(thisdict)

modelName = thisdict["model"]
print(modelName)

attributes = thisdict.items()
print(attributes)
thisdict["model"] = "Aura" 
print(attributes)

thisdict.update({"color":"red"})
print(thisdict)