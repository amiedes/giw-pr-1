db.usuarios.find(
  {
      "country": "SELECTED COUNTRY",
      "likes": {
        "$size": "SIZE",
        "$all": [1, 2, 3]  // Lista de aficiones, separadas por comas
      }
  }
).sort('nombre_campo', pymongo.ASCENDING).limit("LIMIT").pretty();


db.usuarios.find({
  "address.country": "Gabón",
  "likes": { "$all": ['football', 'books'] }
}).sort({'birthdate': 1}).limit(10).pretty();
